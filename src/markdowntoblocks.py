from textnode import TextNode
from textnode import text_to_textnodes


# takes markdown:string
# returns list[string]
def markdown_to_blocks(markdown):
    result = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        block = block.strip("\n ")
        if block == "":
            continue
        result.append(block)
    return result
