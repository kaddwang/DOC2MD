"""
Configuration settings for the DOC2MD project.
Loads environment variables and defines project-wide constants.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# ── Project Root ──────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ── Load .env ─────────────────────────────────────────────────
load_dotenv(PROJECT_ROOT / ".env")

# ── OpenAI Settings ───────────────────────────────────────────
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL: str = "gpt-4o"
OPENAI_MAX_TOKENS: int = 4096
OPENAI_TEMPERATURE: float = 0.1  # Low temperature to reduce hallucination

# ── I/O Directories ──────────────────────────────────────────
INPUT_DIR: Path = PROJECT_ROOT / "input"
OUTPUT_DIR: Path = PROJECT_ROOT / "output"

# Ensure directories exist
INPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
