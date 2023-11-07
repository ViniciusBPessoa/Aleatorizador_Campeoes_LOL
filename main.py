import random
import requests
import json
import os
from PIL import Image

url_champ = "https://ddragon.leagueoflegends.com/cdn/10.22.1/data/pt_BR/champion.json"
url_spells = "https://ddragon.leagueoflegends.com/cdn/10.22.1/data/pt_BR/summoner.json"
champion_thumbnails_folder = "champion_thumbnails"



def display_image_in_terminal(champion_name):
    champion_image_path = os.path.join(champion_thumbnails_folder, f"{champion_name}.png")

    if os.path.exists(champion_image_path):
        with open(champion_image_path, 'rb') as f:
            img = Image.open(f)
            img.show()

def select(n_players=5):
    shuffle_list = random.sample(posi_list, len(posi_list))
    champion_random = random.sample(champion_list, n_players)

    for i in range(len(champion_random)):
        spell_random = random.sample(spell_list, 2)

        champion_name = champion_random[i]
        display_image_in_terminal(champion_name)

        if shuffle_list[i] == "Jg":
            if "Golpear" not in spell_random:
                spell_random[1] = "Golpear"
            print(f"Posição: Jg, Champion: {champion_name}")
            print(f"Sua build será: {random.choice(list_bilds)}")
        else:
            pos = shuffle_list[i]
            print(f"Posição: {pos}, Champion: {champion_name}")
            print(f"Sua build será: {random.choice(list_bilds)}")

        print("Summoner Spells:", spell_random)
        print("-" * 50)

    input("Pressione Enter para continuar...")  # Aguarda a entrada do usuário antes de fechar a imagem

response_champ = requests.get(url_champ)
data_champ = json.loads(response_champ.text)
champions = data_champ["data"]

response_spells = requests.get(url_spells)
data_spells = json.loads(response_spells.text)
summoner_spells = data_spells["data"]

champion_list = []
for champion in champions:
    champion_list.append(champions[champion]["name"])

spell_list = []
for spell in summoner_spells:
    spell_list.append(summoner_spells[spell]["name"])

pops = ['Ao Rei!', 'Arremesso de Poro', 'Marca', 'Marca']
for i in pops:
    spell_list.remove(i)
    
posi_list = ["Top", "Adc", "Sup", "Mid", "Jg"]

list_bilds = ["ATT_SPD", "Letalidade", "OFF tank", "Tank", "AP"]


if __name__ == "__main__":

    while True:
        n_veces = int(input("Quantos players: "))

        if n_veces == 0:
            break
        elif n_veces == "":
            continue
        if 1 <= n_veces <= 5:
            select(n_veces)
        else:
            print("Valor errado, valor deve estar entre 1 e 5!")
