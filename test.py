import random
import requests
import json

def select(n_players = 5, funk = False):
    url_champ = "https://ddragon.leagueoflegends.com/cdn/10.22.1/data/pt_BR/champion.json"
    url_spells = "https://ddragon.leagueoflegends.com/cdn/10.22.1/data/pt_BR/summoner.json"

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

    posi_list = ["Top", "Adc", "Sup", "Mid"]
    shuffle_list = random.sample(posi_list, len(posi_list))
    j = 0

    champion_random = random.sample(champion_list,n_players)
    print(champion_random)
    posi = random.randint(0, n_players)

    for i in range(len(champion_random)):
        
        spell_random = random.sample(spell_list, 2)

        if i==posi:
            if "Golpear" not in spell_random:
                spell_random[1] = "Golpear"
            print("Posição: Jg, Champion: ", champion_random[i])
            print("Summoner Spells: ", spell_random)
        else:
            pos = shuffle_list[j]
            print(f"Posição: {pos}, Champion: ", champion_random[i])
            print("Summoner Spells: ", spell_random)

            j = j + 1
        print("-"*50)

select(4)
