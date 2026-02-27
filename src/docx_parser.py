"""
Docx Parser Module
──────────────────
Reads a .docx file and extracts text paragraphs and inline images
in their original order.  Each element is returned as a dictionary:

    {"type": "text",  "content": "paragraph text ..."}
    {"type": "image", "content": "<base64 string>", "mime": "image/png"}
"""

import base64
import io
import re
from pathlib import Path
from typing import List, Dict

from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT


def _get_image_base64(image_part) -> tuple[str, str]:
    """Extract base64-encoded data and MIME type from an image part."""
    blob: bytes = image_part.blob
    content_type: str = image_part.content_type  # e.g. "image/png"
    b64_str = base64.b64encode(blob).decode("utf-8")
    return b64_str, content_type


def _extract_paragraph_elements(paragraph, rels) -> List[Dict[str, str]]:
    """
    Walk through the XML of a single paragraph and yield text / image
    elements *in the order they appear*.

    A paragraph may contain multiple runs, some of which embed images
    via ``<a:blip r:embed="rId…"/>``.
    """
    from docx.oxml.ns import qn

    elements: List[Dict[str, str]] = []
    text_buffer: list[str] = []

    for child in paragraph._element:
        # ── Run element (<w:r>) ──────────────────────────────
        if child.tag == qn("w:r"):
            # Check for inline images inside the run
            drawings = child.findall(f".//{qn('a:blip')}")
            if drawings:
                # Flush accumulated text first
                if text_buffer:
                    joined = "".join(text_buffer).strip()
                    if joined:
                        elements.append({"type": "text", "content": joined})
                    text_buffer.clear()

                for blip in drawings:
                    embed_id = blip.get(qn("r:embed"))
                    if embed_id and embed_id in rels:
                        rel = rels[embed_id]
                        image_part = rel.target_part
                        b64, mime = _get_image_base64(image_part)
                        elements.append(
                            {"type": "image", "content": b64, "mime": mime}
                        )
            else:
                # Normal text run
                run_text = child.text or ""
                # Also collect <w:t> children
                for t_elem in child.findall(qn("w:t")):
                    run_text += t_elem.text or ""
                text_buffer.append(run_text)

    # Flush remaining text
    if text_buffer:
        joined = "".join(text_buffer).strip()
        if joined:
            elements.append({"type": "text", "content": joined})

    return elements


def parse_docx(file_path: str | Path) -> List[Dict[str, str]]:
    """
    Parse a .docx file and return an ordered list of content elements.

    Parameters
    ----------
    file_path : str | Path
        Path to the .docx file.

    Returns
    -------
    list[dict]
        Each dict has ``type`` ("text" | "image") and ``content``.
        Image dicts additionally carry a ``mime`` key.
    """
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    if file_path.suffix.lower() != ".docx":
        raise ValueError(f"Not a .docx file: {file_path}")

    doc = Document(str(file_path))
    rels = doc.part.rels  # relationships dict for resolving image rIds

    all_elements: List[Dict[str, str]] = []

    for paragraph in doc.paragraphs:
        para_elements = _extract_paragraph_elements(paragraph, rels)
        all_elements.extend(para_elements)

    # Merge consecutive text elements for cleaner payloads
    merged: List[Dict[str, str]] = []
    for elem in all_elements:
        if (
            elem["type"] == "text"
            and merged
            and merged[-1]["type"] == "text"
        ):
            merged[-1]["content"] += "\n" + elem["content"]
        else:
            merged.append(elem)

    return merged
