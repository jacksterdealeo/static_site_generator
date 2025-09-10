import unittest

from extractlinksandimages import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link
)
from textnode import TextNode, TextType


class TestExtractLinksAndImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches
        )

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual(
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")],
            matches
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to a good reminder](https://hasthelargehadroncolliderdestroyedtheworldyet.com)."
        )
        self.assertListEqual(
            [("to a good reminder", "https://hasthelargehadroncolliderdestroyedtheworldyet.com")],
            matches
        )

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")],
            matches
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual([
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            )],
            new_nodes,
        )

    def test_split_images2(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) to test trailing text.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual([
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            TextNode(" to test trailing text.", TextType.TEXT)],
            new_nodes,
        )

    def test_split_images3(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("", TextType.TEXT)], new_nodes)

    def test_split_images_single_image(self):
        node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")], new_nodes)

    def test_split_link(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
            )],
            new_nodes,
        )

    def test_split_link2(self):
        node = TextNode(
            "[LINK](https://i.imgur.com/zjjcJKZ.png) and another [LINK2](https://i.imgur.com/3elNhQu.png) to test trailing text.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("LINK", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "LINK2", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
            TextNode(" to test trailing text.", TextType.TEXT)],
            new_nodes,
        )

    def test_split_link3(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("", TextType.TEXT)], new_nodes,)

    def test_split_link_single_link(self):
        node = TextNode("[LINK](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("LINK", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png")], new_nodes,)
