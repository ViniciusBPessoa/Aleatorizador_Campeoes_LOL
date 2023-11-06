import os
import requests
import json

url_version = "https://ddragon.leagueoflegends.com/api/versions.json"
response_version = requests.get(url_version)
latest_version = json.loads(response_version.text)[0]  # Obtém a versão mais recente

url_champ = f"https://ddragon.leagueoflegends.com/cdn/{latest_version}/data/pt_BR/champion.json"

response_champ = requests.get(url_champ)
data_champ = json.loads(response_champ.text)
champions = data_champ["data"]

# Verificar se a pasta 'champion_thumbnails' existe. Se não, cria a pasta.
if not os.path.exists("champion_thumbnails"):
    os.mkdir("champion_thumbnails")
else:
    # Excluir imagens antigas antes de baixar as novas
    old_files = os.listdir("champion_thumbnails")
    for file in old_files:
        os.remove(os.path.join("champion_thumbnails", file))

# Baixar as splash arts atualizadas dos campeões para a pasta 'champion_thumbnails'
for champion in champions:
    champion_name = champions[champion]["id"]
    champion_img_url = f"http://ddragon.leagueoflegends.com/cdn/{latest_version}/img/champion/{champion_name}.png"
    response_img = requests.get(champion_img_url)
    open(f"champion_thumbnails/{champion_name}.png", "wb").write(response_img.content)

print("Download de miniaturas de campeões concluído!")
