from textnode import TextNode
from htmlnode import HTMLnode
from leafnode import LeafNode
from parentnode import ParentNode

def main():
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
    print(node.to_html())

    print(TextNode("This is a text node", "bold", "https://www.boot.dev"))
    print(HTMLnode(None,None,[],{"href": "https://www.google.com"}))
    print(LeafNode("p", "This is a paragraph of text.").render())
    print(LeafNode("a", "Click me!", {"href": "https://www.google.com"}).render())

main()
