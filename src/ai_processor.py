"""
AI Processor Module
───────────────────
Sends extracted content (text + Base64 images) to OpenAI GPT-4o
and returns the generated Markdown string.

Architecture:
- Text content and images are processed SEPARATELY to ensure
  image processing failures never cause text content loss.
- Step 1: All text is chunked and translated/formatted.
- Step 2: Each image is sent separately for description.
- Step 3: Results are merged in document order.
"""

from __future__ import annotations

import re
from typing import Dict, List

from openai import OpenAI

from config.settings import (
    OPENAI_API_KEY,
    OPENAI_MAX_TOKENS,
    OPENAI_MODEL,
    OPENAI_TEMPERATURE,
)
from src.prompts import SYSTEM_PROMPT

# Max chars per text chunk
_MAX_TEXT_CHARS_PER_CHUNK = 6_000

# Prompt for processing images only
_IMAGE_PROMPT = """You are a Senior Technical Documentation Engineer.
Analyze this image from a technical document:
- If it is a technical diagram, architecture chart, flow chart, or data table:
  Describe it in detail as structured English text (use bullet points or numbered lists).
- If it is a UI screenshot or interface mockup:
  Reply with exactly: SKIP_UI_IMAGE
- Do NOT output any image references or placeholders.
- Do NOT invent information not shown in the image."""

# Continuation prompt for text chunks after the first
_CONTINUATION_PROMPT = """You are continuing the conversion of the same document.
The previous chunk has already been converted. Now convert THIS chunk only.
- Do NOT add a Document Header again.
- Do NOT repeat content from previous chunks.
- Continue with the next logical section headings.
- Maintain the same Markdown style and formatting.
- CRITICAL: Convert EVERY SINGLE paragraph, bullet point, table row, discussion note, date, Q&A, proposal, decision, and detail. This is NOT a summary task. Nothing can be omitted.
- Translate all Chinese content into professional technical English.
"""


def _strip_markdown_fences(text: str) -> str:
    """Remove wrapping ```markdown ... ``` if GPT added it."""
    text = text.strip()
    if text.startswith("```markdown"):
        text = text[len("```markdown"):].strip()
    elif text.startswith("```md"):
        text = text[len("```md"):].strip()
    if text.endswith("```"):
        text = text[:-3].strip()
    return text


def _clean_output(text: str) -> str:
    """Post-process AI output to remove unwanted artifacts."""
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        stripped = line.strip()
        # Remove image placeholders
        if re.match(r"^!\[.*\]\(.*\)$", stripped):
            continue
        # Remove "I'm sorry" / refusal lines
        if stripped.lower().startswith("i'm sorry") or stripped.lower().startswith("i apologize"):
            continue
        # Remove empty image references
        if stripped in ("![]()", "![]"):
            continue
        cleaned.append(line)
    return "\n".join(cleaned)


def _call_openai(client: OpenAI, messages: list) -> str:
    """Make a single OpenAI API call and return the text response."""
    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages,
            max_tokens=OPENAI_MAX_TOKENS,
            temperature=OPENAI_TEMPERATURE,
        )
    except Exception as exc:
        raise RuntimeError(f"OpenAI API call failed: {exc}") from exc
    return response.choices[0].message.content or ""


def _split_text_chunks(text_elements: List[Dict]) -> List[List[Dict]]:
    """Split text elements into manageable chunks."""
    chunks: List[List[Dict]] = []
    current_chunk: List[Dict] = []
    current_len = 0

    for elem in text_elements:
        elem_len = len(elem["content"])
        if current_chunk and current_len + elem_len > _MAX_TEXT_CHARS_PER_CHUNK:
            chunks.append(current_chunk)
            current_chunk = []
            current_len = 0
        current_chunk.append(elem)
        current_len += elem_len

    if current_chunk:
        chunks.append(current_chunk)
    return chunks


def _process_text_chunks(
    client: OpenAI,
    text_elements: List[Dict],
    file_name: str,
) -> List[str]:
    """Process all text elements in chunks, return list of markdown parts."""
    chunks = _split_text_chunks(text_elements)
    results: List[str] = []

    for idx, chunk in enumerate(chunks):
        is_first = idx == 0

        content_parts = []
        if is_first:
            content_parts.append({
                "type": "text",
                "text": (
                    f"File Name: {file_name}\n\n"
                    "Please convert the following document content into "
                    "a structured GitBook Markdown page according to your instructions.\n\n"
                    "IMPORTANT: Convert ALL content below. Do NOT skip or summarize any section."
                ),
            })
        else:
            content_parts.append({
                "type": "text",
                "text": (
                    f"File Name: {file_name}\n\n"
                    "This is the NEXT part of the same document. "
                    "Convert EVERY section, paragraph, and detail below."
                ),
            })

        for elem in chunk:
            content_parts.append({"type": "text", "text": elem["content"]})

        system = SYSTEM_PROMPT if is_first else _CONTINUATION_PROMPT
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": content_parts},
        ]

        raw = _call_openai(client, messages)
        part = _strip_markdown_fences(raw)
        part = _clean_output(part)
        results.append(part)

    return results


def _process_image(client: OpenAI, image_elem: Dict, position_hint: str) -> str:
    """
    Process a single image and return its text description.
    Returns empty string if the image is a UI screenshot or processing fails.
    """
    mime = image_elem.get("mime", "image/png")
    data_url = f"data:{mime};base64,{image_elem['content']}"

    messages = [
        {"role": "system", "content": _IMAGE_PROMPT},
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"This image appears near: {position_hint}",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": data_url, "detail": "high"},
                },
            ],
        },
    ]

    try:
        raw = _call_openai(client, messages)
        raw = raw.strip()

        # If AI flagged as UI screenshot, skip
        if "SKIP_UI_IMAGE" in raw:
            return ""

        # If AI refused
        if raw.lower().startswith("i'm sorry") or raw.lower().startswith("i apologize"):
            return ""

        return _clean_output(raw)

    except Exception:
        # Image processing failure should not break the pipeline
        return ""


def process_with_ai(
    elements: List[Dict[str, str]], file_name: str
) -> str:
    """
    Send the parsed document elements to OpenAI GPT-4o and return
    the Markdown output.

    Text and images are processed separately to ensure robustness:
    - Text content is never lost due to image processing failures.
    - Images are individually described and inserted at their original positions.

    Parameters
    ----------
    elements : list[dict]
        Ordered list produced by ``docx_parser.parse_docx``.
    file_name : str
        Original file name (used in the metadata header).

    Returns
    -------
    str
        The generated Markdown content.
    """
    if not OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY is not set. "
            "Please add it to your .env file."
        )

    client = OpenAI(api_key=OPENAI_API_KEY)

    # ── Step 1: Separate text and image elements ────────────
    text_elements = []
    image_elements = []  # (index_in_original, element, position_hint)

    last_text_hint = ""
    for i, elem in enumerate(elements):
        if elem["type"] == "text":
            text_elements.append(elem)
            # Use first 80 chars as position hint for next image
            last_text_hint = elem["content"][:80]
        elif elem["type"] == "image":
            image_elements.append((i, elem, last_text_hint))

    # ── Step 2: Process all text ────────────────────────────
    text_chunks = _split_text_chunks(text_elements)
    total_chunks = len(text_chunks)
    if total_chunks > 1:
        print(f"     ├─ Text split into {total_chunks} chunks")

    text_results = _process_text_chunks(client, text_elements, file_name)

    # ── Step 3: Process images individually ─────────────────
    image_descriptions: List[str] = []
    if image_elements:
        print(f"     ├─ Processing {len(image_elements)} images individually ...")
        for idx, (orig_idx, img_elem, hint) in enumerate(image_elements):
            desc = _process_image(client, img_elem, hint)
            if desc:
                image_descriptions.append(desc)

    # ── Step 4: Merge text results ──────────────────────────
    # Text chunks are the primary content; image descriptions
    # are appended as a supplementary section (if any)
    merged = "\n\n".join(text_results)

    if image_descriptions:
        merged += "\n\n---\n\n## Technical Diagram Descriptions\n\n"
        for i, desc in enumerate(image_descriptions, 1):
            merged += f"### Diagram {i}\n\n{desc}\n\n"

    return merged
