from enum import Enum


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for i in blocks:
        i = i.strip()
        new_blocks.append(i)
    new_blocks = [x for x in new_blocks if x != ""]
    return new_blocks


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"




def block_to_block_type(block):
    if block.startswith(("# ","## ","### ","#### ","##### ","###### ")):
        return BlockType.HEADING

    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    splited_block = block.split("\n")
    if all(i.startswith(">") for i in splited_block):
        return BlockType.QUOTE

    if all(i.startswith("- ") for i in splited_block):
        return BlockType.UNORDERED_LIST

    if all(line.startswith(f"{i+1}. ") for i, line in enumerate(splited_block)):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH