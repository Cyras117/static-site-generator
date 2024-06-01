from leafnode import LeafNode
from textnode import TextNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(tag=None,value=text_node.text)
        case "bold":
            return LeafNode(tag="b",value=text_node.text)
        case "italic":
            return LeafNode(tag="i",value=text_node.text)
        case "code":
            return LeafNode(tag="code",value=text_node.text)
        case "link":
            return LeafNode(tag="a",value=text_node.text,props={"href":text_node.url})
        case "image":
            return LeafNode(tag="img",value="",props={"src":text_node.url,"alt":"Alt Text"})
        case _:
            raise Exception("Invalid text type")
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    list_text_nodes = list(map(lambda node:node.text.split(delimiter),old_nodes))
    list_text_nodes_new = []
    for l in list_text_nodes:
        for i in range(0,len(l)):
            if i % 2 != 0:
                list_text_nodes_new.append(TextNode(text=l[i],text_type=text_type))
            else:
                list_text_nodes_new.append(TextNode(text=l[i],text_type="text"))
    return list_text_nodes_new