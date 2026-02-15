import unittest

from textnode import TextNode, TextType, text_to_textnodes


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.LINK, "boot.dev")
        node2 = TextNode("This is a text node", TextType.LINK, "boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT, "boot.dev")
        node2 = TextNode("This is a different text node",
                         TextType.TEXT, "boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD, "boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT, "boot.dev")
        self.assertNotEqual(node, node2)

    def test_none_link(self):
        node = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(None, node.url)

    def test_text_to_textnodes_default(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )

    def test_text_to_textnodes_bold_only(self):
        text = "**BOLD ME FATHER**"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("BOLD ME FATHER", TextType.BOLD),
            ]
        )

    def test_text_to_textnodes_text_only(self):
        text = "Only normal human words are here."
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("Only normal human words are here.", TextType.TEXT),
            ]
        )

    def test_text_to_textnodes_nothing(self):
        text = ""
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [])


if __name__ == "__main__":
    unittest.main()
