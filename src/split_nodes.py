from extract_markdown import (
    extract_markdown_images,
    extract_markdown_links,
)
from textnode import TextNode, TextType

#node = TextNode("Just some plain text with no images.", TextType.TEXT)
#split_nodes_image([node])

#node = [ TextNode("Hello ![cat](http://cat.png) world", TextType.TEXT) ]

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        #extracted = [("cat", "http://cat.png")]    
        extracted = extract_markdown_images(old_node.text)
        
        if extracted == []:
            new_nodes.append(old_node)
            continue
        
        original_text = old_node.text
        for image in extracted:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            original_text = sections[1]
        
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
        
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
   
        extracted = extract_markdown_links(old_node.text)
        
        if extracted == []:
            new_nodes.append(old_node)
            continue
        
        original_text = old_node.text
        for link in extracted:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
        
    return new_nodes



"""
Input:
A list of TextNode objects, e.g.:

[TextNode("Hello ![cat](http://cat.png) world", TextType.TEXT)]

Algorithm:

    Loop over each node
    If node is not TextType.TEXT → add it unchanged, skip
    Extract images from node's text
    If no images → add node unchanged, skip
    Set original_text = old_node.text
    Loop over each image:
        Split original_text on the image markdown
        If text before image is not empty → add as TEXT node
        Add the image as an IMAGE node
        Set original_text = text after the image
    If any original_text is left over → add as TEXT node
    Return new_nodes

Output:
A list of TextNode objects, e.g.:

[
    TextNode("Hello ", TextType.TEXT),
    TextNode("cat", TextType.IMAGE, "http://cat.png"),
    TextNode(" world", TextType.TEXT),
]
    
"""   