import os
from pathlib import Path
from shutil import copy
import sys

from markdowntoblocks import markdown_to_html_node
from extracttitle import extract_title



def main():
    basepath = r"/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        
    delete("./docs")
    copy_rec("./static", "./docs")
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


def generate_page(basepath, from_path, template_path, dest_path):
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

    if not os.path.exists(dest_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(page)

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