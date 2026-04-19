from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import ParentNode, LeafNode, text_node_to_html_node
from text_to_textnodes import text_to_textnodes

print("file loaded")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            text = block.replace("\n", " ")
            p_node = ParentNode("p", text_to_children(text))
            children.append(p_node)
        
        elif block_type == BlockType.HEADING:
            level = 0
            for char in block:
                if char == "#":
                    level += 1
                else:
                    break
            text = block[level + 1:]
            tag = f"h{level}"
            h_node = ParentNode(tag, text_to_children(text))
            children.append(h_node)
    
        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            stripped_lines = []
            for line in lines:
                stripped_lines.append(line.lstrip(">").strip())
            text = " ".join(stripped_lines)
            q_node = ParentNode("blockquote", text_to_children(text))
            children.append(q_node)
    
        elif block_type == BlockType.UNORDERED_LIST:
            items = block.split("\n")
            li_nodes = []
            for item in items:
                text = item[2:]  # strip the "- "
                li_nodes.append(ParentNode("li", text_to_children(text)))
            ul_node = ParentNode("ul", li_nodes)
            children.append(ul_node)
        
        elif block_type == BlockType.ORDERED_LIST:
            items = block.split("\n")
            li_nodes = []
            for item in items:
                text = item.split(". ", 1)[1]  # split once on ". " and take the part after
                li_nodes.append(ParentNode("li", text_to_children(text)))
            ol_node = ParentNode("ol", li_nodes)
            children.append(ol_node)
            
        elif block_type == BlockType.CODE:
            # strip the leading "```\n" and trailing "```"
            text = block[4:-3]
            code_leaf = LeafNode("code", text)
            pre_node = ParentNode("pre", [code_leaf])
            children.append(pre_node)

    return ParentNode("div", children)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes








if __name__ == "__main__":
    md = """# Heading

This is a **paragraph** with _italic_.

> a quote
> on two lines

- apple
- banana

1. first
2. second

```
raw **code** stays raw
```"""
    node = markdown_to_html_node(md)
    print(node.to_html())
