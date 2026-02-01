import os
from markdown_html import markdown_to_html_node
from extract_title import extract_title


# generate page from content/index.md using template.html
# and write to public/index.html

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # read markdown file and store contents
    with open(from_path, "r") as f:
        markdown = f.read()
    # read the template file and store contents
    with open(template_path, "r") as f:
        template = f.read()

    # convert markdowm to html string

    html_string = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown)

    # replace {{ Content }} and {{ Title }} in template with html string and title

    page_string = template.replace("{{ Content }}", html_string)
    page_string = page_string.replace("{{ Title }}", title)
    
    # write the new HTML page to dest_path
    # dest_path is public/index.html

    dest_dir_name = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir_name):
           os.makedirs(dest_dir_name)

    with open(dest_path, "w") as f:
        f.write(page_string)
        


    