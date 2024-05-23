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
        name = [link.get_text(strip=True) for link in a_tags if "/pokedex-sv/" in link['href'] and link.get_text(strip=True)]

        img_tags = row.find_all("img", src=True)
        types = []
        for img in img_tags:
            src = img['src']
            if "/pokedex-bw/type/" in src:
                type_name = src.split('/')[-1].replace('.gif', '')
                types.append(type_name)

        stat_tags = row.find_all("td", class_="fooinfo")
        stats = []
        for stat in stat_tags:
            text = stat.get_text(strip=True)
            if text.isdigit():
                stats.append(int(text))

        if name and len(stats) == 6:
            type1 = types[0] if len(types) > 0 else None
            type2 = types[1] if len(types) > 1 else None
            obj_data.append((name[0], type1, type2, *stats))
    
    for name, type1, type2, hp, attack, defense, sp_atk, sp_def, speed in obj_data:
        print(f"Pokémon: {name}, Types: {type1}, {type2}, Stats: {hp}, {attack}, {defense}, {sp_atk}, {sp_def}, {speed}")
else:
    print("Table not found.")
