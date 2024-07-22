import unittest
import utils as u
from textnode import( 
    TextNode,
    TEXT,
    LINK,
    BOLD,
    CODE,
    IMAGE,
    ITALIC
    )

class TestUils (unittest.TestCase):
    #split_nodes_delimiter===============================================================================================================
    def test_split_nodes_delimiter_eq(self):
        list_txt = [TextNode("This is text with a `code block` word", TEXT),TextNode("This is text with a `code block` word2", TEXT)]
        expected = [TextNode("This is text with a ",TEXT), TextNode("code block",CODE), TextNode(" word",TEXT), TextNode("This is text with a ",TEXT), TextNode("code block",CODE), TextNode(" word2",TEXT)]
        self.assertListEqual(u.split_nodes_delimiter(list_txt,"`",CODE),expected)
        
    def test_split_nodes_delimiter_count(self):
        list_txt = [TextNode("This is text with a `code block` word", TEXT),TextNode("This is text with a `code block` word2", TEXT)]
        expected = [TextNode("This is text with a ",TEXT), TextNode("code block",CODE), TextNode(" word",TEXT), TextNode("This is text with a ",TEXT), TextNode("code block",CODE), TextNode(" word2",TEXT)]
        self.assertListEqual(u.split_nodes_delimiter(list_txt,"`",CODE),expected)

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
            TEXT,
            )]
        expected = [TextNode("This is text with an ", TEXT), TextNode("image", IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), TextNode(" and another ", TEXT), TextNode("second image", IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")]
        converted = u.split_nodes_images(nodes)
        self.assertListEqual(converted,expected)

    def test_split_node_images_no_images(self):
        nodes = [TextNode(
            "This is text with an not image and another not image",
            TEXT,
            )]
        expected = [TextNode("This is text with an not image and another not image", TEXT)]
        self.assertListEqual(u.split_nodes_images(nodes),expected)

    #split_links===============================================================================================================
    def test_split_node_links_eq(self):
        nodes = [TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
            TEXT,
        )]
        expected = [TextNode("This is text with a ", TEXT), TextNode("link", LINK, "https://www.example.com"), TextNode(" and ", TEXT), TextNode("another", LINK, "https://www.example.com/another")]
        self.assertListEqual(u.split_nodes_links(nodes),expected)

    def test_split_node_liks_no_liks(self):
        nodes = [TextNode(
            "This is text with a link and link",
            TEXT,
        )]
        expected = [TextNode("This is text with a link and link", TEXT)]
        self.assertListEqual(u.split_nodes_links(nodes),expected)
    #text_to_textnodes===============================================================================================================
    def test_text_to_textnodes_eq(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        expected = [TextNode("This is ", TEXT), TextNode("text", BOLD), TextNode(" with an ", TEXT), TextNode("italic", ITALIC), TextNode(" word and a ", TEXT), TextNode("code block", CODE), TextNode(" and an ", TEXT), TextNode("image", IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), TextNode(" and a ", TEXT), TextNode("link", LINK, "https://boot.dev")]
        self.assertListEqual(u.text_to_textnodes(text),expected)

    def test_text_to_textnodes_only_text(self):
        text = "Text with no delimeters, images or links"
        expected = [TextNode("Text with no delimeters, images or links", TEXT)]
        self.assertListEqual(u.text_to_textnodes(text),expected)

    #markdown_to_blocks===============================================================================================================
    def test_markdown_to_blocks_eq(self):
        markdown = "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items\n"
        expected = [
            'This is **bolded** paragraph', 
            'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', 
            '* This is a list\n* with items\n'
            ]
        self.assertListEqual(u.markdown_to_blocks(markdown),expected)


if __name__ == "__main__":
    unittest.main()
