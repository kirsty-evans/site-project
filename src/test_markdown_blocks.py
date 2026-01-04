import unittest
from markdown_blocks import *


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(
            block_to_block_type("# Heading"),
            BlockType.HEADING
        )
        self.assertEqual(
            block_to_block_type("###### Heading"),
            BlockType.HEADING
        )

    def test_heading_too_many_hashes(self):
        self.assertEqual(
            block_to_block_type("####### Heading"),
            BlockType.PARAGRAPH
        )

    def test_code_block(self):
        block = "```\ncode\n```"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.CODE
        )

    def test_quote(self):
        self.assertEqual(
            block_to_block_type("> quoted text"),
            BlockType.QUOTE
        )

    def test_unordered_list_dash(self):
        self.assertEqual(
            block_to_block_type("- item"),
            BlockType.UNORDERED_LIST
        )

    def test_unordered_list_asterisk(self):
        self.assertEqual(
            block_to_block_type("* item"),
            BlockType.UNORDERED_LIST
        )

    def test_ordered_list(self):
        self.assertEqual(
            block_to_block_type("1. item"),
            BlockType.ORDERED_LIST
        )

    def test_paragraph(self):
        self.assertEqual(
            block_to_block_type("Just some text."),
            BlockType.PARAGRAPH
        )


if __name__ == "__main__":
    unittest.main()
