from textnode import TextNode
from htmlnode import HTMLnode
from leafnode import LeafNode
from parentnode import ParentNode
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
   
def main():
    transferFiles(os.getcwd()+"/static",os.getcwd()+"/public",True)

main()
