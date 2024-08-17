import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(
        tag="a",
        value=None,  # Since we're focusing on props, this can be None
        children=None,
        props={"href": "https://www.google.com", "target": "_blank"}
        )

        actual_op = node.props_to_html()
        expected_op = 'href="https://www.google.com" target="_blank"'
        assert actual_op == expected_op, f"Expected: {expected_op}, but got: {actual_op}"

    def test_leaf_to_html(self):
        leaf1 = LeafNode("This is a simple text node")
        self.assertEqual(leaf1.to_html(), "This is a simple text node")

        leaf2 = LeafNode("This is a paragraph", tag="p")
        self.assertEqual(leaf2.to_html(), "<p>This is a paragraph</p>")
    
    def test_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode("").to_html()

if __name__ == "__main__":
    unittest.main()