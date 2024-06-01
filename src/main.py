from textnode import TextNode
from htmlnode import HTMLnode
from leafnode import LeafNode
from parentnode import ParentNode
from utils import split_nodes_delimiter

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
    #print(node.to_html())

    # print(TextNode("This is a text node", "bold", "https://www.boot.dev"))
    # print(HTMLnode(None,None,[],{"href": "https://www.google.com"}))
    # print(LeafNode("p", "This is a paragraph of text.").render())
    # print(LeafNode("a", "Click me!", {"href": "https://www.google.com"}).render())
    #print(LeafNode.text_node_to_html_node(TextNode("This is a text node", "text", "https://www.boot.dev")).render())

    n = [TextNode("This is text with a `code block` word", "text"),TextNode("This is text with a `code block` word2", "text2")]

    b = split_nodes_delimiter(n,"`","code")

    print(b)

main()
