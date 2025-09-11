import re
from enum import Enum
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
# returns list[TextNode]
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


# takes text:string
# returns list[TextNode]
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    delimiters = [
        ("**", TextType.BOLD),
        ("_", TextType.ITALIC),
        ("`", TextType.CODE)
    ]
    for d in delimiters:
        nodes = (split_nodes_delimiter(nodes, d[0], d[1]))

    return nodes


# takes text_node:TextNode
# returns LeafNode
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
            return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
        case _:
            pass


# takes text:string
# returns list[tuple(alt_text:string, URL:string)]
def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


# takes text:string
# returns list[tuple(anchor_text:string, URL:string)]
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


# takes list[TextNode]
# returns list[TextNode]
def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        remaining_text = old_node.text
        images = extract_markdown_images(remaining_text)
        if len(images) == 0:
            result.append(old_node)
            continue
        nodes_from_node = []
        for image in images:
            image_alt, image_link = image
            text_segments = remaining_text.split(f"![{image_alt}]({image_link})", 1)
            if len(text_segments[0]) != 0:
                nodes_from_node.append(TextNode(text_segments[0], TextType.TEXT))
            nodes_from_node.append(TextNode(image_alt, TextType.IMAGE, url=image_link))
            remaining_text = text_segments[1]
        if len(remaining_text) != 0:
            nodes_from_node.append(TextNode(remaining_text, TextType.TEXT))
        result.extend(nodes_from_node)
    return result


# takes list[TextNode]
# returns list[TextNode]
def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        remaining_text = old_node.text
        links = extract_markdown_links(remaining_text)
        if len(links) == 0:
            result.append(old_node)
            continue
        nodes_from_node = []
        for link in links:
            link_text, link_url = link
            text_segments = remaining_text.split(f"[{link_text}]({link_url})", 1)
            if len(text_segments[0]) != 0:
                nodes_from_node.append(TextNode(text_segments[0], TextType.TEXT))
            nodes_from_node.append(TextNode(link_text, TextType.LINK, url=link_url))
            remaining_text = text_segments[1]
        if len(remaining_text) != 0:
            nodes_from_node.append(TextNode(remaining_text, TextType.TEXT))
        result.extend(nodes_from_node)
    return result
