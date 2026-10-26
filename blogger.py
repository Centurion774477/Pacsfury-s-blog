
import markdown
import sys
import os
from datetime import date
import json

# guard clauses
if len(sys.argv) < 2:
    print("No file specified — please specify a file to transpile."); sys.exit(1)

given_file = sys.argv[1]

if not os.path.exists(given_file):
    print(f"File {given_file} does not exist."); sys.exit(1)

if os.path.getsize(given_file) == 0:
    print(f"File {given_file} is empty."); sys.exit(1)

# markdown to html
def get_html(file):
    return markdown.markdown(open(file).read())


# if not being run in the right directory
# if not os.path.exists("blogs.json"):
#     print("Blogger is intended to be ran in the blogs directory."
#           "Please cd into that directory and then rerun Blogger."
#           "\n\nYour new HTML file will still be generated.")
#     print(get_html(given_file)); sys.exit(0)


def get_id_from_title(title):
    return "-".join(title.lower().split())


# gather information
given_title = input("What would you like to title this post?\n~> ")
tags  = input("List the tags you would like to attach, separated by a comma.\n~> ")

date = date.today().strftime('%Y-%m-%d')
post_id = get_id_from_title(given_title)
content = get_html(given_file)
tags = tags.split(",")

post = {
    "id": post_id,
    "title": given_title,
    "date": date,
    "tags": tags,
    content: content
}

print("Post:")
print(post)

# append post to blogs

# read
with open("blogs.json", "r") as f:
    blogs_content = json.load(f)

# append post to the blogs array
blogs_content["blogs"].append(post)

# # write
with open("blogs.json", "w") as f:
    json.dump(blogs_content, f, indent=2)
