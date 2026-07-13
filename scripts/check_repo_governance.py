#!/usr/bin/env python3
"""Validate the minimum AI-agent governance structure of the repository."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "AGENT_BOARD.md",
    "CLAUDE.md",
    ".github/copilot-instructions.md",
    "TASKS.md",
    "ARCHITECTURE.md",
    "ROADMAP.md