from markdown_blocks import *
from htmlnode import *
from inline_markdown import *
from textnode import *
from parentnode import *

def text_to_children(text):
    '''
    Converts a text string into a list of HTMLNode children representing the inline markdown structure.
    For example, the text "This is **bold** text" would be converted into:
    [HTMLNode(tag=None, value="This is "), HTMLNode(tag="strong", value="bold"), HTMLNode(tag=None, value=" text")]
    '''
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        if text_node.text_type == TextType.TEXT:
            children.append(LeafNode(None, text_node.text))
        elif text_node.text_type == TextType.BOLD:
            children.append(LeafNode("b", text_node.text))
        elif text_node.text_type == TextType.ITALIC:
            children.append(LeafNode("i", text_node.text))
        elif text_node.text_type == TextType.CODE:
            children.append(LeafNode("code", text_node.text))
    return children

def markdown_to_html_node(markdown):
    '''
    Converts a full markdown document into a single parent HTMLNode.
    The parent HTMLNode will have children representing each block in the markdown document.
    '''
    blocks = markdown_to_blocks(markdown)
    node_list = []
    for block in blocks:
        block_type = block_to_block_type(block)
        print(f"block type for {block} is {block_type}")
        if block_type == BlockType.PARAGRAPH:
            lines = block.split("\n")
            stripped = [line.strip() for line in lines if line.strip() != ""]
            para_text = " ".join(stripped)
            if para_text == "":          # skip empty paragraph blocks
                continue
            children = text_to_children(para_text)
            node = ParentNode("p", children)
            node_list.append(node)
            continue
        if block_type == BlockType.HEADING:
            heading_level = 0
            for ch in block:
                if ch == "#":
                    heading_level += 1
                else:
                    break
            if heading_level < 1:
                heading_level = 1
            if heading_level > 6:
                heading_level = 6
            tag = f"h{heading_level}"
            content = block[heading_level:].strip()
            children = text_to_children(content)
            node = ParentNode(tag, children)
            node_list.append(node)
            continue
        if block_type == BlockType.CODE:
            lines = block.split("\n")
            inner_lines = lines[1:-1]              # drop ``` lines
            stripped = [line.lstrip() for line in inner_lines]
            code_text = "\n".join(stripped) + "\n"

            inner = LeafNode("code", code_text)
            outer = ParentNode("pre", [inner])
            node_list.append(outer)
            continue  # Code blocks do not have inline children
        if block_type == BlockType.QUOTE:
            children = text_to_children(block)
            node = ParentNode("blockquote", children)
            node_list.append(node)
            continue
        if block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            li_nodes = []
            for line in lines:
                line = line.strip()
                if line == "":
                    continue
                item_text = line[2:]
                children = text_to_children(item_text)
                li_node = ParentNode("li", children)
                li_nodes.append(li_node)
            ul_node = ParentNode("ul", li_nodes)
            node_list.append(ul_node)
            continue
        if block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            li_nodes = []
            for line in lines:
                line = line.strip()
                if line == "":
                    continue
                # find the first ". " and remove the leading number + ". "
                # e.g. "12. foo" -> find index of "."
                dot_index = line.find(".")
                if dot_index == -1:
                    continue  # or handle error; but skip malformed line
                item_text = line[dot_index+2:]  # skip ". " as well
                children = text_to_children(item_text)
                li_node = ParentNode("li", children)
                li_nodes.append(li_node)

            ol_node = ParentNode("ol", li_nodes)
            node_list.append(ol_node)
            continue
    parent_node = ParentNode(tag="div", children=node_list)
    return parent_node
    

        
    '''
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            node = HTMLNode(tag="h1")
        if block_type == BlockType.PARAGRAPH:
            node = HTMLNode(tag="p")
        if block_type == BlockType.CODE:
            node = HTMLNode(tag="pre")
        if block_type == BlockType.QUOTE:
            node = HTMLNode(tag="blockquote")
        if block_type == BlockType.UNORDERED_LIST:
            node = HTMLNode(tag="ul")
        if block_type == BlockType.ORDERED_LIST:
            node = HTMLNode(tag="ol")

    '''

    return blocks
        

mk = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
# print(markdown_to_html_node(mk))

