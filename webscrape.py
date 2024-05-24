import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_SCRAPE_URL")

def scrape_data():
    """
    Get data from table: name, types (up to 2), stats(hp, atk, def, spatk, spdef, speed)
    """
    req = requests.get(BASE_URL)
    soup = BeautifulSoup(req.content, "html.parser")
    search = soup.find("table", class_="tab")
    
    obj_data = []
    if search:    
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

    else:
        print("Table not found.")

    return obj_data
if __name__ == "__main__":
    mon_data = scrape_data()
    for data in mon_data:
        print(data)


#obj_data = scrape_data()
#for name, type1, type2, hp, attack, defense, sp_atk, sp_def, speed in obj_data:
#            print(f"Pokémon: {name}, Types: {type1}, {type2}, Stats: {hp}, {attack}, {defense}, {sp_atk}, {sp_def}, {speed}")
