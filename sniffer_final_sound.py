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
categories_list = ["Final Destination Helmet", "Final Destination Chestplate"]

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
#                | |    |           |    | ||
#  ___  ___  _ __| |_   |___________|    | ||
# / __|/ _ \| '__| __|  | ||/.---. ||    | ||
# \__ \ (_) | |  | |_   |-||/_____\||-.  | |
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