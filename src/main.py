

import os
import shutil
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def copystatic():
    if os.path.exists("./public"):
        shutil.rmtree('./public')
    shutil.copytree('./static', './public')

def crawler_content(dir_path):
    dir = os.listdir(dir_path)
    for dir in dir:
        entry_path = os.path.join(dir_path,dir)
        if os.path.isfile(entry_path):
            dest = dir_path.replace(dir_path_content, ".")
            dest_pathhh = os.path.join(dir_path_public,dest)
            generate_page(
                entry_path,
                template_path,
                os.path.join(dest_pathhh, "index.html"),
            )
        else:
            crawler_content(entry_path)



def main():
    print("Copying static files to public directory...")
    copystatic()
    print("Starting crawler...")
    crawler_content(dir_path_content)

    #print("Generating page...")
    #generate_page(
    #    os.path.join(dir_path_content, "index.md"),
    #    template_path,
    #    os.path.join(dir_path_public, "index.html"),
    #)


main()

