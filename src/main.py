from textnode import TextNode, TextType
from markdown_to_html import markdown_to_html_node
import os, shutil

def main():
    if os.path.exists("./static"):
        #print("statc dir exists")
        shutil.rmtree("./public")
        print("deleted old public dir")
    os.mkdir("./public")
    print("added new public dir")
     
    copy_files("./static", "./public")


    generate_page("content/index.md", "template.html", "public/index.html")
    
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
    

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path, "r")
    template_file = open(template_path, "r")
    file_string = from_file.read()
    template_string = template_file.read()
    title = extract_title(file_string)
    file_html = markdown_to_html_node(file_string).to_html()
    new_html = template_string.replace("{{ Title }}", title)
    new_html = new_html.replace("{{ Content }}", file_html)
    
    from_file.close()
    template_file.close()

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(new_html)
    
    return 





main()

#print(extract_title("# some shit to test"))
