import unittest

from textnode import TextNode, TextType, split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_bold(self):
        node = TextNode("This is a test of **bold** text.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes, [
                TextNode("This is a test of ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text.", TextType.TEXT),
            ]
        )

    def test_split_italic(self):
        node = TextNode("This is a test of _italic_ text.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes, [
                TextNode("This is a test of ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text.", TextType.TEXT),
            ]
        )

    def test_split_ends(self):
        node = TextNode("`Grovel `inverted code` sudo sandwitch`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes, [
                TextNode("Grovel ", TextType.CODE),
                TextNode("inverted code", TextType.TEXT),
                TextNode(" sudo sandwitch", TextType.CODE),
            ]
        )
