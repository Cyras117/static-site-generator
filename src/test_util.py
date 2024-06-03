import unittest
import utils as u
from textnode import TextNode

class TestUils (unittest.TestCase):
    #text_node_to_html_node===============================================================================================================
    def test_text_node_to_html_node_text_text(self):
        text_node = TextNode("This is a text node", "text", "https://www.boot.dev")
        self.assertEqual(u.text_node_to_html_node(text_node).render(),f'{text_node.text}')
    
    def test_text_node_to_html_node_text_bold(self):
        text_node = TextNode("This is a bold node", "bold", "https://www.boot.dev")
        self.assertEqual(u.text_node_to_html_node(text_node).render(),f'<b>{text_node.text}</b>')
    
    def test_text_node_to_html_node_text_italic(self):
        text_node = TextNode("This is a bold node", "italic", "https://www.boot.dev")
        self.assertEqual(u.text_node_to_html_node(text_node).render(),f'<i>{text_node.text}</i>')

    def test_text_node_to_html_node_text_code(self):
        text_node = TextNode("This is a bold node", "code", "https://www.boot.dev")
        self.assertEqual(u.text_node_to_html_node(text_node).render(),f'<code>{text_node.text}</code>')
    
    def test_text_node_to_html_node_text_link(self):
        text_node = TextNode("This is a bold node", "link", "https://www.boot.dev")
        self.assertEqual(u.text_node_to_html_node(text_node).render(),f'<a href="{text_node.url}">{text_node.text}</a>')
    
    def test_text_node_to_html_node_text_image(self):
        text_node = TextNode("", "image", "https://www.boot.dev")
        self.assertEqual(u.text_node_to_html_node(text_node).render(),f'<img src="{text_node.url}" alt="Alt Text">{text_node.text}</img>')
    
    #split_nodes_delimiter===============================================================================================================
    def test_split_nodes_delimiter_eq(self):
        list_txt = [TextNode("This is text with a `code block` word", "text"),TextNode("This is text with a `code block` word2", "text2")]
        expected = [TextNode("This is text with a ","text"), TextNode("code block","code"), TextNode(" word","text"), TextNode("This is text with a ","text"), TextNode("code block","code"), TextNode(" word2","text")]
        self.assertListEqual(u.split_nodes_delimiter(list_txt,"`","code"),expected)
        
    def test_split_nodes_delimiter_count(self):
        list_txt = [TextNode("This is text with a `code block` word", "text"),TextNode("This is text with a `code block` word2", "text2")]
        expected = [TextNode("This is text with a ","text"), TextNode("code block","code"), TextNode(" word","text"), TextNode("This is text with a ","text"), TextNode("code block","code"), TextNode(" word2","text")]
        self.assertListEqual(u.split_nodes_delimiter(list_txt,"`","code"),expected)

    #extract_markdown_images===============================================================================================================
    def test_extract_markdown_images_count(self):
        txt = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        expected = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        self.assertCountEqual(u.extract_markdown_images(txt),expected)
    
    def test_extract_markdown_images_eq(self):
        txt = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        expected = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        self.assertListEqual(u.extract_markdown_images(txt),expected)

    #extract_markdown_links===============================================================================================================
    def test_extract_markdown_links_count(self):
        txt = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expected = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        self.assertCountEqual(u.extract_markdown_links(txt),expected)
    
    def test_extract_markdown_links_eq(self):
        txt = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expected = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        self.assertListEqual(u.extract_markdown_links(txt),expected)

    #split_images===============================================================================================================
    def test_split_node_images_eq(self):
        nodes = [TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            "text",
            )]
        expected = [TextNode("This is text with an ", "text"), TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), TextNode(" and another ", "text"), TextNode("second image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")]
        self.assertListEqual(u.split_nodes_images(nodes),expected)

    def test_split_node_images_no_images(self):
        nodes = [TextNode(
            "This is text with an not image and another not image",
            "text",
            )]
        expected = [TextNode("This is text with an not image and another not image", "text")]
        self.assertListEqual(u.split_nodes_images(nodes),expected)

    #split_links===============================================================================================================
    def test_split_node_links_eq(self):
        nodes = [TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
            "text",
        )]
        expected = [TextNode("This is text with a ", "text"), TextNode("link", "link", "https://www.example.com"), TextNode(" and ", "text"), TextNode("another", "link", "https://www.example.com/another")]
        self.assertListEqual(u.split_nodes_link(nodes),expected)

    def test_split_node_images_no_images(self):
        nodes = [TextNode(
            "This is text with a link and link",
            "text",
        )]
        expected = [TextNode("This is text with a link and link", "text")]
        self.assertListEqual(u.split_nodes_images(nodes),expected)

if __name__ == "__main__":
    unittest.main()
