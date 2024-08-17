import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def props(self):
        node = HTMLNode(
        tag="a",
        value=None,  # Since we're focusing on props, this can be None
        children=None,
        props={"href": "https://www.google.com", "target": "_blank"}
        )

        actual_op = node.props_to_html()
        expected_op = 'href="https://www.google.com" target="_blank"'
        assert actual_op == expected_op, f"Expected: {expected_op}, but got: {actual_op}"


if __name__ == "__main__":
    unittest.main()