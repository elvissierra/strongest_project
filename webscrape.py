import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.serebii.net/scarletviolet/pokemon.shtml")
soup = BeautifulSoup(req.content, "html.parser")
search = soup.find("table", class_="tab")
#iterate through each <tr> tag
    #iterate through each <a> tag
        #if tag.get_text(strip=True) and pattern "/pokemon-sv/"
        #if pattern "/pokemon-bw/type/"

if search:
    obj_data = []
    rows = search.find_all("tr")

    for row in rows:
        a_tags = row.find_all("a", href=True)
        names = [link.get_text(strip=True) for link in a_tags if "/pokedex-sv/" in link['href']]

        img_tags = row.find_all("img", src=True)
        types = [img["src"].split("/")[-1].replace(".gif", "") for img in img_tags if "/pokemon-bw/type/" in img["src"]]

        print(names, types)