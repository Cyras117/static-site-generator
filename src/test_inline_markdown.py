import unittest
from inline_markdown import(
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link
)
from textnode import (
    TextNode,
    BOLD,
    IMAGE,
    ITALIC,
    CODE,
    LINK,
    TEXT
)

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TEXT)
        new_nodes = split_nodes_delimiter([node], "**", BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TEXT),
                TextNode("bolded", BOLD),
                TextNode(" word", TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TEXT),
                TextNode("bolded", BOLD),
                TextNode(" word and ", TEXT),
                TextNode("another", BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TEXT),
                TextNode("bolded word", BOLD),
                TextNode(" and ", TEXT),
                TextNode("another", BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TEXT)
        new_nodes = split_nodes_delimiter([node], "*", ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TEXT),
                TextNode("italic", ITALIC),
                TextNode(" word", TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TEXT)
        new_nodes = split_nodes_delimiter([node], "**", BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", BOLD),
                TextNode(" and ", TEXT),
                TextNode("italic", ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TEXT)
        new_nodes = split_nodes_delimiter([node], "`", CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TEXT),
                TextNode("code block", CODE),
                TextNode(" word", TEXT),
            ],
            new_nodes,
        )
    #extract_markdown_images===============================================================================================================
    def test_extract_markdown_images_count(self):
        txt = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        expected = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        self.assertCountEqual(extract_markdown_images(txt),expected)
    
    def test_extract_markdown_images_eq(self):
        txt = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        expected = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        self.assertListEqual(extract_markdown_images(txt),expected)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    #extract_markdown_links===============================================================================================================
    def test_extract_markdown_links_count(self):
        txt = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expected = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        self.assertCountEqual(extract_markdown_links(txt),expected)
    
    def test_extract_markdown_links_eq(self):
        txt = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expected = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        self.assertListEqual(extract_markdown_links(txt),expected)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )


    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TEXT),
                TextNode("image", IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.com/image.png)",
            TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", IMAGE, "https://www.example.com/image.png"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TEXT),
                TextNode("image", IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TEXT),
                TextNode(
                    "second image", IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TEXT),
                TextNode("link", LINK, "https://boot.dev"),
                TextNode(" and ", TEXT),
                TextNode("another link", LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TEXT),
            ],
            new_nodes,
        )

    def test_split_node_images_eq(self):
        self.maxDiff = None
        nodes = [TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            TEXT,
            )]
        expected = [TextNode("This is text with an ", TEXT), TextNode("image", IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), TextNode(" and another ", TEXT), TextNode("second image", IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")]
        converted = split_nodes_image(nodes)
        self.assertListEqual(converted,expected)

    def test_split_node_images_no_images(self):
        nodes = [TextNode(
            "This is text with an not image and another not image",
            TEXT,
            )]
        expected = [TextNode("This is text with an not image and another not image", TEXT)]
        self.assertListEqual(split_nodes_image(nodes),expected)

    def test_split_node_links_eq(self):
        nodes = [TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
            TEXT,
        )]
        expected = [TextNode("This is text with a ", TEXT), TextNode("link", LINK, "https://www.example.com"), TextNode(" and ", TEXT), TextNode("another", LINK, "https://www.example.com/another")]
        self.assertListEqual(split_nodes_link(nodes),expected)

    def test_split_node_liks_no_liks(self):
        nodes = [TextNode(
            "This is text with a link and link",
            TEXT,
        )]
        expected = [TextNode("This is text with a link and link", TEXT)]
        self.assertListEqual(split_nodes_link(nodes),expected)

if __name__ == "__main__":
    unittest.main()