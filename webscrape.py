import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.serebii.net/scarletviolet/pokemon.shtml")

soup = BeautifulSoup(r.content, "html.parser")

s = soup.find("td", class_="pkmn")
content = s.find_all("a", href=True)

names = [a.get_text(strip=True) for a in content if "Name" in a["href"]]

for name in names:
    print(name)