import html.parser
import pathlib
import unittest
from urllib.parse import urlsplit

ROOT = pathlib.Path(__file__).resolve().parents[1]
PUBLIC_PAGES = (
    "index.html", "workshop.html", "library.html", "vestigia-runtime.html",
    "vestigia.html", "daemon-bridge.html", "archive.html", "mcp-server.html",
)

class Links(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])

def parsed(path):
    parser = Links()
    parser.feed((ROOT / path).read_text(encoding="utf-8"))
    return parser

class SiteContractTests(unittest.TestCase):
    def test_internal_links_resolve(self):
        docs = {name: parsed(name) for name in PUBLIC_PAGES}
        for name, doc in docs.items():
            for link in doc.links:
                parts = urlsplit(link)
                if parts.scheme or parts.netloc or not parts.path:
                    continue
                target_name = (ROOT / name).parent.joinpath(parts.path).name
                if target_name not in PUBLIC_PAGES:
                    continue
                target = (ROOT / name).parent / parts.path
                self.assertTrue(target.exists(), f"{name}: missing {link}")
                if parts.fragment:
                    self.assertIn(parts.fragment, docs[target_name].ids,
                                  f"{name}: missing fragment in {link}")

    def test_library_links_to_archive_and_mcp(self):
        links = parsed("library.html").links
        self.assertIn("archive.html", links)
        self.assertIn("mcp-server.html", links)

    def test_versions_are_labeled_as_development(self):
        runtime = (ROOT / "vestigia-runtime.html").read_text(encoding="utf-8").lower()
        mcp = (ROOT / "mcp-server.html").read_text(encoding="utf-8").lower()
        self.assertIn("0.8.0.dev0", runtime)
        self.assertIn("development", runtime)
        self.assertIn("0.10.0.dev0", mcp)
        self.assertIn("development", mcp)

    def test_bridge_activity_and_mcp_boundary_are_distinct(self):
        page = (ROOT / "daemon-bridge.html").read_text(encoding="utf-8").lower()
        self.assertIn("active", page)
        self.assertIn("resident-configured bells", page)
        self.assertIn("mcp", page)
        self.assertIn("logs", page)
        self.assertIn("relay", page)

    def test_workshop_leads_with_two_lanes_and_keeps_commons(self):
        page = (ROOT / "workshop.html").read_text(encoding="utf-8").lower()
        self.assertIn("relational continuity", page)
        self.assertIn("agent and mcp reliability", page)
        self.assertIn("free", page)
        self.assertIn("commons", page)

    def test_public_site_omits_signal_and_payment_handles(self):
        public = "\n".join((ROOT / name).read_text(encoding="utf-8") for name in PUBLIC_PAGES).lower()
        for private_handle in ("jeffpadget.66", "$jeffpadget", "paypal.me/echocollaboration"):
            self.assertNotIn(private_handle, public)

    def test_runtime_card_and_site_log_show_growth(self):
        home = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="vestigia-runtime.html">🏡 VESTIGIA Runtime', home)
        self.assertIn("v1.3", home)
        self.assertIn("Still growing.", home)

    def test_workshop_invitation_is_centered(self):
        page = (ROOT / "workshop.html").read_text(encoding="utf-8")
        self.assertIn("workshop-invitation--centered", page)
        styles = (ROOT / "css/components.css").read_text(encoding="utf-8")
        self.assertRegex(styles, r"\.workshop-invitation--centered\s*\{[^}]*margin-inline:\s*auto")

    def test_shell_lists_platform_links_on_separate_lines_and_reports_archive_scale(self):
        page = (ROOT / "vestigia.html").read_text(encoding="utf-8")
        self.assertIn('<ul class="platform-links">', page)
        self.assertIn("18,012 files", page)
        self.assertIn("21.9 GB", page)
        self.assertIn("1,848 files", page)

    def test_mcp_catalog_groups_all_capabilities_and_highlights_commander(self):
        page = (ROOT / "mcp-server.html").read_text(encoding="utf-8")
        self.assertIn("69 named MCP capabilities", page)
        self.assertIn("Magic: The Gathering Commander", page)
        self.assertIn("game.shortcut_propose", page)
        self.assertIn("archive.promote_directory", page)
        self.assertIn("runtime.write_capabilities", page)
        self.assertEqual(page.count("<code>"), 69)
        self.assertEqual(page.count('<details class="capability-group"'), 7)

if __name__ == "__main__":
    unittest.main()

