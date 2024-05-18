import requests
from bs4 import BeautifulSoup

#extract url
req = requests.get("https://www.serebii.net/scarletviolet/pokemon.shtml")

soup = BeautifulSoup(req.content, "html.parser")

search = soup.find("table", class_="tab")

content = search.find_all("a", href=True)

#base_url = "https://www.serebii.net"
#links = [(link.get_text(strip=True), base_url + link["href"]) for link in content if "/pokemon-sv/" in link["href"]]

names = [link.get_text(strip=True) for link in content if "/pokedex-sv/" in link['href']]
for name in names:
    print(name)

#fetch and parse each mons url
"""
def fetch_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    type_info = soup.find("table", class_="dextable")

    if type_info:
        type_rows = type_info.find_all("a", href= True)
        types = []

        if type_rows:
            type_data = [link.get_text(strip=True) for link in type_rows if "/pokedex-sv/" in link["href"]]

            if type_data:
                types.append(type_data)
        return types
    return []

for name, url in links:
    types = fetch_data[url]
    print(f"{name}: {types}")
    """