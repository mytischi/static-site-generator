from textnode import TextType, TextNode

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None: 
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}>{children_html}</{self.tag}>"


def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception ("Not a correct TextType")
    
    if text_node.text_type == TextType.TEXT:
        new_html = LeafNode(None, text_node.text)
        return new_html
    if text_node.text_type == TextType.BOLD:
        new_html = LeafNode("b", text_node.text)
        return new_html
    if text_node.text_type == TextType.ITALIC:
        new_html = LeafNode("i", text_node.text)
        return new_html
    if text_node.text_type == TextType.LINK:
        new_html = LeafNode("a", text_node.text, {"href": text_node.url})
        return new_html
    if text_node.text_type == TextType.IMAGE:
        new_html = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        return new_html
    if text_node.text_type == TextType.CODE:
        new_html = LeafNode("code", text_node.text)
        return new_html
