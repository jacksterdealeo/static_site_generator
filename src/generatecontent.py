from markdowntoblocks import markdown_to_html_node
from extracttitle import extract_title
import os
from pathlib import Path



def read_text_file(path):
    with open(path, "r") as f:
        text = f.read()
        f.close()
        return text

def generate_page(basepath, from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = read_text_file(from_path)
    page = read_text_file(template_path)
    page_HTMLnode = markdown_to_html_node(markdown)
    content = page_HTMLnode.to_html()
    title = extract_title(markdown)
    page = page.replace('{{ Title }}', title)
    page = page.replace('{{ Content }}', content)
    page = page.replace('href="/', 'href="' + basepath)
    page = page.replace('src="/', 'src="' + basepath)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(page)
    to_file.close()
    print(f"Page generated to {dest_path}")

def generate_pages_recursive(basepath, dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for filename in os.listdir(dir_path_content):
        full_src = os.path.join(dir_path_content, filename)
        full_dest = os.path.join(dest_dir_path, filename)
        if os.path.isfile(full_src):
            full_dest = os.path.join(dest_dir_path, Path(full_dest).stem + ".html")
            print(f"Generating {full_src} -> {full_dest}")
            generate_page(basepath, full_src, template_path, full_dest)
        elif os.path.isdir(full_src):
            print(f"Making {full_src} -> {full_dest}")
            generate_pages_recursive(basepath, full_src, template_path, full_dest)
    print(f"Copying directories to {dest_dir_path} done")
