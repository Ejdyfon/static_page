

import os
import shutil
import sys
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def copystatic():
    if os.path.exists("./docs"):
        shutil.rmtree('./docs')
    shutil.copytree('./static', './docs')

def crawler_content(dir_path, basepath):
    dir = os.listdir(dir_path)
    for dir in dir:
        entry_path = os.path.join(dir_path,dir)
        if os.path.isfile(entry_path):
            dest = dir_path.replace(dir_path_content, ".")
            dest_pathhh = os.path.join(dir_path_public,dest)
            generate_page(
                entry_path,
                template_path,
                os.path.join(dest_pathhh, "index.html"), basepath
            )
        else:
            crawler_content(entry_path, basepath)



def main():
    if len(sys.argv) > 0:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    print("Copying static files to public directory...")
    copystatic()
    print("Starting crawler...")
    crawler_content(dir_path_content, basepath)

    #print("Generating page...")
    #generate_page(
    #    os.path.join(dir_path_content, "index.md"),
    #    template_path,
    #    os.path.join(dir_path_public, "index.html"),
    #)


main()

