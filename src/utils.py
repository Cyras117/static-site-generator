from re import findall,sub

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
        i = 0
        start = 0
        end = 0
        while i < len(s):
            if s[i] == delimiter:
                if i+1 < len(s) and s[i+1] != delimiter:
                    start = i+1
                    while i+1 < len(s) and s[i+1]!=delimiter:
                        i += 1
                    end = i+1
                    i+=1
                    list_return.append(TextNode(s[:start-1:],"text"))
                    list_return.append(TextNode(s[start:end:],text_type))
            i += 1
        list_return.append(TextNode(s[end+1::],"text"))
    return list_return
                
def extract_markdown_images(text):
    return findall(IMAGE_REGEX,text)

def extract_markdown_links(text):
    return findall(LINK_REGEX,text)

def split_nodes_images(old_nodes):
    split_word = "_splithere_"
    list_return = []
    for n in old_nodes:
        transform_list = []
        list_img = extract_markdown_images(n.text)
        if len(list_img) > 0:
            text_sub = sub(IMAGE_REGEX,split_word,n.text)
            for i in list_img:
                transform_list.append(text_sub[:text_sub.index(split_word):])
                transform_list.append(i)
                text_sub = text_sub[text_sub.index(split_word)+len(split_word)::]
            list_return += list(map(lambda text:TextNode(text,"text") if not text in list_img else TextNode(text[0],"image",text[1],),transform_list))
        else:
            list_return.append(TextNode(n.text,"text"))
    return list_return

def split_nodes_link(old_nodes):
    split_word = "_splithere_"
    list_return = []
    for n in old_nodes:
        transform_list = []
        list_link = extract_markdown_links(n.text)
        if len(list_link) > 0:    
            text_sub = sub(LINK_REGEX,split_word,n.text)
            for i in list_link:
                transform_list.append(text_sub[:text_sub.index(split_word):])
                transform_list.append(i)
                text_sub = text_sub[text_sub.index(split_word)+len(split_word)::]
            list_return += list(map(lambda text:TextNode(text,"text") if not text in list_link else TextNode(text[0],"link",text[1],),transform_list))
        else:
            list_return.append(TextNode(n.text,"text"))
    return list_return

#TODO:Finish this   
def text_to_textnodes(text):
    text_node = [TextNode(text,"text")]
    text_node_italic = split_nodes_delimiter(old_nodes=text_node,delimiter="*",text_type="italic")
    text_node_bold = split_nodes_delimiter(old_nodes=text_node_italic,delimiter="**",text_type="bold")
    text_node_code = split_nodes_delimiter(old_nodes=text_node_italic,delimiter="`",text_type="code")


    return text_node_italic