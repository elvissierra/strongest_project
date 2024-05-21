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
        names = [link.get_text(strip=True) for link in a_tags if "/pokedex-sv/" in link['href'] and link.get_text(strip=True)]

        img_tags = row.find_all("img", src=True)
        types = []
        for img in img_tags:
            src = img['src']
            if "/pokedex-bw/type/" in src:
                type_name = src.split('/')[-1].replace('.gif', '')
                types.append(type_name)
        
        if names:
            obj_data.append((names[0], types))
    
    for name, types in obj_data:
        print(f"Pokémon: {name}, Types: {', '.join(types)}")
else:
    print("Table with class 'tab' not found.")
