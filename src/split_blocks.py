

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