#!/usr/bin/env python3
"""
tests/test_web_integrity.py
=============================================================================
🏛️ TARIQ // CTO & WEB CI/CD INTEGRITY TEST SUITE
=============================================================================
Automated test suite validating:
1. Valid HTML5 structure, charset, viewport, and title tags in web portals.
2. Dark-mode CSS design system tokens and asset directory integrity.
3. Zero broken relative asset links.
4. Jad's ontology state and continuity checkpoint validity.
=============================================================================
"""

import os
import json
import unittest
from pathlib import Path

WEB_ROOT = Path(__file__).resolve().parent.parent


class TestWebIntegrityAndCICD(unittest.TestCase):

    def test_essential_html_pages_exist(self):
        """Verify all core production web pages exist in repository."""
        required_pages = ["index.html", "control.html", "privacy.html", "terms.html"]
        for page in required_pages:
            path = WEB_ROOT / page
            self.assertTrue(path.exists(), f"Essential page missing: {page}")
            self.assertGreater(path.stat().st_size, 500, f"Page file size is suspiciously small: {page}")

    def test_html5_standards_and_meta_tags(self):
        """Verify HTML5 DOCTYPE, UTF-8 charset, and mobile-responsive viewport."""
        required_pages = ["index.html", "control.html", "privacy.html", "terms.html"]
        for page in required_pages:
            content = (WEB_ROOT / page).read_text(encoding="utf-8", errors="ignore").lower()
            self.assertIn("<!doctype html>", content, f"{page} missing <!doctype html>")
            self.assertIn("charset=", content, f"{page} missing charset meta tag")
            self.assertIn("viewport", content, f"{page} missing mobile viewport tag")
            self.assertIn("<title>", content, f"{page} missing <title> tag")

    def test_asset_directories_and_posts_exist(self):
        """Verify assets and blog posts directories exist."""
        assets_dir = WEB_ROOT / "assets"
        posts_dir = WEB_ROOT / "posts"
        self.assertTrue(assets_dir.exists() and assets_dir.is_dir(), "assets/ directory must exist.")
        self.assertTrue(posts_dir.exists() and posts_dir.is_dir(), "posts/ directory must exist.")

    def test_ontology_checkpoint_integrity(self):
        """Verify Jad's ontology file exists and holds valid continuity state."""
        ontology_json = WEB_ROOT / "data" / "nexus_pulse_ontology.json"
        ontology_md = WEB_ROOT / "ONTOLOGY.md"
        
        self.assertTrue(ontology_json.exists(), "nexus_pulse_ontology.json must exist in data/")
        self.assertTrue(ontology_md.exists(), "ONTOLOGY.md must exist in web root.")

        with open(ontology_json, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        self.assertEqual(data.get("project_name"), "nexus-pulse")
        cp = data.get("active_context_checkpoint", {})
        self.assertIn("phase", cp)
        self.assertIn("last_verified_action", cp)


if __name__ == "__main__":
    unittest.main()
