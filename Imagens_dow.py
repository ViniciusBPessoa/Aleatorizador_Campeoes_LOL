import os
import requests
import json

url_champ = "https://ddragon.leagueoflegends.com/cdn/10.22.1/data/pt_BR/champion.json"

response_champ = requests.get(url_champ)
data_champ = json.loads(response_champ.text)
champions = data_champ["data"]

if not os.path.exists("champion_thumbnails"):
    os.mkdir("champion_thumbnails")

for champion in champions:
    champion_name = champions[champion]["id"]
    champion_img_url = f"http://ddragon.leagueoflegends.com/cdn/10.22.1/img/champion/{champion_name}.png"
    response_img = requests.get(champion_img_url)
    open(f"champion_thumbnails/{champion_name}.png", "wb").write(response_img.content)

print("Download de miniaturas de campeões concluído!")

