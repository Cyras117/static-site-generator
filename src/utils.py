from re import findall,search
from text_type import TextType
from block_type import BlockType
from leafnode import LeafNode
from textnode import TextNode
import htmlnode


IMAGE_REGEX = r"!\[(.*?)\]\((.*?)\)"
LINK_REGEX = r"\[(.*?)\]\((.*?)\)"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None,value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b",value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i",value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code",value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a",value=text_node.text,props={"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img",value="",props={"src":text_node.url,"alt":"Alt Text"})
        case _:
            raise Exception("Invalid text type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    list_return = []
    for node in old_nodes:
        s = node.text
        if delimiter in s: 
            if len(delimiter) < 2:
                i = 0
                start = 0
                end = 0
                while i < len(s):
                    if s[i] == delimiter:
                        if i+1 < len(s) and s[i+1] != delimiter and i-1 >= 0 and s[i-1] != delimiter:
                            start = i+1
                            while i+1 < len(s) and s[i+1]!=delimiter:
                                i += 1
                            end = i+1
                            i=end
                            if not (end+1 < len(s) and s[end+1] == delimiter):
                                list_return.append(TextNode(s[:start-1:],TextType.TEXT))
                                list_return.append(TextNode(s[start:end:],text_type))
                    i += 1
                list_return.append(TextNode(s[end+1::],TextType.TEXT))
            else:
                saux = s
                while True:
                    start = saux.find(delimiter)+2
                    end = saux.find(delimiter,start)
                    list_return.append(TextNode(saux[:start-2:],TextType.TEXT))
                    list_return.append(TextNode(saux[start:end:],text_type))
                    if end + 2 < len(saux):
                        saux = saux[end+2::]
                    if saux.find(delimiter) == -1:
                        break
                if end + 2 < len(saux) and len(saux[end+2])>0:
                    list_return.append(TextNode(s[end+2:],TextType.TEXT))
        else:
            list_return.append(node)

    return list_return
                
def extract_markdown_images(text):
    return findall(IMAGE_REGEX,text)

def extract_markdown_links(text):
    return findall(LINK_REGEX,text)

def split_nodes_images(old_nodes):
    list_return = []
    for n in old_nodes:
        auxtext = n.text
        mobject = search(IMAGE_REGEX,auxtext)
        extracted = extract_markdown_images(auxtext)
        if mobject:
            for img in extracted:
                start = mobject.span()[0]
                end = mobject.span()[1]
                list_return.append(TextNode(auxtext[:start:],TextType.TEXT)) 
                list_return.append(TextNode(img[0],TextType.IMAGE,img[1]))
                auxtext = auxtext[end::]
                if search(IMAGE_REGEX,auxtext):
                    mobject = search(IMAGE_REGEX,auxtext)
            if len(auxtext) > 0:
                list_return.append(TextNode(auxtext,TextType.TEXT))
        else:   
            list_return.append(n)
    return list_return

def split_nodes_links(old_nodes):
    list_return = []
    for n in old_nodes:
        auxtext = n.text
        mobject = search(LINK_REGEX,auxtext)
        extracted = extract_markdown_links(auxtext)
        if mobject:
            for img in extracted:
                start = mobject.span()[0]
                end = mobject.span()[1]
                list_return.append(TextNode(auxtext[:start:],TextType.TEXT)) 
                list_return.append(TextNode(img[0],TextType.LINK,img[1]))
                auxtext = auxtext[end::]
                if search(LINK_REGEX,auxtext):
                    mobject = search(LINK_REGEX,auxtext)
            if len(auxtext) > 0:
                list_return.append(TextNode(auxtext,TextType.TEXT))
        else:   
            list_return.append(n)
    return list_return
  
def text_to_textnodes(text):
    text_node = [TextNode(text,TextType.TEXT)]
    text_node_bold = split_nodes_delimiter(old_nodes=text_node,delimiter="**",text_type=TextType.BOLD)
    text_node_italic = split_nodes_delimiter(old_nodes=text_node_bold,delimiter="*",text_type=TextType.ITALIC)
    text_node_code = split_nodes_delimiter(old_nodes=text_node_italic,delimiter="`",text_type=TextType.CODE)
    text_node_images = split_nodes_images(text_node_code)
    text_node_links = split_nodes_links(text_node_images)
    return text_node_links 


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks_return = []
    for block in blocks:
        block_apend = ""
        block_lines = block.split("\n")
        for line in block_lines:
            l = line.lstrip(" ").rstrip(" ")
            if len(l)<=0:
                continue
            block_apend = block_apend + "\n"+l
        blocks_return.append(block_apend)
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
        if line[0] != '-' or line[0] != '*':
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
    #TODO: check if there is block with more than 1 quote
    block_text = block.replace("```","")
    return htmlnode.HTMLnode(tag="blockquote",value=block)

def markdown_to_html_node(markdown):
    mainnode = htmlnode.HTMLnode(tag="div")

    for block in markdown_to_blocks(markdown):
        if block_to_block_type(block) == BlockType.quote:
            mainnode.children.append(quote_block_to_html_qute(block))
    
