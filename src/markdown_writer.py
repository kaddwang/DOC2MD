"""
Markdown Writer Module
──────────────────────
Writes the generated Markdown content to a .md file in the output directory.
"""

from pathlib import Path

from config.settings import OUTPUT_DIR


def save_markdown(markdown_content: str, original_filename: str) -> Path:
    """
    Save the Markdown string to a ``.md`` file.

    The output file will have the same stem as the original docx file
    but with a ``.md`` extension, and will be placed in ``OUTPUT_DIR``.

    Parameters
    ----------
    markdown_content : str
        The Markdown text to write.
    original_filename : str
        The original ``.docx`` filename (e.g. ``"spec.docx"``).

    Returns
    -------
    Path
        The path of the written ``.md`` file.
    """
    stem = Path(original_filename).stem
    output_path = OUTPUT_DIR / f"{stem}.md"
    output_path.write_text(markdown_content, encoding="utf-8")
    return output_path
