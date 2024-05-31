from textnode import TextNode
from htmlnode import HTMLnode
from leafnode import LeafNode

def main():
    #print(TextNode("This is a text node", "bold", "https://www.boot.dev"))
    #print(HTMLnode(None,None,[],{"href": "https://www.google.com"}))
    print(LeafNode("p", "This is a paragraph of text.").render())
    print(LeafNode("a", "Click me!", {"href": "https://www.google.com"}).render())

main()
