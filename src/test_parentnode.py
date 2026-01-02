import unittest

from htmlnode import *
from parentnode import *


class TestParentNode(unittest.TestCase):
    def test_example(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],)
        expected_node = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_node)

    def test_with_props(self):
        node = ParentNode(
        "p",
        [
            LeafNode("a", "Bold text", {"href": "google.com", "target": "_blank"}),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],)
        expected_node = '<p><a href="google.com" target="_blank">Bold text</a>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(), expected_node)


if __name__ == "__main__":
    unittest.main()