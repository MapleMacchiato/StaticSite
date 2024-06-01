import os
import shutil
from textnode import TextNode

def main():
    target_dir, source_dir = "public", "static"
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.mkdir(target_dir)
    copy_dir(source_dir, target_dir)

def copy_dir(source, target):
    source_items = os.listdir(source)
    target_items = os.listdir(target)
    for item in source_items:
        source_path = os.path.join(source, item)
        target_path = os.path.join(target, item)
        if os.path.isfile(source_path):
            print(f"Copying {source_path} to {target_path}")
            shutil.copy(source_path, target_path)
            continue
        os.mkdir(target_path)
        copy_dir(source_path, target_path)
main()




