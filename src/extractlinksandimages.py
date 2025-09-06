import re


# takes text:string
# returns list[tuple(alt_text:string, URL:string)]
def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


# takes text:string
# returns list[tuple(anchor_text:string, URL:string)]
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
