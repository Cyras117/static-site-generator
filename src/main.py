from textnode import TextNode
from htmlnode import HTMLnode
from leafnode import LeafNode
from parentnode import ParentNode
from utils import split_nodes_delimiter,extract_markdown_images,extract_markdown_links,split_nodes_images,split_nodes_links,text_to_textnodes

def main():
    # node = ParentNode(
    # "p",
    # [
    #     LeafNode("b", "Bold text"),
    #     LeafNode(None, "Normal text"),
    #     LeafNode("i", "italic text"),
    #     LeafNode(None, "Normal text"),
    #     ParentNode("p2",[
    #         LeafNode("i2", "italic text"),
    #         LeafNode(None, "Normal text2"),
    #     ],{"test":"props"}),
    # ],{"test0":"props0"},
    # )
    # print(node.to_html())
    # n = [TextNode("This is text with a `code block` word", "text"),TextNode("This is text with a `code block` word2", "text2")]
    # b = split_nodes_delimiter(n,"`","code")

    # print(TextNode("This is a text node", "bold", "https://www.boot.dev"))
    # print(HTMLnode(None,None,[],{"href": "https://www.google.com"}))
    # print(LeafNode("p", "This is a paragraph of text.").render())
    # print(LeafNode("a", "Click me!", {"href": "https://www.google.com"}).render())
    # print(LeafNode.text_node_to_html_node(TextNode("This is a text node", "text", "https://www.boot.dev")).render())
    #print(extract_markdown_images("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"))
    #print(extract_markdown_links("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"))
    # tn = TextNode(
    #     "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    #     "text",
    # )
    # tn2 = TextNode(
    #     "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
    #     "text",
    # )
    # print(split_nodes_images([tn]))
    # print(extract_markdown_images(tn.text))
    #print(split_nodes_link([tn2]))
    txt = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
    print(text_to_textnodes(txt))
    # list_txt = [TextNode("This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)", "text")]
    # print(split_nodes_delimiter(list_txt,"**","bold"))
    # print(split_nodes_delimiter(list_txt,"*","italic"))

main()
