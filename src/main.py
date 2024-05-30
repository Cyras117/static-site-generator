from textnode import TextNode
from htmlnode import HTMLnode

def main():
    #print(TextNode("This is a text node", "bold", "https://www.boot.dev"))
    print(HTMLnode(a="test0",b="test1",c="test2",d="test3",e="test4").props_to_html())
main()