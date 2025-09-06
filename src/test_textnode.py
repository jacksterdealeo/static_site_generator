import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
