from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(self, tag, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("The tag is missing.")
        if self.children is None or self.children == []:
            raise ValueError("The children are missing.")
        return f"<{self.tag}>{' '.join(map(lambda x: x.to_html(), self.children))}</{self.tag}>"
