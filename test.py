import random
import requests
import json

url_champ = "https://ddragon.leagueoflegends.com/cdn/10.22.1/data/pt_BR/champion.json"
url_spells = "https://ddragon.leagueoflegends.com/cdn/10.22.1/data/pt_BR/summoner.json"

def select(n_players = 5, funk = False):

    shuffle_list = random.sample(posi_list, len(posi_list))

    champion_random = random.sample(champion_list,n_players)

    for i in range(len(champion_random)):
        
        spell_random = random.sample(spell_list, 2)

        if shuffle_list[i] == "Jg":
            if "Golpear" not in spell_random:
                spell_random[1] = "Golpear"
            print("Posição: Jg, Champion: ", champion_random[i])
            print("Summoner Spells: ", spell_random)
        else:
            pos = shuffle_list[i]
            print(f"Posição: {pos}, Champion: ", champion_random[i])
            print("Summoner Spells: ", spell_random)

        print("-"*50)

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

if __name__ == "__main__":

    while True:
        n_veses = int(input("Quantos players: "))

        if n_veses == 0:
            break
        elif n_veses == "":
            continue
        if n_veses <= 5 and n_veses >= 1:
            select(n_veses)
        else:
            print("Valor errado, valor deve estar entre 1 e 6!")
