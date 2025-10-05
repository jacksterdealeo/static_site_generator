def extract_title(markdown: str) -> str :
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line.removeprefix("# ")

    raise Exception("Title not found")