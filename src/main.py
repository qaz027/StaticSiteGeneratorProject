from textnode import *

#print("Hello World.")

def main():
    dummy = TextNode('this is some dummy text', TextType.LINK, 'https://boot.dev/sexual_chocolate')
    print(dummy.__repr__())


main()
