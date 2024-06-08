import unittest
from text_type import TextType
import utils as u
from textnode import TextNode

class TestUils (unittest.TestCase):
    #text_node_to_html_node===============================================================================================================
    def test_text_node_to_html_node_text_text(self):
        text_node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(u.text_node_to_html_node(text_node).render(),f'{text_node.text}')
    
    def test_text_node_to_html_node_text_bold(self):
        text_node = TextNode("This is a bold node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(u.text_node_to_html_node(text_node).render(),f'<b>{text_node.text}</b>')
    
    def test_text_node_to_html_node_text_italic(self):
        text_node = TextNode("This is a bold node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(u.text_node_to_html_node(text_node).render(),f'<i>{text_node.text}</i>')

    def test_text_node_to_html_node_text_code(self):
        text_node = TextNode("This is a bold node", TextType.CODE, "https://www.boot.dev")
        self.assertEqual(u.text_node_to_html_node(text_node).render(),f'<code>{text_node.text}</code>')
    
    def test_text_node_to_html_node_text_link(self):
        text_node = TextNode("This is a bold node", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(u.text_node_to_html_node(text_node).render(),f'<a href="{text_node.url}">{text_node.text}</a>')
    
    def test_text_node_to_html_node_text_image(self):
        text_node = TextNode("", TextType.IMAGE, "https://www.boot.dev")
        self.assertEqual(u.text_node_to_html_node(text_node).render(),f'<img src="{text_node.url}" alt="Alt Text">{text_node.text}</img>')
    
    #split_nodes_delimiter===============================================================================================================
    def test_split_nodes_delimiter_eq(self):
        list_txt = [TextNode("This is text with a `code block` word", TextType.TEXT),TextNode("This is text with a `code block` word2", TextType.TEXT)]
        expected = [TextNode("This is text with a ",TextType.TEXT), TextNode("code block",TextType.CODE), TextNode(" word",TextType.TEXT), TextNode("This is text with a ",TextType.TEXT), TextNode("code block",TextType.CODE), TextNode(" word2",TextType.TEXT)]
        self.assertListEqual(u.split_nodes_delimiter(list_txt,"`",TextType.CODE),expected)
        
    def test_split_nodes_delimiter_count(self):
        list_txt = [TextNode("This is text with a `code block` word", TextType.TEXT),TextNode("This is text with a `code block` word2", TextType.TEXT)]
        expected = [TextNode("This is text with a ",TextType.TEXT), TextNode("code block",TextType.CODE), TextNode(" word",TextType.TEXT), TextNode("This is text with a ",TextType.TEXT), TextNode("code block",TextType.CODE), TextNode(" word2",TextType.TEXT)]
        self.assertListEqual(u.split_nodes_delimiter(list_txt,"`",TextType.CODE),expected)

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
        self.maxDiff = None
        nodes = [TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            TextType.TEXT,
            )]
        expected = [TextNode("This is text with an ", TextType.TEXT), TextNode("image", TextType.IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), TextNode(" and another ", TextType.TEXT), TextNode("second image", TextType.IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")]
        self.assertListEqual(u.split_nodes_images(nodes),expected)

    def test_split_node_images_no_images(self):
        nodes = [TextNode(
            "This is text with an not image and another not image",
            TextType.TEXT,
            )]
        expected = [TextNode("This is text with an not image and another not image", TextType.TEXT)]
        self.assertListEqual(u.split_nodes_images(nodes),expected)

    #split_links===============================================================================================================
    def test_split_node_links_eq(self):
        nodes = [TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
            TextType.TEXT,
        )]
        expected = [TextNode("This is text with a ", TextType.TEXT), TextNode("link", TextType.LINK, "https://www.example.com"), TextNode(" and ", TextType.TEXT), TextNode("another", TextType.LINK, "https://www.example.com/another")]
        self.assertListEqual(u.split_nodes_links(nodes),expected)

    def test_split_node_liks_no_liks(self):
        nodes = [TextNode(
            "This is text with a link and link",
            TextType.TEXT,
        )]
        expected = [TextNode("This is text with a link and link", TextType.TEXT)]
        self.assertListEqual(u.split_nodes_links(nodes),expected)
    #text_to_textnodes===============================================================================================================
    def test_text_to_textnodes_eq(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        expected = [TextNode("This is ", TextType.TEXT), TextNode("text", TextType.BOLD), TextNode(" with an ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word and a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" and an ", TextType.TEXT), TextNode("image", TextType.IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), TextNode(" and a ", TextType.TEXT), TextNode("link", TextType.LINK, "https://boot.dev")]
        self.assertListEqual(u.text_to_textnodes(text),expected)

    def test_text_to_textnodes_only_text(self):
        text = "Text with no delimeters, images or links"
        expected = [TextNode("Text with no delimeters, images or links", TextType.TEXT)]
        self.assertListEqual(u.text_to_textnodes(text),expected)

    #markdown_to_blocks===============================================================================================================
    def test_markdown_to_blocks_eq(self):
        markdown = "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items\n"
        expected = ['\nThis is **bolded** paragraph', '\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', '\n* This is a list\n* with items']
        self.assertListEqual(u.markdown_to_blocks(markdown),expected)





if __name__ == "__main__":
    unittest.main()
