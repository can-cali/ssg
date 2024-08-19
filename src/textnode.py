from htmlnode import LeafNode
from extract_md import (
    extract_markdown_images,
    extract_markdown_links,
)

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href: text_node.url"})
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text type:{text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_nodes = []
        partitions = node.text.split(delimiter)
        if len(partitions) % 2 == 0:
            raise ValueError("Invalid markdown syntax")
        for i in range(len(partitions)):
            if partitions[i] == "":
                continue
            if i % 2 == 0:
                n = TextNode(partitions[i], text_type_text)
                split_nodes.append(n)
            else:
                n = TextNode(partitions[i], text_type)
                split_nodes.append(n)
        new_nodes.extend(split_nodes)
    return new_nodes

#wow this was hard
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        ext = extract_markdown_images(node.text)
        if not ext:
            new_nodes.append(node)
            continue
        current_text = node.text
        for alt, url in ext:
            partitions = current_text.split(f"![{alt}]({url})", 1)
            if partitions[0]:
                n = TextNode(partitions[0], text_type_text)
                new_nodes.append(n)
            n1 = TextNode(alt, text_type_image, url)
            new_nodes.append(n1)
            current_text = partitions[1] if len(partitions) > 1 else ""
        if current_text:
            n = TextNode(current_text, text_type_text)
            new_nodes.append(n)
    return new_nodes
