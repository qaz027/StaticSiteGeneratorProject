from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered_list"

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

def block_to_block_type(block):
    '''
    Create a block_to_block_type function that takes a single block of markdown text as input and returns the BlockType representing the type of block it is. You can assume all leading and trailing whitespace were already stripped (we did that in a previous lesson).
        Headings start with 1-6 # characters, followed by a space and then the heading text.
        Multiline Code blocks must start with 3 backticks and a newline, then end with 3 backticks.
        Every line in a quote block must start with a "greater-than" character: > followed by the quote text. A space after > is allowed but not required.
        Every line in an unordered list block must start with a - character, followed by a space.
        Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
        If none of the above conditions are met, the block is a normal paragraph.
    
    :param blocks: blocks are the stripped string of markdown text
    '''
    lines = block.split("\n")

    if block.startswith(("#", "##", "###", "####", "#####", "######")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("-"):
        for line in lines:
            if not line.startswith("-"):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i+=1
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

    # returns blocktype

    