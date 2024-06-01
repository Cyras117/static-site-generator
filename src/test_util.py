import unittest

from utils import text_node_to_html_node
from utils import split_nodes_delimiter
from textnode import TextNode

class TestUils (unittest.TestCase):
    #text_node_to_html_node===============================================================================================================
    def test_text_node_to_html_node_text_text(self):
        text_node = TextNode("This is a text node", "text", "https://www.boot.dev")
        self.assertEqual(text_node_to_html_node(text_node).render(),f'{text_node.text}')
    
    def test_text_node_to_html_node_text_bold(self):
        text_node = TextNode("This is a bold node", "bold", "https://www.boot.dev")
        self.assertEqual(text_node_to_html_node(text_node).render(),f'<b>{text_node.text}</b>')
    
    def test_text_node_to_html_node_text_italic(self):
        text_node = TextNode("This is a bold node", "italic", "https://www.boot.dev")
        self.assertEqual(text_node_to_html_node(text_node).render(),f'<i>{text_node.text}</i>')

    def test_text_node_to_html_node_text_code(self):
        text_node = TextNode("This is a bold node", "code", "https://www.boot.dev")
        self.assertEqual(text_node_to_html_node(text_node).render(),f'<code>{text_node.text}</code>')
    
    def test_text_node_to_html_node_text_link(self):
        text_node = TextNode("This is a bold node", "link", "https://www.boot.dev")
        self.assertEqual(text_node_to_html_node(text_node).render(),f'<a href="{text_node.url}">{text_node.text}</a>')
    
    def test_text_node_to_html_node_text_image(self):
        text_node = TextNode("", "image", "https://www.boot.dev")
        self.assertEqual(text_node_to_html_node(text_node).render(),f'<img src="{text_node.url}" alt="Alt Text">{text_node.text}</img>')
    
    #split_nodes_delimiter===============================================================================================================
    def test_split_nodes_delimiter(self):
        list_txt = [TextNode("This is text with a `code block` word", "text"),TextNode("This is text with a `code block` word2", "text2")]
        self.assertListEqual(split_nodes_delimiter(list_txt,"`","code"),[TextNode("This is text with a ","text"), TextNode("code block","code"), TextNode(" word","text"), TextNode("This is text with a ","text"), TextNode("code block","code"), TextNode(" word2","text")])

if __name__ == "__main__":
    unittest.main()
