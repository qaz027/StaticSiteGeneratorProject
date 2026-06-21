import os
import shutil
import sys

from copystatic import copy_files_recursive
from textnode import *
from source_to_destination_copy import *
from gencontent import generate_page
from gencontent import generate_pages_recursive

#print("Hello World.")

"""
def main():
    dummy = TextNode('this is some dummy text', TextType.LINK, 'https://boot.dev/sexual_chocolate')
    print(dummy.__repr__())
 """




dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"


def main():
    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)


main()
