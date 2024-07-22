from htmlnode import LeafNode

TEXT = "text"
BOLD = "bold"
ITALIC = "italic"
CODE = "code"
LINK = "link"
IMAGE = "image"

class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self,other):
        return (
            self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url
            ) 

    def __repr__(self):
        if self.url == None:
            return f'TextNode({self.text}, {self.text_type})'    
        return f'TextNode({self.text}, {self.text_type}, {self.url})'

def text_node_to_html_node(text_node):
        if text_node.text_type == TEXT:
            return LeafNode(tag=None,value=text_node.text)
        if text_node.text_type == BOLD:
            return LeafNode(tag="b",value=text_node.text)
        if text_node.text_type == ITALIC:
            return LeafNode(tag="i",value=text_node.text)
        if text_node.text_type == CODE:
            return LeafNode(tag="code",value=text_node.text)
        if text_node.text_type == LINK:
            return LeafNode(tag="a",value=text_node.text,props={"href":text_node.url})
        if text_node.text_type == IMAGE:
            return LeafNode(tag="img",value="",props={"src":text_node.url,"alt":text_node.text})
        raise ValueError(f"Invalid text type: {text_node.text_type}")