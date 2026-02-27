"""
AI Processor Module
───────────────────
Sends extracted content (text + Base64 images) to OpenAI GPT-4o
and returns the generated Markdown string.
"""

from typing import List, Dict

from openai import OpenAI

from config.settings import (
    OPENAI_API_KEY,
    OPENAI_MODEL,
    OPENAI_MAX_TOKENS,
    OPENAI_TEMPERATURE,
)
from src.prompts import SYSTEM_PROMPT


def _build_user_content(
    elements: List[Dict[str, str]], file_name: str
) -> list:
    """
    Build the ``content`` array for the user message.

    The array interleaves ``{"type": "text", ...}`` and
    ``{"type": "image_url", ...}`` items so that GPT-4o
    processes them in the original document order.
    """
    content_parts: list = []

    # Prepend an instruction with the file name
    content_parts.append(
        {
            "type": "text",
            "text": (
                f"File Name: {file_name}\n\n"
                "Please convert the following document content into "
                "a structured GitBook Markdown page according to your instructions."
            ),
        }
    )

    for elem in elements:
        if elem["type"] == "text":
            content_parts.append({"type": "text", "text": elem["content"]})
        elif elem["type"] == "image":
            mime = elem.get("mime", "image/png")
            data_url = f"data:{mime};base64,{elem['content']}"
            content_parts.append(
                {
                    "type": "image_url",
                    "image_url": {"url": data_url, "detail": "high"},
                }
            )

    return content_parts


def process_with_ai(
    elements: List[Dict[str, str]], file_name: str
) -> str:
    """
    Send the parsed document elements to OpenAI GPT-4o and return
    the Markdown output.

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

    Raises
    ------
    ValueError
        If the API key is missing.
    RuntimeError
        If the API call fails.
    """
    if not OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY is not set. "
            "Please add it to your .env file."
        )

    client = OpenAI(api_key=OPENAI_API_KEY)

    user_content = _build_user_content(elements, file_name)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_content},
    ]

    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages,
            max_tokens=OPENAI_MAX_TOKENS,
            temperature=OPENAI_TEMPERATURE,
        )
    except Exception as exc:
        raise RuntimeError(f"OpenAI API call failed: {exc}") from exc

    choice = response.choices[0]
    markdown_text: str = choice.message.content or ""

    return markdown_text.strip()
