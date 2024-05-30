import unittest

from htmlnode import HTMLnode

class TestHTMLNode (unittest.TestCase):
    def test_eq_props(self):
        props = HTMLnode(a="test0",b="test1",c="test2",d="test3",e="test4")
        self.assertEqual(props.props_to_html(), f' a="test0" b="test1" c="test2" d="test3" e="test4"')
    
    def test_empy_propety(self):
        not_props = HTMLnode("a","dentro tag")
        self.assertIsNotNone(not_props.props)

if __name__ == "__main__":
    unittest.main()
