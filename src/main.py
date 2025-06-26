

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

def main():
    print("Copying static files to public directory...")
    copystatic()

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )


main()

