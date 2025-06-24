import unittest

from htmlnode import HTMLNode
from leadnode import LeafNode



class TestLeafNode(unittest.TestCase):    
    def test_leaf_href(self):
        props = {"one": "value_one", "two": "value_two"}
        node = LeafNode("link","Testing!",props=props)
        self.assertEqual(node.to_html(), '<link one="value_one" two="value_two">Testing!</link>')
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()