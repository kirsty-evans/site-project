from enum import Enum
import re

def markdown_to_blocks(markdown):
    '''
    Takes a raw Markdown string (representing a full document) as input and returns a list of block strings.
    '''
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


class BlockType(Enum):
     
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    '''
    Takes a block markdown string as input and returns its BlockType.
    Assumes all leading/trailing whitespace has been stripped
    '''
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        return BlockType.QUOTE
    if block.startswith("- ") or block.startswith("* "):
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH