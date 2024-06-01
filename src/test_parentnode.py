import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode (unittest.TestCase):

    def test_eq(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ParentNode("p2",[
                LeafNode("i2", "italic text"),
                LeafNode(None, "Normal text2"),
            ],{"test":"props"}),
        ],{"test0":"props0"},
        )
        self.assertEqual(node.to_html(), '<p test0="props0"><b>Bold text</b>Normal text<i>italic text</i>Normal text<p2 test="props"><i2>italic text</i2>Normal text2</p2></p>')

    def test_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
            )
            
    


if __name__ == "__main__":
    unittest.main()
