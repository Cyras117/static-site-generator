class HTMLnode:
    def __init__(self,tag=None,value=None,children=[],**props):
        self.tag =tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        return f"HMLNode(TAG={self.tag}, VALUE={self.value}, CHILDREN={self.children}, PROPS={self.props}"

    def to_html(self):
        raise NotImplementedError("Not done yet")
    
    def props_to_html(self):
        return f" {" ".join(map(lambda prop:f'{prop}="{self.props[prop]}"' ,self.props))}"