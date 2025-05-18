from textnode import TextNode
from textnode import TextType


def main():
    node = TextNode("Hello, Larl.", TextType.LINK.value,
                    "https://docs.python.org/3/library/enum.html")
    print(node)


if __name__ == "__main__":
    main()
