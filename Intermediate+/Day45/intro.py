from bs4 import BeautifulSoup

with open("./Day45/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.title,"\n")
# print(soup.prettify)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags,"\n")

for tag in all_anchor_tags:
    print(tag.get("href"))

heading  = soup.find_all("h1",id = "name")
print("\n",heading)

h3 = soup.find_all("h3",  class_= "heading")
print("\n",h3)