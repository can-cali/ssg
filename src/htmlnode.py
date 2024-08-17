class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f"HTML Object with tag={self.tag}, value={self.value}, childrens={self.children} and props={self.props}"

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a non-empty value")
        if self.tag is None:
            return self.value
        else:
            if self.props is not None and self.props:
                return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"