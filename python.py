#Autor   : quentin.peridon@hotmail.fr
#Version : 1.2
#Date    : 29/04/2023

# Imports
import requests
import concurrent.futures
import re


def process_auction(auction):
    #        ^
    #        |
    #        +
    #        |
    #        |
    #        |
    #        |
    #        |
    #        A
    #       ===                ________
    #      /EEE\               |______|
    #     //EEE\\              |*(  )*|
    # ___//_____\\_____________|O|  |O|_______
    # Recherche l'objet "Final Destination" pour des enchères légendaires et mythiques à bas prix.
    if auction["bin"] and auction["item_name"].find(item_final_destination) != -1:
        # L'objet "Final Destination" a une enchère initiale de 15M à 22M.
        if auction["tier"] == "LEGENDARY" and auction["item_lore"].find("50,000") != -1 and auction["starting_bid"] < 14999999:
            results.append("Potential 50 000 leg        : " + auction["item_name"] + " at the price of " + str(auction["starting_bid"]))
        elif auction["tier"] == "MYTHIC" and auction["item_lore"].find("50,000") != -1 and auction["starting_bid"] < 28999999:
            results.append("Potential 50 000 mythic     : " + auction["item_name"] + " at the price of " + str(auction["starting_bid"]))
        elif auction["tier"] == "MYTHIC" and auction["item_lore"].find("100,000") != -1 and auction["starting_bid"] < 35000000:
            results.append("Potential 100 000 mythic    : " + auction["item_name"] + " at the price of " + str(auction["starting_bid"]))


    #                    ___......----:'"":--....(\
    #             .-':'"":   :  :  :   :  :  :.(1\.`-.
    #           .'`.  `.  :  :  :   :   : : : : : :  .';
    #          :-`. :   .  : :  `.  :   : :.   : :`.`. a;
    #          : ;-. `-.-._.  :  :   :  ::. .' `. `., =  ;
    #          :-:.` .-. _-.,  :  :  : ::,.'.-' ;-. ,'''"
    #        .'.' ;`. .-' `-.:  :  : : :;.-'.-.'   `-'
    # :.   .'.'.-' .'`-.' -._;..:---'''"~;._.-;
    # :`--'.'  : :'     ;`-.;            :.`.-'`.
    #  `'"`    : :      ;`.;             :=; `.-'`.
    #          : '.    :  ;              :-:   `._-`.
    #           `'"'    `. `.            `--'     `._;
    #                     `'"'
    # Recherche l'objet "Tiger" pour des enchères épiques et légendaires à bas prix.
    elif auction["bin"] and auction["item_name"].find(item_tiger) != -1:
        if auction["tier"] == "EPIC" and auction["item_name"].find("Lvl 100") != -1 and auction["starting_bid"] < 18999999:
            results.append("Tiger epic lvl 100          : " + str(auction["starting_bid"]))
        elif auction["tier"] == "LEGENDARY" and auction["item_name"].find("Lvl 100") != -1 and auction["starting_bid"] < 28000000:
            results.append("Tiger leg lvl 100           : " + str(auction["starting_bid"]))


    #  |\(                          .'  Y '>,
    #   \ \                        / _   _   \
    #    \\\                       )(_) (_)(|}
    #     \\\                      {  4A   } /
    #      \\\                      \uLuJJ/\l
    #       \\\                     |3    p)/
    #        \\\___ __________      /nnm_n//
    #        c7___-__,__-)\,__)(".  \_>-<_/D
    #                   //V     \_"-._.__G G_c__.-__<"/ ( \
    #                          <"-._>__-,G_.___)\   \7\
    #                         ("-.__.| \"<.__.-" )   \ \
    #                         |"-.__"\  |"-.__.-".\   \ \
    #                         ("-.__"". \"-.__.-".|    \_\
    #                         \"-.__""|!|"-.__.-".)     \ \
    #                          "-.__""\_|"-.__.-"./      \ l
    #                           ".__""">G>-.__.-">       .--,_
    # Recherche l'objet "Wither Skeleton" pour des enchères légendaires à bas prix.
    elif auction["bin"] and auction["item_name"].find(item_skeleton) != -1:
        if auction["tier"] == "LEGENDARY" and auction["item_name"].find("Lvl 100") != -1 and auction["starting_bid"] < 9000000:
            results.append("Wither skeleton leg lvl 100 : " + str(auction["starting_bid"]))


    #                      __..--"".          .""--..__             
    #                _..-``       ][\        /[]       ``-.._       
    #            _.-`           __/\ \      / /\__           `-._   
    #         .-`     __..---```    \ \    / /    ```---..__     `-.
    #       .`  _.--``               \ \  / /               ``--._  `.
    #      / .-`                      \ \/ /                      `-. \
    #     /.`                          \/ /                          `.\
    #    |`                            / /\                            `|
    # Recherche l'objet "Reaper Scythe" pour des enchères légendaires à bas prix.
    elif auction["bin"] and auction["item_name"].find(item_reaper) != -1:
        if auction["tier"] == "LEGENDARY" and auction["item_lore"].find("Ultimate Wise V") != -1 and auction["starting_bid"] < 40000000:
            results.append("Reaper Scythe               : " + str(auction["starting_bid"]))


    #            __  _
    #        .-.'  `; `-._  __  _
    #       (_,         .-:'  `; `-._
    #     ,'o"(        (_,           )
    #    (__,-'      ,'o"(            )>
    #       (       (__,-'            )
    #        `-'._.--._(             )
    #           |||  |||`-'._.--._.-'
    #                      |||  |||
    # Recherche l'objet "Sheep" pour des enchères légendaires à bas prix.
    elif auction["bin"] and auction["item_name"].find(item_sheep) != -1:
        if auction["tier"] == "LEGENDARY" and auction["item_name"].find("Lvl 100") != -1 and auction["starting_bid"] < 11500000:
            results.append("Sheep leg lvl 100           : " + str(auction["starting_bid"]))
    
    
    #                  .---.
    #     .--.     ___/     \
    #    /    `.-""   `-,    ;
    #   ;     /     O O  \  /
    #   `.    \          /-'
    #  _  J-.__;      _.'
    # (" /      `.   -=:
    #  `:         `, -=|
    #   |  F\    i, ; -|
    #   |  | |   ||  \_J
    #   mmm! `mmM Mmm'
    # Recherche l'objet "Elephant" pour des enchères légendaires à bas prix.
    elif auction["bin"] and auction["item_name"].find(item_elephant) != -1:
        if auction["tier"] == "LEGENDARY" and auction["item_name"].find("Lvl 100") != -1 and auction["starting_bid"] < 40000000:
            results.append("Elephant leg lvl 100        : " + str(auction["starting_bid"]))


    #                     /\              _
    #                    /  \            / \
    #                   |  _ \          /   \   _
    #                   | / \ \        /     \ / \
    #                   |/   \ \       |      /   \
    #                   /     \ |      | /\  / \   \
    #                  /|      \| ~  ~ |/  \/   \   \
    #          _______/_|_______\(o)(o)/___/\___|_   \
    #         /      /  |       (______)     \  | \   \_
    #        /      /   |      /              \ |  \
    #       /      /    |     /                \|   \
    #      /      /     |    /                  \    \
    #     /     _/      |   /                   |\    \
    #    /             _|  |                    |_\    \_
    #  _/                  |                       \
    #                      |                        \
    #                      |                         \_
    #                     _|                        
    # Recherche l'objet "Tarantula Helmet" pour des enchères mythiques à bas prix.
    elif auction["bin"] and auction["item_name"].find(item_helmet_tar) != -1:
        if auction["tier"] == "MYTHIC" and auction["item_lore"].find("25,000") != -1 and auction["starting_bid"] < 20000000:
            results.append("Potential helmet tarantula  : " + str(auction["starting_bid"]))
        if auction["tier"] == "MYTHIC" and auction["item_lore"].find("50,000") != -1 and auction["starting_bid"] < 30000000:
            results.append("Potential helmet tarantula  : " + str(auction["starting_bid"]))
    pass


# List of all responses from get call
responses = []
# Url of the skyblock auctions
url = f"https://api.hypixel.net/skyblock/auctions"

# Get the number of page in the auctions house
response = requests.get(url)
response_json = response.json()
if response_json.get("success") == False and response_json.get("cause") == "Page not found":
    exit
number_of_page=(response_json.get("totalPages"))

# Loop on all pages of the auction house in order to fill responses[]
for pages in range(0, number_of_page):
    url = f"https://api.hypixel.net/skyblock/auctions?page={pages}"
    response = requests.get(url)
    response_json = response.json()
    if response_json.get("success") == False and response_json.get("cause") == "Page not found":
        break
    responses.append(response_json)

# Crée une liste d'enchères en filtrant les enchères à partir de réponses.
# Si aucune enchère n'est trouvée, renvoie une liste vide.
auctions = [auction for response in responses for auction in response.get("auctions", [])]

# Crée des variables pour les noms d'objets recherchés.
item_final_destination = "Final"
item_shadow_assassin = "Ancient Shadow Assassin"
item_tiger = "Tiger"
item_skeleton = "Wither Skeleton"
item_sheep="Sheep"
item_elephant="Elephant"
item_helmet_tar = "Tarantula Helmet"
item_reaper="Reaper Scythe"

# Créer une liste pour stocker les résultats
results = []

# Parcours chaque enchère pour les objets recherchés.
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Traiter chaque enchère dans un thread séparé
    futures = [executor.submit(process_auction, auction) for auction in auctions]

    # Attendre que tous les threads soient terminés
    for future in concurrent.futures.as_completed(futures):
        # Ignorer les résultats (puisque process_auction ne renvoie rien)
        pass

# On crée une liste des catégories d'objet à rechercher
categories_list = ["Leggings", "Helmet", "Boots", "Chestplate", "Reaper Scythe", "lvl 100"]

# On crée un dictionnaire qui a pour clés les catégories et pour valeurs des listes vides.
categories_results = {category: [] for category in categories_list}

# On parcourt chaque élément de la liste results,
# puis pour chaque catégorie, si la catégorie est présente dans la chaîne de caractères de l'élément,
# on ajoute cet élément à la liste correspondante dans le dictionnaire categories_results.
for result in results:
    for category in categories_list:
        if category in str(result):
            categories_results[category].append(result)

# Affichage des résultats triés par catégorie
for category, results_list in categories_results.items():
    # Affichage de 100 '=' pour un meilleur affichage
    print(f"\n{category}:\n{'='*100}")
    for result in sorted(results_list, key=lambda x: x[-9:]):
        print(f"{result}")