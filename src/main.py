import os
from textnode import TextNode

def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    copy_dir("test_source", "test_target")
    print(node)

def copy_dir(source, target):
    print(os.listdir("../"))
    



main()




