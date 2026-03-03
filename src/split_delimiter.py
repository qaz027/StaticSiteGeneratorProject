from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    '''
    It takes a list of "old nodes", a delimiter, and a text type. 
    It should return a new list of nodes, where any "text" type nodes in the input list are (potentially) 
    split into multiple nodes based on the syntax. For example, given the following input:

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
    # split the old_nodes by the delimiter
    #nodes = old_nodes.split(delimiter)
    
    for old_node in old_nodes:
        if text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        nodes = []
        sections = old_node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown syntax - need closing formatting for section")
        
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                nodes.append(TextNode(sections[i], text_type))
        
        new_nodes.extend(nodes)

    
    
    return new_nodes
