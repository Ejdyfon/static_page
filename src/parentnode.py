from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("All parent must have tags")
        
        if not self.children:
            raise ValueError("All parent must have children")

        ret = f"<{self.tag}>"
        for child in self.children:
            ret += child.to_html()
        ret += f"</{self.tag}>"

        return ret