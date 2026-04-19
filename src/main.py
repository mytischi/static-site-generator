from textnode import TextNode, TextType
import os, shutil

def main():
    if os.path.exists("./static"):
        #print("statc dir exists")
        shutil.rmtree("./public")
        print("deleted old public dir")
    os.mkdir("./public")
    print("added new public dir")
     
    copy_files("./static", "./public")
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
    from_file = open("from_path", "r")
    template_file = open("template_path", "r")



main()

#print(extract_title("# some shit to test"))
