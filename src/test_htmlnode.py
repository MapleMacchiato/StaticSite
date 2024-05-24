import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_prop(self):
        html_node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        target_str = ' href="https://www.google.com" target="_blank"'
        res_str = html_node.props_to_html()
        self.assertEqual(target_str, res_str)
