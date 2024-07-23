import unittest
import utils as u
class TestUils (unittest.TestCase):
    #text_to_textnodes===============================================================================================================
    # def test_text_to_textnodes_eq(self):
    #     text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
    #     expected = [TextNode("This is ", TEXT), TextNode("text", BOLD), TextNode(" with an ", TEXT), TextNode("italic", ITALIC), TextNode(" word and a ", TEXT), TextNode("code block", CODE), TextNode(" and an ", TEXT), TextNode("image", IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), TextNode(" and a ", TEXT), TextNode("link", LINK, "https://boot.dev")]
    #     self.assertListEqual(u.text_to_textnodes(text),expected)

    # def test_text_to_textnodes_only_text(self):
    #     text = "Text with no delimeters, images or links"
    #     expected = [TextNode("Text with no delimeters, images or links", TEXT)]
    #     self.assertListEqual(u.text_to_textnodes(text),expected)

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
