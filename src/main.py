import os
from pathlib import Path
from shutil import copy
import sys

from markdowntoblocks import markdown_to_html_node
from extracttitle import extract_title


dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    print(f"BASE PATH: {basepath}")
        
    print("Deleting public directory...")
    delete(dir_path_public)

    print("Copying static files to public directory...")
    copy_rec(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(
        basepath,
        "./content/",
        "./template.html",
        "./docs/"
        )

    '''
    node = TextNode(
        "Hello, Larl.",
        TextType.LINK,
        "https://docs.python.org/3/library/enum.html"
    )
    print(node)
    '''


def delete(folder_path: str):
    if not os.path.exists(folder_path):
        return
    for filename in os.listdir(folder_path):
        print(f"Deleting: {filename}")
        file_path = os.path.join(folder_path, filename)  
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)  
            elif os.path.isdir(file_path):
                delete(file_path)
                os.rmdir(file_path)  
        except Exception as e:  
            print(f"Error deleting {file_path}: {e}")
    print("Deletion done")


def copy_rec(src: str, dst: str) -> None:
    src = os.path.abspath(src)
    dst = os.path.abspath(dst)
    if not os.path.exists(dst):
        os.mkdir(dst)
    for path in os.listdir(src):
        full_path = os.path.join(src, path)
        if os.path.isfile(full_path):
            copy(full_path, dst)
        elif os.path.isdir(full_path):
            copy_rec(full_path, os.path.join(dst, path))
    print(f"Copying to {dst} done")


def copy_directory_tree(src: str, dst: str) -> None:
    src = os.path.abspath(src)
    dst = os.path.abspath(dst)
    if not os.path.exists(dst):
        os.mkdir(dst)
    for path in os.listdir(src):
        full_path = os.path.join(src, path)
        if os.path.isdir(full_path):
            copy_rec(full_path, os.path.join(dst, path))
    print(f"Copying directories to {dst} done")


def read_text_file(path):
    with open(path, "r") as f:
        return f.read()


def generate_page(basepath: str, from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = read_text_file(from_path)
    page = read_text_file(template_path)
    page_HTMLnode = markdown_to_html_node(markdown)
    content = page_HTMLnode.to_html()
    title = extract_title(markdown)
    page = page.replace('{{ Title }}', title)
    page = page.replace('{{ Content }}', content)
    page = page.replace('"href="/', 'href="' + basepath)
    page = page.replace('src="/', 'src="' + basepath)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(page)
    to_file.close()


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


if __name__ == "__main__":
    main()