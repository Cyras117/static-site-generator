from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self,tag=None,value=None,props={}):
        super().__init__(tag=tag,value=value,props=props)
        if value == None:
            raise ValueError("Invalid Value")

    def render(self):
        if self.tag == None:
            return self.value
        else:
            if len(self.props) <= 0:
                return f'<{self.tag}>{self.value}</{self.tag}>'
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"