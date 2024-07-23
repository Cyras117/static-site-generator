from textnode import (
    TextNode,
    IMAGE,
    TEXT
)
from inline_markdown import(
    split_nodes_image,
    split_nodes_link
)
from htmlnode import (
    HTMLNode,
    LeafNode
)
import utils as u
import os,shutil

def transferFiles(src,dst ,clear_folder = False):
    if clear_folder:
        shutil.rmtree(dst)
        os.mkdir(dst)
    
    for item in os.listdir(src):
        item_path = os.path.join("/",src,item)
        if os.path.isfile(item_path):
            shutil.copy(item_path,dst)
        if os.path.isdir(item_path):
            os.mkdir(os.path.join("/",dst,item))
            transferFiles(os.path.join("/",src,item),os.path.join("/",dst,item))
        print(item_path)

def generate_page(from_path, template_path, dest_path):
    mdstring = ""
    htmlstring = ""
    print(f"\nGenerating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path,'r') as mdfile:
        mdstring = mdfile.read()
        
    with open(template_path,'r') as htmlfile:
        htmlstring = htmlfile.read()

    mainnode = u.markdown_to_html_node(mdstring)
    print(mainnode)





def main():
    #transferFiles(os.getcwd()+"/static",os.getcwd()+"/public",True)
    # wd = os.getcwd()
    # generate_page(f'{wd}/content/index.md',f'{wd}/template.html','')
    node = TextNode(
            "![image](https://www.example.com/image.png)",
            TEXT,
        )
    new_nodes = split_nodes_image([node])
    TextNode("image", IMAGE, "https://www.example.com/image.png")
    print(new_nodes)

main()
