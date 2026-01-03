# CH3

import re

from textnode import TextNode, TextType, text_node_to_html_node


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



