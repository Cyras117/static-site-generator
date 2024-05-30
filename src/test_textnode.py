import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold","https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold","https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold","https://www.boot.net")
        node2 = TextNode("This is a text node", "bold","https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq_text_type(self):
        node = TextNode("This is a text node", "bold","https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold","https://www.boot.dev")
        self.assertEqual(node.text_type, node2.text_type)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", "bold","https://www.boot.dev")
        node2 = TextNode("This is a text node", "roboto","https://www.boot.dev")
        self.assertNotEqual(node.text_type, node2.text_type)

    def test_url_none(self):
        node = TextNode("This is a text node", "bold",None)
        self.assertEqual(node.url,None)



if __name__ == "__main__":
    unittest.main()
