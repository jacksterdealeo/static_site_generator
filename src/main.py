import os
from pathlib import Path
from shutil import copy
import sys

from generatecontent import generate_pages_recursive


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
    generate_pages_recursive(basepath, dir_path_content, template_path, dir_path_public)


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
        text = f.read()
        f.close()
        return text
    

if __name__ == "__main__":
    main()