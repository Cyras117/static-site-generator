import unittest

from leafnode import LeafNode
from textnode import TextNode

class TestLeafNode (unittest.TestCase):
    def test_eq_props(self):
        props = LeafNode(value="p",props={"a":"test0","b":"test1","c":"test2","d":"test3","e":"test4"})
        self.assertEqual(props.props_to_html(), f' a="test0" b="test1" c="test2" d="test3" e="test4"')
    
    def test_empy_propety(self):
        not_props = LeafNode("a","dentro tag")
        self.assertEqual(not_props.props,{})
    
    def test_Value_None(self):
        with self.assertRaises(ValueError):
            LeafNode(value=None,props={"a":"test0","b":"test1","c":"test2","d":"test3","e":"test4"})
    
    def test_render_tag_None(self):
        val = "Tag is None"
        tag_none = LeafNode(value=val,props={"a":"test0","b":"test1","c":"test2","d":"test3","e":"test4"})
        self.assertEqual(tag_none.render(),val)

    def test_render(self):
        tag_none = LeafNode(tag="render",value="This Render test",props={"a":"test0","b":"test1","c":"test2","d":"test3","e":"test4"})
        self.assertEqual(tag_none.render(),f'<{tag_none.tag}{tag_none.props_to_html()}>{tag_none.value}</{tag_none.tag}>')

    def test_text_node_to_html_node_text_text(self):
        text_node = TextNode("This is a text node", "text", "https://www.boot.dev")
        self.assertEqual(LeafNode.text_node_to_html_node(text_node).render(),f'{text_node.text}')
    
    def test_text_node_to_html_node_text_bold(self):
        text_node = TextNode("This is a bold node", "bold", "https://www.boot.dev")
        self.assertEqual(LeafNode.text_node_to_html_node(text_node).render(),f'<b>{text_node.text}</b>')
    
    def test_text_node_to_html_node_text_italic(self):
        text_node = TextNode("This is a bold node", "italic", "https://www.boot.dev")
        self.assertEqual(LeafNode.text_node_to_html_node(text_node).render(),f'<i>{text_node.text}</i>')

    def test_text_node_to_html_node_text_code(self):
        text_node = TextNode("This is a bold node", "code", "https://www.boot.dev")
        self.assertEqual(LeafNode.text_node_to_html_node(text_node).render(),f'<code>{text_node.text}</code>')
    
    def test_text_node_to_html_node_text_link(self):
        text_node = TextNode("This is a bold node", "link", "https://www.boot.dev")
        self.assertEqual(LeafNode.text_node_to_html_node(text_node).render(),f'<a href="{text_node.url}">{text_node.text}</a>')
    
    def test_text_node_to_html_node_text_image(self):
        text_node = TextNode("", "image", "https://www.boot.dev")
        self.assertEqual(LeafNode.text_node_to_html_node(text_node).render(),f'<img src="{text_node.url}" alt="Alt Text">{text_node.text}</img>')



if __name__ == "__main__":
    unittest.main()
