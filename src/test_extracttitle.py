import unittest

from extracttitle import extract_title


class TestHTMLNode(unittest.TestCase):
    def test_eq_blank(self):
        text = """# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)"""
        title = "Tolkien Fan Club"
        self.assertEqual(extract_title(text), title)
    
    def test_not_equal(self):
        with self.assertRaises(Exception):
            text = """## Blog posts

    - [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
    - [Why Tom Bombadil Was a Mistake](/blog/tom)
    - [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)"""

            extract_title(text)