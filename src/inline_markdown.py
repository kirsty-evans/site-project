# CH3

import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    '''
splits nodes into multiple nodes if they have multiple text types.

Example input:

node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

new_nodes becomes:

[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
]

'''
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            parts = node.text.split(delimiter)
            # check for closing delimiter: if odd number of parts, we have a closing delimiter
            if len(parts) % 2 == 0:
                raise Exception("Unclosed delimiter in text node")
            for i in range(len(parts)):
                if i % 2 == 0:
                    # even index: normal text
                    new_nodes.append(TextNode(parts[i], TextType.TEXT))
                else:
                    # odd index: special text
                    new_nodes.append(TextNode(parts[i], text_type))
    return new_nodes
    

# testing
# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
            
def extract_markdown_images(text):
    '''
    Takes raw markdown text and returns a list of tuples
    Each tuple contains the alt text and the URL of any markdown images

    '''
    matches = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', text)
    return matches


# TESTING

# text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# print(extract_markdown_images(text))

# Expected output: [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

def extract_markdown_links(text):
    '''
    Extracts markdown links and returns tuples of anchor text and URLs

    '''
    matches = re.findall(r'\[([^\]]*)\]\(([^)]+)\)', text)
    return matches

# TESTING

# text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
# print(extract_markdown_links(text))

# Expected output:  [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

def split_nodes_image(old_nodes):
    '''
    Splits raw markdown text into TextNodes based on images.
    '''
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            current_text = node.text
            images = extract_markdown_images(current_text)
            if not images:
                new_nodes.append(node)
                continue

            for image_text, image_url in images:
                full_md = f"![{image_text}]({image_url})"
                before, after = current_text.split(full_md, 1)
                if before:
                    new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(image_text, TextType.IMAGE, image_url))

                current_text = after

    return new_nodes
            
        


def split_nodes_link(old_nodes):
    '''
    Splits raw markdown text into TextNodes based on images.
    '''
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            current_text = node.text
            links = extract_markdown_links(current_text)
            if not links:
                new_nodes.append(node)
                continue

            for link_text, link_url in links:
                full_md = f"[{link_text}]({link_url})"
                before, after = current_text.split(full_md, 1)
                if before:
                    new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

                current_text = after

    return new_nodes

# TESTING
'''
node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
new_nodes = split_nodes_link([node])
print(new_nodes)

'''
# Expected output:
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]

'''

node = TextNode(
    "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
    TextType.TEXT,
)
new_nodes = split_nodes_image([node])
print(new_nodes)

'''

def text_to_textnodes(text):
    '''
    Converts raw string of markdown-flavoured text into a list of TextNode objects
    '''
    node = TextNode(text, TextType.TEXT)
    new_nodes = [node]
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes



# TESTING

'''

example_input = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

nodes = text_to_textnodes(example_input)
for node in nodes:
    print(node)

    '''
'''
output should be:
[
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
]

'''

def markdown_to_blocks(markdown):
    '''
    Takes a raw Markdown string (representing a full document) as input and returns a list of block strings.
    '''
    blocks = markdown.split("\n\n")
    for block in blocks:
        block = block.strip()
        if block == "":
            blocks.remove(block)
    return blocks

