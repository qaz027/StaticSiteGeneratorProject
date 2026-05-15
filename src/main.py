from textnode import *
from source_to_destination_copy import *

#print("Hello World.")

"""
def main():
    dummy = TextNode('this is some dummy text', TextType.LINK, 'https://boot.dev/sexual_chocolate')
    print(dummy.__repr__())
 """

import os
import shutil

from copystatic import copy_files_recursive


dir_path_static = "./static"
dir_path_public = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)


main()
main()
