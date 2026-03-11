from enum import Enum

class BlockType(Enum):
    PARAGRAPH: "paragraph"
    HEADING: "heading"
    CODE: "code"
    QUOTE: "quote"
    UNORDERED_LIST: "unordered list"
    ORDERED_LIST: "ordered_list"

def markdown_to_blocks(markdown):
    blocks = []
    #print(f"Markdown block: {markdown}")

    md_list = markdown.split("\n\n")
    #md_list = list(filter(None,md_list))

    for block in md_list:
        if block =="":
            continue
        block = block.strip()
        blocks.append(block)
    
    return blocks

def block_to_blockType(blocks):
    pass