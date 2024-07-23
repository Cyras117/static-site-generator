from block_type import BlockType
from htmlnode import HTMLNode
  
# def text_to_textnodes(text):
#     text_node = [TextNode(text,TEXT)]
#     text_node_bold = split_nodes_delimiter(old_nodes=text_node,delimiter="**",text_type=BOLD)
#     text_node_italic = split_nodes_delimiter(old_nodes=text_node_bold,delimiter="*",text_type=ITALIC)
#     text_node_code = split_nodes_delimiter(old_nodes=text_node_italic,delimiter="`",text_type=CODE)
#     text_node_images = split_nodes_images(text_node_code)
#     text_node_links = split_nodes_links(text_node_images)
#     return text_node_links 


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks_return = []
    for block in blocks:
        block_apend = []
        block_lines = block.split("\n")
        if len(block_lines) > 1:
            for line in block_lines:
                l = line.lstrip(" ").rstrip(" ")
                block_apend.append(l)
            blocks_return.append("\n".join(block_apend))
        elif len(block_lines) > 0:
            blocks_return.append(block_lines[0])
    return blocks_return

    
def block_to_block_type(block_markdown):
    block_lines = block_markdown.split('\n')

    for line in block_lines:
        index = 0
        while len(line) >= 0 and index < len(line) and index < 6:
            if index +1 < len(line) and block_markdown[index] == '#' and block_markdown[index+1] == ' ':
                return BlockType.heading
            index += 1

    if block_markdown[:3:] == '```' and block_markdown[:-3:] == '```':
        return BlockType.code
    
    quotes = True
    for line in block_lines:
        if line[0] != '>':
            quotes = False
    if quotes:
        return BlockType.quote

    ulist = True
    for line in block_lines:
        if line[:2:] != '- ' or line[:2:] != '* ':
            ulist = False
    if ulist:
        return BlockType.unordered_list
    
    olist = True
    for l in range(0,len(block_lines)):
        line = block_lines[l]
        if len(line) >= 3 and line[0].isnumeric() and line[1] == '.' and line[0] == f'{l+1}' and line[2] == ' ':
            olist = True
        else:
            olist = False
    if olist:
        return BlockType.ordered_list

    return BlockType.paragraph
def quote_block_to_html_qute(block):
    block_lines = block.split("\n")
    block_text = ""
    if len(block_lines) <= 1:
        block_text = block.replace(">","")
    else:
        for line in block_lines:
            block_text = block_text + " " + line
    return HTMLNode(tag="blockquote",value=block_text)

def unorderedlist_block_to_html_ul(block):
    nodeul = HTMLNode(tag="ul")
    block_lines = block.split("\n")
    for line in block_lines:
        line_text = line.replace("* ","").replace("- ","")
        linode = HTMLNode(tag="li",value=line_text)
        nodeul.children.append(linode)
    return nodeul

def orderedlist_block_to_html_ol(block):
    nodeol = HTMLNode(tag="ol")
    block_lines = block.split("\n")
    for line in block_lines:
        line_text = line[3::]
        linode = HTMLNode(tag="li",value=line_text)
        nodeol.children.append(linode)
    return nodeol

def code_block_to_html_code(block):
    codenode = HTMLNode(tag="code")
    block_text = block.replace("```","")
    codenode.children.append(HTMLNode(tag="pre",value=block_text))
    return codenode

def head_block_to_html_head(block):
    block_lines = block.split("\n")
    listnodes = []
    for line in block_lines:
        if line.count("#") == 1:
            listnodes.append(HTMLNode(tag="h1",value=line.strip("#")))
        if line.count("#") == 2:
            listnodes.append(HTMLNode(tag="h2",value=line.strip("#")))
        if line.count("#") == 3:
            listnodes.append(HTMLNode(tag="h3",value=line.strip("#")))
        if line.count("#") == 4:
            listnodes.append(HTMLNode(tag="h4",value=line.strip("#")))
        if line.count("#") == 5:
            listnodes.append(HTMLNode(tag="h5",value=line.strip("#")))
        if line.count("#") == 6:
            listnodes.append(HTMLNode(tag="h6",value=line.strip("#")))
    return listnodes

def markdown_to_html_node(markdown):
    mainnode = HTMLNode(tag="div")
    for block in markdown_to_blocks(markdown):
        block_type = block_to_block_type(block)
        if block_type == BlockType.quote:
            mainnode.children.append(quote_block_to_html_qute(block))
        if block_type == BlockType.unordered_list:
            ulnode = unorderedlist_block_to_html_ul(block)
            mainnode.children.append(ulnode)
        if block_type == BlockType.ordered_list:
            orderedlist_block_to_html_ol(block)
            ##mainnode.children.append(olnode)
        if block_type == BlockType.code:
            mainnode.children.append(code_block_to_html_code(block))
        if block_type == BlockType.heading:
            mainnode.children = mainnode.children + head_block_to_html_head(block)
        if block_type == BlockType.paragraph:
            mainnode.children.append(HTMLNode(tag="p",value=block))
    return mainnode    

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.count("#") == 1 and line.startswith("#"):
            return line.replace("# ","")