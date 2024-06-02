import os
import shutil
from textnode import TextNode
from markdown_blocks import markdown_to_html_node
def main():
    target_dir, source_dir = "public", "static"
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.mkdir(target_dir)
    copy_dir(source_dir, target_dir)
    
    from_path = "content/index.md"
    template_path = "template.html"
    dest_path = "public/index.html"
    generate_page(from_path, template_path, dest_path)

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

def extract_title(markdown):
    lines = markdown.split("\n")
    if lines[0].startswith("# "):
        return lines[0].strip("# ")
    else:
        raise Exception("All pages need a single h1 header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    md_text = ""
    with open(from_path, "r") as f:
        md_text = f.read()
    f.close()
    
    title = extract_title(md_text)
    template = ""
    with open(template_path, "r") as f:
        template = f.read()
    f.close()
    
    html_nodes = markdown_to_html_node(md_text)
    html = html_nodes.to_html()
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    
    f = open(dest_path, "w")
    f.write(template)
    f.close()


main()




