from re import findall,split,sub,search

from leafnode import LeafNode
from textnode import TextNode


IMAGE_REGEX = r"!\[(.*?)\]\((.*?)\)"
LINK_REGEX = r"\[(.*?)\]\((.*?)\)"

#TODO chang it to ifs
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(tag=None,value=text_node.text)
        case "bold":
            return LeafNode(tag="b",value=text_node.text)
        case "italic":
            return LeafNode(tag="i",value=text_node.text)
        case "code":
            return LeafNode(tag="code",value=text_node.text)
        case "link":
            return LeafNode(tag="a",value=text_node.text,props={"href":text_node.url})
        case "image":
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
                                list_return.append(TextNode(s[:start-1:],"text"))
                                list_return.append(TextNode(s[start:end:],text_type))
                    i += 1
                list_return.append(TextNode(s[end+1::],"text"))
            else:
                saux = s
                while True:
                    start = saux.find(delimiter)+2
                    end = saux.find(delimiter,start)
                    list_return.append(TextNode(saux[:start-2:],"text"))
                    list_return.append(TextNode(saux[start:end:],text_type))
                    if end + 2 < len(saux):
                        saux = saux[end+2::]
                    if saux.find(delimiter) == -1:
                        break
                if end + 2 < len(saux) and len(saux[end+2])>0:
                    list_return.append(TextNode(s[end+2:],"text"))
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
                list_return.append(TextNode(auxtext[:start:],"text")) 
                list_return.append(TextNode(img[0],"image",img[1]))
                auxtext = auxtext[end::]
                if search(IMAGE_REGEX,auxtext):
                    mobject = search(IMAGE_REGEX,auxtext)
            if len(auxtext) > 0:
                list_return.append(TextNode(auxtext,"text"))
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
                list_return.append(TextNode(auxtext[:start:],"text")) 
                list_return.append(TextNode(img[0],"link",img[1]))
                auxtext = auxtext[end::]
                if search(LINK_REGEX,auxtext):
                    mobject = search(LINK_REGEX,auxtext)
            if len(auxtext) > 0:
                list_return.append(TextNode(auxtext,"text"))
        else:   
            list_return.append(n)
    return list_return
  
def text_to_textnodes(text):
    text_node = [TextNode(text,"text")]
    text_node_bold = split_nodes_delimiter(old_nodes=text_node,delimiter="**",text_type="bold")
    text_node_italic = split_nodes_delimiter(old_nodes=text_node_bold,delimiter="*",text_type="italic")
    text_node_code = split_nodes_delimiter(old_nodes=text_node_italic,delimiter="`",text_type="code")
    text_node_images = split_nodes_images(text_node_code)
    text_node_links = split_nodes_links(text_node_images)


    return text_node_links