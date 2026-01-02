import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html1(self):
        node = HTMLNode("p", "hello world", None, None)
        expected_node = ""
        self.assertEqual(node.props_to_html(), expected_node)


    def test_props_to_html2(self):
        node = HTMLNode(None, None, None, {"href": "google.com", "target": "_blank"})
        expected_node = ' href="google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_node)

    def test_props_to_html3(self):
        node = HTMLNode(None, None, None, {"href": "google.com"})
        expected_node = ' href="google.com"'
        self.assertEqual(node.props_to_html(), expected_node)

    def test_props_to_html4(self):
        node = HTMLNode(None, None, None, {})
        expected_node = ''
        self.assertEqual(node.props_to_html(), expected_node)

    def test_props_to_html5(self):
        node = HTMLNode(None, None, None, 'banana')
        with self.assertRaises(TypeError):
            node.props_to_html()

if __name__ == "__main__":
    unittest.main()