from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent must have tags")
        
        if self.children is None:
            raise ValueError("All parent must have children")

        ret = f"<{self.tag}>"
        for child in self.children:
            ret += child.to_html()
        ret += f"</{self.tag}>"

        return ret