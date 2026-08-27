from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_benchmark  # noqa: E402


class BenchmarkHelpersTest(unittest.TestCase):
    def test_heading_matching_allows_specialized_heading_suffix(self) -> None:
        self.assertTrue(
            validate_benchmark.heading_matches("High-Agency Options (3)", "High-Agency Options")
        )
        self.assertFalse(
            validate_benchmark.heading_matches("High-Agency Options", "High-Agency Action")
        )

    def test_prompt_bank_parser_preserves_canonical_order(self) -> None:
        text = (
            "## example\n"
            "### Happy path\nPrompt\n"
            "### Missing critical info\nPrompt\n"
            "### Conflicting objectives\nPrompt\n"
            "### High-stakes constraint\nPrompt\n"
        )
        self.assertEqual(
            validate_benchmark.parse_prompt_bank(text),
            {
                "example": [
                    "Happy path",
                    "Missing critical info",
                    "Conflicting objectives",
                    "High-stakes constraint",
                ]
            },
        )

    def test_current_repository_satisfies_benchmark_contract(self) -> None:
        self.assertEqual(validate_benchmark.validate(), [])


if __name__ == "__main__":
    unittest.main()
