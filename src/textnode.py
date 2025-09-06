from enum import Enum
from htmlnode import HTMLNode
from leafnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text_type != other.text_type:
            return False
        if self.text != other.text:
            return False
        if self.url != other.url:
            return False
        return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


# takes old_nodes:list[TextNode], dilimiter:string, text_type:TextType
# returns list[TextNode] or raises exception
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        nodes_from_node = []
        text_segments = old_node.text.split(delimiter)
        if len(text_segments) % 2 == 0:
            raise Exception(f"Missing delimiter in {old_node}.")
        for i in range(len(text_segments)):
            text = text_segments[i]
            if text == "":
                continue
            if i % 2 != 0:
                nodes_from_node.append(TextNode(text, text_type, url=None))
            else:
                nodes_from_node.append(TextNode(text, TextType.TEXT))
        result.extend(nodes_from_node)
    return result


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, "href")
        case TextType.IMAGE:
            return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text,})
        case _:
            pass
