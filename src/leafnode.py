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
                return f'<{self.tag}>{self.value}</{self.tag}>'
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'