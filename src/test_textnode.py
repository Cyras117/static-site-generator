import unittest

from textnode import (
    TextNode,
    text_node_to_html_node,
    BOLD,
    TEXT,
    ITALIC,
    IMAGE,
    CODE,
    LINK
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", BOLD,"https://www.boot.dev")
        node2 = TextNode("This is a text node", BOLD,"https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", BOLD,"https://www.boot.net")
        node2 = TextNode("This is a text node", BOLD,"https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq_text_type(self):
        node = TextNode("This is a text node", BOLD,"https://www.boot.dev")
        node2 = TextNode("This is a text node", BOLD,"https://www.boot.dev")
        self.assertEqual(node.text_type, node2.text_type)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", BOLD,"https://www.boot.dev")
        node2 = TextNode("This is a text node", TEXT,"https://www.boot.dev")
        self.assertNotEqual(node.text_type, node2.text_type)

    def test_eq_url(self):
        node = TextNode("This is a text node", ITALIC, "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", ITALIC, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", BOLD,None)
        self.assertEqual(node.url,None)

    def test_repr(self):
        node = TextNode("This is a text node", TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

#text_node_to_html_node===============================================================================================================
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_text_node_to_html_node_text_text(self):
        text_node = TextNode("This is a text node", TEXT, "https://www.boot.dev")
        self.assertEqual(text_node.text,"This is a text node")
        self.assertEqual(text_node.text_type,TEXT)
        self.assertEqual(text_node.url,"https://www.boot.dev")
    
    def test_text_node_to_html_node_text_bold(self):
        text_node = TextNode("This is a bold text node", BOLD, "https://www.boot.dev")
        self.assertEqual(text_node.text,"This is a bold text node")
        self.assertEqual(text_node.text_type,BOLD)
        self.assertEqual(text_node.url,"https://www.boot.dev")
    
    def test_text_node_to_html_node_text_italic(self):
        text_node = TextNode("This is a italic text node", ITALIC, "https://www.boot.dev")
        self.assertEqual(text_node.text,"This is a italic text node")
        self.assertEqual(text_node.text_type,ITALIC)
        self.assertEqual(text_node.url,"https://www.boot.dev")

    def test_text_node_to_html_node_text_code(self):
        text_node = TextNode("This is a code text node", CODE, "https://www.boot.dev")
        self.assertEqual(text_node.text,"This is a code text node")
        self.assertEqual(text_node.text_type,CODE)
        self.assertEqual(text_node.url,"https://www.boot.dev")
    
    def test_text_node_to_html_node_text_link(self):
        text_node = TextNode("This is a bold node", LINK, "https://www.boot.dev")
        self.assertEqual(text_node.text, "This is a bold node")
        self.assertEqual(text_node.text_type, LINK)
        self.assertEqual(text_node.url, "https://www.boot.dev")


if __name__ == "__main__":
    unittest.main()
