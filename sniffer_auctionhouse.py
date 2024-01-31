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
            results.append("    Potential 50 000 leg        : " + auction["item_name"] + " at the price of " + str(auction["starting_bid"]))
        elif auction["tier"] == "MYTHIC" and auction["item_lore"].find("50,000") != -1 and auction["starting_bid"] < 28999999:
            results.append("    Potential 50 000 mythic     : " + auction["item_name"] + " at the price of " + str(auction["starting_bid"]))
        elif auction["tier"] == "MYTHIC" and auction["item_lore"].find("100,000") != -1 and auction["starting_bid"] < 35000000:
            results.append("    Potential 100 000 mythic    : " + auction["item_name"] + " at the price of " + str(auction["starting_bid"]))


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
            results.append("    Tiger epic lvl 100          : " + str(auction["starting_bid"]))
        elif auction["tier"] == "LEGENDARY" and auction["item_name"].find("Lvl 100") != -1 and auction["starting_bid"] < 28000000:
            results.append("    Tiger leg lvl 100           : " + str(auction["starting_bid"]))


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
            results.append("    Wither skeleton leg lvl 100 : " + str(auction["starting_bid"]))


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
        if auction["tier"] == "LEGENDARY" and auction["item_lore"].find("Ultimate Wise V") != -1 and auction["starting_bid"] < 26999999:
            results.append("    Reaper Scythe Leg           : " + str(auction["starting_bid"]))
        elif auction["tier"] == "MYTHIC" and auction["starting_bid"] < 36999999:
            results.append("    Reaper Scythe Mythic        : " + str(auction["starting_bid"]))
        elif auction["starting_bid"] < 25555555:
            results.append("    Reaper Scythe Nothing       : " + str(auction["starting_bid"]))
        

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
            results.append("    Sheep leg lvl 100           : " + str(auction["starting_bid"]))
    
    
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
        if auction["tier"] == "LEGENDARY" and auction["item_name"].find("Lvl 100") != -1 and auction["starting_bid"] < 20000000:
            results.append("    Elephant leg lvl 100        : " + str(auction["starting_bid"]))


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
            results.append("    Potential helmet tarantula  : " + str(auction["starting_bid"]))
        if auction["tier"] == "MYTHIC" and auction["item_lore"].find("50,000") != -1 and auction["starting_bid"] < 30000000:
            results.append("    Potential helmet tarantula  : " + str(auction["starting_bid"]))
 
 
    #      _                    _ 
    #     | |                  | |
    #  ___| |__   _____   _____| |
    # / __| '_ \ / _ \ \ / / _ \ |
    # \__ \ | | | (_) \ V /  __/ |
    # |___/_| |_|\___/ \_/ \___|_|
    # Recherche l'objet "Aspect of the Void" pour des enchères epic à bas prix.
    elif auction["bin"] and auction["item_name"].find(item_aspect_of_the_void) != -1:
        if auction["tier"] == "EPIC" and auction["item_lore"].find("12 blocks") != -1 and auction["starting_bid"] < 750000:
            results.append("    Aspect of the Void          : " + str(auction["starting_bid"]))

    # Recherche l'objet "item_molten" pour des enchères epic à bas prix.
    elif auction["bin"] and auction["item_name"].find(item_molten_necklace) != -1:
        if auction["item_lore"].find("Mana Regeneration") != -1 and auction["item_lore"].find("Mana Pool") != -1:
            match = re.search(r"Mana Regeneration ([IVXLCDM]+)", auction["item_lore"])
            Mana_regen_chiffre = match.group(1)
            match = re.search(r"Mana Pool ([IVXLCDM]+)", auction["item_lore"])
            Mana_pool_chiffre = match.group(1)

            results.append("    Molten Necklace             : " + str(auction["starting_bid"]) + "  Mana regen : " + str(Mana_regen_chiffre) + " Mana Pool : " + str(Mana_pool_chiffre) + " " + auction["tier"])
    elif auction["bin"] and auction["item_name"].find(item_molten_bracelet) != -1:
        if auction["item_lore"].find("Mana Regeneration") != -1 and auction["item_lore"].find("Mana Pool") != -1:
            match = re.search(r"Mana Regeneration ([IVXLCDM]+)", auction["item_lore"])
            Mana_regen_chiffre = match.group(1)
            match = re.search(r"Mana Pool ([IVXLCDM]+)", auction["item_lore"])
            Mana_pool_chiffre = match.group(1)
            
            results.append("    Molten Bracelet             : " + str(auction["starting_bid"]) + "  Mana regen : " + str(Mana_regen_chiffre) + " Mana Pool : " + str(Mana_pool_chiffre) + " " + auction["tier"])
    elif auction["bin"] and auction["item_name"].find(item_molten_cloak) != -1:
        if auction["item_lore"].find("Mana Regeneration") != -1 and auction["item_lore"].find("Mana Pool") != -1:
            match = re.search(r"Mana Regeneration ([IVXLCDM]+)", auction["item_lore"])
            Mana_regen_chiffre = match.group(1)
            match = re.search(r"Mana Pool ([IVXLCDM]+)", auction["item_lore"])
            Mana_pool_chiffre = match.group(1)
            
            results.append("    Molten Cloak                : " + str(auction["starting_bid"]) + "  Mana regen : " + str(Mana_regen_chiffre) + " Mana Pool : " + str(Mana_pool_chiffre) + " " + auction["tier"])

    elif auction["bin"] and auction["item_name"].find(item_aurora_chestplate) != -1:
        if auction["item_lore"].find("Mana Regeneration") != -1 and auction["item_lore"].find("Mana Pool") != -1:
            match = re.search(r"Mana Regeneration ([IVXLCDM]+)", auction["item_lore"])
            Mana_regen_chiffre = match.group(1)
            match = re.search(r"Mana Pool ([IVXLCDM]+)", auction["item_lore"])
            Mana_pool_chiffre = match.group(1)
            
            results.append("    Aurora Chestplate           : " + str(auction["starting_bid"]) + "  Mana regen : " + str(Mana_regen_chiffre) + " Mana Pool : " + str(Mana_pool_chiffre) + " " + auction["tier"])
    elif auction["bin"] and auction["item_name"].find(item_aurora_leggings) != -1:
        if auction["item_lore"].find("Mana Regeneration") != -1 and auction["item_lore"].find("Mana Pool") != -1:
            match = re.search(r"Mana Regeneration ([IVXLCDM]+)", auction["item_lore"])
            Mana_regen_chiffre = match.group(1)
            match = re.search(r"Mana Pool ([IVXLCDM]+)", auction["item_lore"])
            Mana_pool_chiffre = match.group(1)
            
            results.append("    Aurora Leggings             : " + str(auction["starting_bid"]) + "  Mana regen : " + str(Mana_regen_chiffre) + " Mana Pool : " + str(Mana_pool_chiffre) + " " + auction["tier"])
    elif auction["bin"] and auction["item_name"].find(item_aurora_boots) != -1:
        if auction["item_lore"].find("Mana Regeneration") != -1 and auction["item_lore"].find("Mana Pool") != -1:
            match = re.search(r"Mana Regeneration ([IVXLCDM]+)", auction["item_lore"])
            Mana_regen_chiffre = match.group(1)
            match = re.search(r"Mana Pool ([IVXLCDM]+)", auction["item_lore"])
            Mana_pool_chiffre = match.group(1)
            
            results.append("    Aurora Boots                : " + str(auction["starting_bid"]) + "  Mana regen : " + str(Mana_regen_chiffre) + " Mana Pool : " + str(Mana_pool_chiffre) + " " + auction["tier"])

    elif auction["bin"] and auction["item_name"].find(item_contagion_bracelet) != -1:
        if auction["item_lore"].find("Mana Regeneration") != -1 and auction["item_lore"].find("Mana Pool") != -1:
            match = re.search(r"Mana Regeneration ([IVXLCDM]+)", auction["item_lore"])
            Mana_regen_chiffre = match.group(1)
            match = re.search(r"Mana Pool ([IVXLCDM]+)", auction["item_lore"])
            Mana_pool_chiffre = match.group(1)
            
            results.append("    Gauntlet of Contagion       : " + str(auction["starting_bid"]) + "  Mana regen : " + str(Mana_regen_chiffre) + " Mana Pool : " + str(Mana_pool_chiffre) + " " + auction["tier"])


    # Recherche l'objet "item_molten" pour des enchères epic à bas prix.
    if auction["bin"] and auction["item_name"].find(item_molten_necklace) != -1:
        if auction["item_lore"].find("Vitality") != -1 and auction["item_lore"].find("Dominance") != -1:
            match = re.search(r"Vitality ([IVXLCDM]+)", auction["item_lore"])
            vitality_chiffre = match.group(1)
            match = re.search(r"Dominance ([IVXLCDM]+)", auction["item_lore"])
            Dominance_chiffre = match.group(1)

            results.append("    Molten Necklace             : " + str(auction["starting_bid"]) + "  Vitality : " + str(vitality_chiffre) + " Dominance : " + str(Dominance_chiffre) + " " + auction["tier"])
    if auction["bin"] and auction["item_name"].find(item_molten_bracelet) != -1:
        if auction["item_lore"].find("Vitality") != -1 and auction["item_lore"].find("Dominance") != -1:
            match = re.search(r"Vitality ([IVXLCDM]+)", auction["item_lore"])
            vitality_chiffre = match.group(1)
            match = re.search(r"Dominance ([IVXLCDM]+)", auction["item_lore"])
            Dominance_chiffre = match.group(1)
            
            results.append("    Molten Bracelet             : " + str(auction["starting_bid"]) + "  Vitality : " + str(vitality_chiffre) + " Dominance : " + str(Dominance_chiffre) + " " + auction["tier"])
    if auction["bin"] and auction["item_name"].find(item_molten_cloak) != -1:
        if auction["item_lore"].find("Vitality") != -1 and auction["item_lore"].find("Dominance") != -1:
            match = re.search(r"Vitality ([IVXLCDM]+)", auction["item_lore"])
            vitality_chiffre = match.group(1)
            match = re.search(r"Dominance ([IVXLCDM]+)", auction["item_lore"])
            Dominance_chiffre = match.group(1)
            
            results.append("    Molten Cloak                : " + str(auction["starting_bid"]) + "  Vitality : " + str(vitality_chiffre) + " Dominance : " + str(Dominance_chiffre) + " " + auction["tier"])

    if auction["bin"] and auction["item_name"].find(item_aurora_chestplate) != -1:
        if auction["item_lore"].find("Vitality") != -1 and auction["item_lore"].find("Dominance") != -1:
            match = re.search(r"Vitality ([IVXLCDM]+)", auction["item_lore"])
            vitality_chiffre = match.group(1)
            match = re.search(r"Dominance ([IVXLCDM]+)", auction["item_lore"])
            Dominance_chiffre = match.group(1)
            
            results.append("    Aurora Chestplate           : " + str(auction["starting_bid"]) + "  Vitality : " + str(vitality_chiffre) + " Dominance : " + str(Dominance_chiffre) + " " + auction["tier"])
    if auction["bin"] and auction["item_name"].find(item_aurora_leggings) != -1:
        if auction["item_lore"].find("Vitality") != -1 and auction["item_lore"].find("Dominance") != -1:
            match = re.search(r"Vitality ([IVXLCDM]+)", auction["item_lore"])
            vitality_chiffre = match.group(1)
            match = re.search(r"Dominance ([IVXLCDM]+)", auction["item_lore"])
            Dominance_chiffre = match.group(1)
            
            results.append("    Aurora Leggings             : " + str(auction["starting_bid"]) + "  Vitality : " + str(vitality_chiffre) + " Dominance : " + str(Dominance_chiffre) + " " + auction["tier"])
    if auction["bin"] and auction["item_name"].find(item_aurora_boots) != -1:
        if auction["item_lore"].find("Vitality") != -1 and auction["item_lore"].find("Dominance") != -1:
            match = re.search(r"Vitality ([IVXLCDM]+)", auction["item_lore"])
            vitality_chiffre = match.group(1)
            match = re.search(r"Dominance ([IVXLCDM]+)", auction["item_lore"])
            Dominance_chiffre = match.group(1)
            
            results.append("    Aurora Boots                : " + str(auction["starting_bid"]) + "  Vitality : " + str(vitality_chiffre) + " Dominance : " + str(Dominance_chiffre) + " " + auction["tier"])

    if auction["bin"] and auction["item_name"].find(item_contagion_bracelet) != -1:
        if auction["item_lore"].find("Vitality") != -1 and auction["item_lore"].find("Dominance") != -1:
            match = re.search(r"Vitality ([IVXLCDM]+)", auction["item_lore"])
            vitality_chiffre = match.group(1)
            match = re.search(r"Dominance ([IVXLCDM]+)", auction["item_lore"])
            Dominance_chiffre = match.group(1)
            
            results.append("    Gauntlet of Contagion       : " + str(auction["starting_bid"]) + "  Vitality : " + str(vitality_chiffre) + " Dominance : " + str(Dominance_chiffre) + " " + auction["tier"])



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


#                              _        ,
#                             (_\______/________
#                               \-|-|/|-|-|-|-|/
#                                \==/-|-|-|-|-/
#                                 \/|-|-|-|,-'
#                                  \--|-'''
#                                   \_j________
#                                   (_)     (_)
# Crée une liste d'enchères en filtrant les enchères à partir de réponses.
# Si aucune enchère n'est trouvée, renvoie une liste vide.
auctions = [auction for response in responses for auction in response.get("auctions", [])]

#  Print dun ascii art pour dissocier deux apples dif
print("--------------------------------------------------------------------.\n| .--                    FEDERAL REVERSE NOTE                    .-- |\n| |_       ......    THE UNTIED STATES OF FRANCE                 |_  |\n| __)    ``````````             ______            B93810455B     __) |\n|      2        ___            /      \                     2        |\n|              /|~  \\         /   _-\\  \           __ _ _ _  __      |\n|             | |-< |        |  //   \  |         |_  | | | |_       |\n|              \|_//         | |-  o o| |         |   | `.' |__      |\n|               ~~~          | |\   b.' |                            |\n|       B83910455B           |  \ '~~|  |                            |\n| .--  2                      \_/ ```__/    ....            2    .-- |\n| |_        ///// ///// ////   \__\'`\/      ``  //// / ////      |_  |\n| __)                     C I N Q  E U R O S                     __) |\n`--------------------------------------------------------------------\'")

# Crée des variables pour les noms d'objets recherchés.
item_final_destination = "Final"
item_shadow_assassin = "Ancient Shadow Assassin"
item_tiger = "Tiger"
item_skeleton = "Wither Skeleton"
item_sheep="Sheep"
item_elephant="Elephant"
item_helmet_tar = "Tarantula Helmet"
item_reaper="Reaper Scythe"
item_aspect_of_the_void="Aspect of the Void"
item_molten_necklace="Molten Necklace"
item_molten_bracelet="Molten Bracelet"
item_contagion_bracelet="Gauntlet of Contagion"
item_molten_cloak="Molten Cloak"

item_aurora_chestplate="Aurora Chestplate"
item_aurora_leggings="Aurora Leggings"
item_aurora_boots="Aurora Boots"


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
categories_list = ["Final Destination Leggings", "Final Destination Helmet", "Final Destination Boots", "Final Destination Chestplate", "Reaper Scythe", "Aspect of the Void", "lvl 100", "Molten Necklace", "Molten Bracelet", "Molten Cloak", "Aurora Chestplate", "Aurora Leggings", "Aurora Boots", "Gauntlet of Contagion"]

# On crée un dictionnaire qui a pour clés les catégories et pour valeurs des listes vides.
categories_results = {category: [] for category in categories_list}

# On parcourt chaque élément de la liste results,
# puis pour chaque catégorie, si la catégorie est présente dans la chaîne de caractères de l'élément,
# on ajoute cet élément à la liste correspondante dans le dictionnaire categories_results.
for result in results:
    for category in categories_list:
        if category in str(result):
            categories_results[category].append(result)


#                           ________________
#                         _/_______________/|
#                        /___________/___//||
#                 _     |===        |----| ||
#                | |    |           |   �| ||
#  ___  ___  _ __| |_   |___________|   �| ||
# / __|/ _ \| '__| __|  | ||/.�---.||    | ||
# \__ \ (_) | |  | |_   |-||/_____\||-.  | |�
# |___/\___/|_|   \__|  |_||=L==H==||_|__|/   
# Affichage des résultats triés par catégorie
for category, results_list in categories_results.items():
    # Affichage de 100 '=' pour un meilleur affichage
    print(f"\n{category}:\n{'='*100}")
    
    # Fonction de clé personnalisée pour trier en fonction du nombre après le ':'
    def get_number_after_colon(result):
        # Recherche du nombre après le ':'
        match = re.search(r": (\d+)", result)
        return int(match.group(1)) if match else 0

    # Tri des résultats en utilisant la fonction de clé personnalisée
    sorted_results = sorted(results_list, key=get_number_after_colon)
    
    for result in sorted_results:
        print(result)