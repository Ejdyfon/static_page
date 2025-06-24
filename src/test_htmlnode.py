import unittest

from htmlnode import HTMLNode



class TestHTMLNode(unittest.TestCase):
#    def test_eq(self):
#        node = HTMLNode(tag="tag", value="value", children="children", props="props")
#        node2 = HTMLNode(tag="tag", value="value", children="children", props="props")
#        self.assertEqual(node, node2)
#    
#    def test_eq_no_props(self):
#        node = HTMLNode(tag="tag", value="value", children="children")
#        node2 = HTMLNode(tag="tag", value="value", children="children")
#        self.assertEqual(node, node2)
#    
#    def test_eq_no_children(self):
#        node = HTMLNode(tag="tag", value="value", props="props")
#        node2 = HTMLNode(tag="tag", value="value", props="props")
#        self.assertEqual(node, node2)
#    
#    def test_not_eq_tag(self):
#        node = HTMLNode(tag="tag", value="value", children="children", props="props")
#        node2 = HTMLNode(tag="1", value="value", children="children", props="props")
#        self.assertNotEqual(node, node2)
#    
#    def test_not_eq_child(self):
#        node = HTMLNode(tag="tag", value="value", children="children")
#        node2 = HTMLNode(tag="tag", value="value")
#       self.assertNotEqual(node, node2)
#

    def test_self_prop_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    
    def test_self_prop_one(self):
        props = {"one": "value_one"}
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(), ' one="value_one"')
    
    def test_self_prop_two(self):
        props = {"one": "value_one", "two": "value_two"}
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(), ' one="value_one" two="value_two"')

if __name__ == "__main__":
    unittest.main()