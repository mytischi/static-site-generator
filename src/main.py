from textnode import TextNode, TextType
from markdown_to_html import markdown_to_html_node
import os, shutil, sys

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        
    if os.path.exists("./docs"):
        #print("statc dir exists")
        shutil.rmtree("./docs")
        print("deleted old docs dir")
    os.mkdir("./docs")
    print("added new docs dir")
     
    copy_files("./static", "./docs")


    #generate_page("content/index.md", "template.html", "docs/index.html")
    generate_pages_recursive("content", "template.html", "docs", basepath)
    
    return print("Done!")


def copy_files(path, destination):

    list_dir = os.listdir(path)
    print("checking static dir")
    
    for i in list_dir:
        i_dir = os.path.join(path, i)
        if not os.path.isfile(i_dir):
            new_destination = os.path.join(destination, i)
            print(f"going in {i_dir}")
            os.mkdir(new_destination)
            copy_files(i_dir, new_destination)
        else:
            shutil.copy(i_dir, destination)
   
    return print(f"copy in {destination} complited")



def extract_title(markdown):
    strings = markdown.split("\n")
    for string in strings:
        if string.startswith("# "):
            return string.replace("# ", "")
    

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path, "r")
    template_file = open(template_path, "r")
    file_string = from_file.read()
    template_string = template_file.read()
    title = extract_title(file_string)
    file_html = markdown_to_html_node(file_string).to_html()
    new_html = template_string.replace("{{ Title }}", title)
    new_html = new_html.replace("{{ Content }}", file_html)
    new_html = new_html.replace('href="/', f'href="{basepath}')
    new_html = new_html.replace('src="/', f'src="{basepath}')
    from_file.close()
    template_file.close()

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(new_html)
    
    return 

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    items = os.listdir(dir_path_content)

    for item in items:
        content_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)

        if os.path.isdir(content_path):
            os.mkdir(dest_path)
            generate_pages_recursive(content_path, template_path, dest_path, basepath)
        elif item.endswith(".md"):
            # what should the destination filename be?
            # should it stay ".md", or become ".html"?
            html_name = item.replace(".md", ".html")
            html_dest_path = os.path.join(dest_dir_path, html_name)
            generate_page(content_path, template_path, html_dest_path, basepath)
    return





main()

#print(extract_title("# some shit to test"))
