from enum import Enum
import re


def markdown_to_blocks(markdown: str) -> list[str]:
    result = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        block = block.strip("\n ")
        if block == "":
            continue
        result.append(block)
    return result


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown: str) -> BlockType:
    if re.match(r"(#){1,6}( )", markdown) is not None:
        return BlockType.HEADING
    if re.match(r"(`){3}", markdown) is not None and re.search(r"((`){3}$)", markdown) is not None:
        return BlockType.CODE
    if re.fullmatch(r"(?m)^>.*(?:\n>.*)*\n?$", markdown) is not None:
        return BlockType.QUOTE
    if re.fullmatch(r"(?m)^(- ).*(?:\n(- ).*)*\n?$", markdown) is not None:
        return BlockType.UNORDERED_LIST

    is_ordered_list = True
    count = 1
    for line in markdown.split("\n"):
        if line.startswith(f"{count}. "):
            count += 1
        else:
            is_ordered_list = False
            break
    if is_ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
