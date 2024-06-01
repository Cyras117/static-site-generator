from htmlnode import HTMLnode

class LeafNode(HTMLnode):
    def __init__(self,tag=None,value=None,props={}):
        super().__init__(tag=tag,value=value,props=props)
        if value == None:
            raise ValueError("Invalid Value")

    def render(self):
        if self.tag == None:
            return self.value
        else:
            if len(self.props) <= 0:
                return f'<{self.tag}>{self.value}<{self.tag}/>'
            return f'<{self.tag}{self.props_to_html()}>{self.value}<{self.tag}/>'

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