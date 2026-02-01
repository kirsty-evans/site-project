import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_with_header(self):
        markdown = "# This is the title\n\nSome content here."
        expected_title = "This is the title"
        self.assertEqual(extract_title(markdown), expected_title)

    def test_with_header2(self):
        markdown = "Some content here.\n\n# This is the title\n\n"
        expected_title = "This is the title"
        self.assertEqual(extract_title(markdown), expected_title)

    def test_no_header(self):
        markdown = "Some content here.\n\nThis is the title\n\n"
        with self.assertRaises(Exception):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()