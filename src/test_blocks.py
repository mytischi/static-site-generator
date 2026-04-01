import unittest
from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestBlock(unittest.TestCase):
    
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

    def test_block_to_block_type(self):
        md = "# Heading"
        block_type = block_to_block_type(md) 
        self.assertEqual(block_type, BlockType.HEADING)

if __name__ == "__main__":
    unittest.main()
