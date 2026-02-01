from enum import Enum
from textnode import *
import os
import shutil
from generate_page import generate_page

path_public = "public"
path_static = "static"

def copy_static_to_public(path_public, path_static, is_root = True):
    # delete all contents of public directory
    if is_root:
        if os.path.exists(path_public):
            shutil.rmtree(path_public)
        os.mkdir(path_public)

    # copy all files and from static to public, keep structure
    for item in os.listdir(path_static):
        source_item_path = os.path.join(path_static, item)
        dest_item_path = os.path.join(path_public, item)

        if os.path.isdir(source_item_path):
            os.mkdir(dest_item_path)
            copy_static_to_public(dest_item_path, source_item_path, is_root=False)
        else:
            shutil.copy(source_item_path, dest_item_path)




def main():
    copy_static_to_public(path_public, path_static)
    generate_page("content/index.md", "template.html", "public/index.html")
    
main()
