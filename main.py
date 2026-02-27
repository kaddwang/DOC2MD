#!/usr/bin/env python3
"""
DOC2MD — Multi-modal Docx to GitBook Markdown Automation Tool
═════════════════════════════════════════════════════════════
Converts .docx files (with embedded images) into structured,
RAG-friendly Markdown for GitBook, powered by OpenAI GPT-4o.

Usage
─────
  # Convert a single file
  python main.py path/to/document.docx

  # Convert all .docx files in the default input/ folder
  python main.py

  # Convert all .docx files in a custom folder
  python main.py --input-dir /path/to/folder
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from config.settings import INPUT_DIR, OUTPUT_DIR
from src.docx_parser import parse_docx
from src.ai_processor import process_with_ai
from src.markdown_writer import save_markdown


def convert_file(docx_path: Path) -> Path:
    """
    Full pipeline for a single .docx file:
    parse → AI process → write Markdown.

    Returns the path of the generated .md file.
    """
    file_name = docx_path.name
    print(f"  📄 Parsing:    {file_name}")
    elements = parse_docx(docx_path)

    text_count = sum(1 for e in elements if e["type"] == "text")
    image_count = sum(1 for e in elements if e["type"] == "image")
    print(f"     ├─ Text blocks : {text_count}")
    print(f"     ├─ Images      : {image_count}")

    print(f"  🤖 Processing: Sending to GPT-4o ...")
    markdown = process_with_ai(elements, file_name)

    print(f"  💾 Writing:    {docx_path.stem}.md")
    output_path = save_markdown(markdown, file_name)

    print(f"  ✅ Done:       {output_path}")
    return output_path


def gather_docx_files(source: str | None) -> list[Path]:
    """
    Determine which .docx files to process.

    - If *source* is a path to a single .docx file, return it.
    - If *source* is a directory, return all .docx files inside.
    - If *source* is None, use the default ``input/`` directory.
    """
    if source is None:
        target = INPUT_DIR
    else:
        target = Path(source)

    if target.is_file():
        if target.suffix.lower() != ".docx":
            print(f"❌ Error: {target} is not a .docx file.")
            sys.exit(1)
        return [target]

    if target.is_dir():
        files = sorted(target.glob("*.docx"))
        if not files:
            print(f"⚠️  No .docx files found in: {target}")
            sys.exit(0)
        return files

    print(f"❌ Error: Path does not exist: {target}")
    sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="DOC2MD — Convert .docx files to GitBook Markdown via GPT-4o"
    )
    parser.add_argument(
        "source",
        nargs="?",
        default=None,
        help=(
            "Path to a single .docx file or a directory containing .docx files. "
            "Defaults to the input/ folder."
        ),
    )
    parser.add_argument(
        "--input-dir",
        dest="input_dir",
        default=None,
        help="Alias for the source argument (directory of .docx files).",
    )
    args = parser.parse_args()

    source = args.source or args.input_dir

    docx_files = gather_docx_files(source)

    print("=" * 60)
    print("  DOC2MD — Docx → GitBook Markdown Converter")
    print(f"  Files to process : {len(docx_files)}")
    print(f"  Output directory : {OUTPUT_DIR}")
    print("=" * 60)

    success_count = 0
    fail_count = 0

    for idx, docx_path in enumerate(docx_files, start=1):
        print(f"\n[{idx}/{len(docx_files)}] {docx_path.name}")
        print("-" * 40)
        try:
            convert_file(docx_path)
            success_count += 1
        except Exception as exc:
            print(f"  ❌ Failed: {exc}")
            fail_count += 1

    print("\n" + "=" * 60)
    print(f"  🏁 Completed:  {success_count} succeeded, {fail_count} failed")
    print("=" * 60)


if __name__ == "__main__":
    main()
