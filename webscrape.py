import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.serebii.net/scarletviolet/pokemon.shtml")

soup = BeautifulSoup(req.content, "html.parser")

search = soup.find("table", class_="tab")

content = search.find_all("a", href=True)

names = [link.get_text(strip=True) for link in content if "/pokedex-sv/" in link['href']]

for name in names:
    print(name)