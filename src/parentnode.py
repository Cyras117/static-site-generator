from htmlnode import HTMLnode

class ParentNode(HTMLnode):
    def __init__(self, tag, children, props={}):
        super().__init__(tag=tag, children=children, props=props)
        if tag == None:
            raise ValueError("Invalid value for Tag")
        if children == None or len(children) <= 0:
            raise ValueError("Invalid value for children")
    
    def to_html(self):
        str_return = ""

        for node in self.children:
            if node.children == None or node.children == []:
                str_return += node.render()
            else:
                str_return += node.to_html()
        
        if self.tag != None:
            str_return = f'<{self.tag}{self.props_to_html()}>{str_return}'
            return f'{str_return}</{self.tag}>'
        return str_return