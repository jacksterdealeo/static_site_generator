import unittest

from markdowntoblocks import (
    markdown_to_html_node,
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
)

class TestMarkdownToHTML(unittest.TestCase):
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

    # Below are tests from Boot.dev solution files:
    def test_markdown_to_blocks_solution(self):
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

    def test_markdown_to_blocks_newlines_solution(self):
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

    def test_block_to_block_types_solution(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph_solution(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs_solution(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists_solution(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings_solution(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote_solution(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code_solution(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


if __name__ == "__main__":
    unittest.main()

