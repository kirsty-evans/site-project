import unittest

from htmlnode import *


class TestLeafNode(unittest.TestCase):
    def test_to_html_none_props(self):
        node = LeafNode("p", "hello world")
        expected_node = "<p>hello world</p>"
        self.assertEqual(node.to_html(), expected_node)

    def test_to_html_None_Invalid(self):
        node = LeafNode(None, None, 'banana')
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_None(self):
        node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_2_props(self):
        node = LeafNode("a", "hello world", {"href": "google.com", "target": "_blank"})
        expected_node = '<a href="google.com" target="_blank">hello world</a>'
        self.assertEqual(node.to_html(), expected_node)

if __name__ == "__main__":
    unittest.main()