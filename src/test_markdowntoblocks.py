import unittest

from markdowntoblocks import markdown_to_blocks, block_to_block_type, BlockType


class TestLeafNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_blank(self):
        md = ""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )

    def test_block_to_block_type_heading(self):
        md = """#### TEST
qwqweqdas asdaw"""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.HEADING
        )

    def test_block_to_block_type_code(self):
        md = """```sfvsdfrgf !$#%^@#$)()
dfsfs
sa@SADAW$43fqaw```"""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.CODE
        )

    def test_block_to_block_type_quote(self):
        md = """>GEORGE WAS IN A WELL."""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.QUOTE
        )

    def test_block_to_block_type_unordered_list(self):
        md = """- sfdwerfsdf
- sdfwsfef
- dgfdgrs"""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.UNORDERED_LIST
        )

    def test_block_to_block_type_ordered_list(self):
        md = """1. sfdwerfsdf
2. sdfwsfef
3. dgfdgrs"""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.ORDERED_LIST
        )

    def test_block_to_block_type_ordered_list_broken1(self):
        md = """1. sfdwerfsdf
2. sdfwsfef
4. dgfd"""
        block_type = block_to_block_type(md)
        self.assertNotEqual(
            block_type,
            BlockType.ORDERED_LIST
        )
