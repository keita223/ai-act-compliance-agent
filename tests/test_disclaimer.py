"""Tests for the shared legal disclaimer."""

from ai_act_agent.disclaimer import LEGAL_DISCLAIMER


def test_disclaimer_is_not_empty() -> None:
    assert isinstance(LEGAL_DISCLAIMER, str) and LEGAL_DISCLAIMER.strip()


def test_disclaimer_says_it_does_not_replace_legal_advice() -> None:
    assert "legal advice" in LEGAL_DISCLAIMER
