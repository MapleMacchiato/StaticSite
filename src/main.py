import os
import shutil
from pathlib import Path
from textnode import TextNode
from markdown_blocks import markdown_to_html_node
def main():
    target_dir, source_dir = "public", "static"
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.mkdir(target_dir)
    copy_dir(source_dir, target_dir)
    
    #from_path = "content/index.md"
    template_path = "template.html"
    #dest_path = "public/index.html"
    #generate_page(from_path, template_path, dest_path)
    from_dir = "content"
    dest_dir = "public"
    generate_pages_recursive(from_dir, template_path, dest_dir)


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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")

main()




