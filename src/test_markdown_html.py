import unittest
from markdown_html import markdown_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_node(self):
        md = """
# this is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

* This is a list item
* This is another list item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is a heading</h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is a list item</li><li>This is another list item</li></ul></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and more items

1. This is an ordered list
2. with items
3. and more items
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and more items</li></ul><ol><li>This is an ordered list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

## this is an h2

### this is an h3

#### this is an h4

##### this is an h5

###### this is an h6
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><h2>this is an h2</h2><h3>this is an h3</h3><h4>this is an h4</h4><h5>this is an h5</h5><h6>this is an h6</h6></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote
> block
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote></div>",
        )

    def test_code(self):
        md = """
```
This is a code block
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is a code block\n</code></pre></div>",
        )


if __name__ == "__main__":
    unittest.main()
