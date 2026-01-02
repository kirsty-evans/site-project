from htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("parent nodes must have a tag")
        if self.children == None:
            raise ValueError("parent node must have children")
        children_string = ""
        for child in self.children:
            children_string += f"{child.to_html()}"
        return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"