import unittest

from htmlnode import LeafNode

class TestLeafNode (unittest.TestCase):
    pass
    # def test_eq_props(self):
    #     props = LeafNode(value="p",props={"a":"test0","b":"test1","c":"test2","d":"test3","e":"test4"})
    #     self.assertEqual(props.props_to_html(), f' a="test0" b="test1" c="test2" d="test3" e="test4"')
    
    # def test_empy_propety(self):
    #     not_props = LeafNode("a","dentro tag")
    #     self.assertEqual(not_props.props,{})
    
    # def test_Value_None(self):
    #     with self.assertRaises(ValueError):
    #         LeafNode(value=None,props={"a":"test0","b":"test1","c":"test2","d":"test3","e":"test4"})
    
    # def test_render_tag_None(self):
    #     val = "Tag is None"
    #     tag_none = LeafNode(value=val,props={"a":"test0","b":"test1","c":"test2","d":"test3","e":"test4"})
    #     self.assertEqual(tag_none.render(),val)

    # def test_render(self):
    #     tag_none = LeafNode(tag="render",value="This Render test",props={"a":"test0","b":"test1","c":"test2","d":"test3","e":"test4"})
    #     self.assertEqual(tag_none.render(),f'<{tag_none.tag}{tag_none.props_to_html()}>{tag_none.value}</{tag_none.tag}>')

# if __name__ == "__main__":
#     unittest.main()
