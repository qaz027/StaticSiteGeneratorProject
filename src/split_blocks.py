from enum import Enum
from htmlnode import HTMLNode, ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from split_delimiter import text_to_textnodes


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

    
# def markdown_to_html_node(markdown):
#     '''
#     Docstring for markdown_to_html_node
#     converts a full markdown document into a single parent HTMLNode. That one parent HTMLNode should (obviously) contain many child HTMLNode objects representing the nested elements.

#     1. Split the markdown into blocks
#     2. Loop over each block
#         3. Based on the type of block, create a new HTMLNode with the proper data
#         4. Assign the proper child HTMLNode objects to the block node. I created a shared text_to_children(text) function that works for all block types. 
#         It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions (think TextNode -> HTMLNode) 
#         5. The "code" block is a bit of a special case: it should not do any inline markdown parsing of its children. I didn't use my text_to_children function for this block type, 
#         I manually made a TextNode and used text_node_to_html_node.
#     6. Make all the block nodes children under a single parent HTML node (which should just be a div) and return it.

    
#     :param markdown: Description
#     '''

#     blocks = markdown_to_blocks(markdown)
#     for block in blocks:
#         type = block_to_block_type(block=block)
#         # Based on the type of block, create a new HTMLNode with the proper data
#         if type == BlockType.PARAGRAPH:
#             node = HTMLNode("p", )

    
#     pass


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return olist_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        parts = item.split(". ", 1)
        text = parts[1]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

    