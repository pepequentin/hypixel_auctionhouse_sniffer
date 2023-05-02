#Autor   : quentin.peridon@hotmail.fr
#Version : 1.2
#Date    : 29/04/2023

#imports
import requests
import json

responses = []
url = f"https://api.hypixel.net/skyblock/auctions"


#get the number of page in the auctions house
response = requests.get(url)
response_json = response.json()
if response_json.get("success") == False and response_json.get("cause") == "Page not found":
    exit
number_of_page=(response_json.get("totalPages"))

#loop on all pages of the auction house in order to fill responses[]
for i in range(0, number_of_page):
    url = f"https://api.hypixel.net/skyblock/auctions?page={i}"
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
item_helmet_tar = "Tarantula Helmet"

# Parcours chaque enchère pour les objets recherchés.
for auction in auctions:
    try:
        # Recherche l'objet "Final Destination" pour des enchères légendaires et mythiques à bas prix.
        if auction["bin"] and auction["item_name"].find(item_final_destination) != -1:
            # L'objet "Final Destination" a une enchère initiale de 15M à 22M.
            if auction["tier"] == "LEGENDARY" and auction["item_lore"].find("50,000") != -1 and auction["starting_bid"] < 14999999:
                print("Potential 50 000 leg        : " + auction["item_name"] + " at the price of " + str(auction["starting_bid"]))
            elif auction["tier"] == "MYTHIC" and auction["item_lore"].find("50,000") != -1 and auction["starting_bid"] < 27999999:
                print("Potential 50 000 mythic     : " + auction["item_name"] + " at the price of " + str(auction["starting_bid"]))
            elif auction["tier"] == "MYTHIC" and auction["item_lore"].find("100,000") != -1 and auction["starting_bid"] < 35000000:
                print("Potential 100 000 mythic    : " + auction["item_name"] + " at the price of " + str(auction["starting_bid"]))

        # Recherche l'objet "Tiger" pour des enchères épiques et légendaires à bas prix.
        elif auction["bin"] and auction["item_name"].find(item_tiger) != -1:
            if auction["tier"] == "EPIC" and auction["item_name"].find("Lvl 100") != -1 and auction["starting_bid"] < 18000000:
                print("Tiger epic lvl 100          : " + str(auction["starting_bid"]))
            elif auction["tier"] == "LEGENDARY" and auction["item_name"].find("Lvl 100") != -1 and auction["starting_bid"] < 35000000:
                print("Tiger leg lvl 100           : " + str(auction["starting_bid"]))

        # Recherche l'objet "Wither Skeleton" pour des enchères légendaires à bas prix.
        elif auction["bin"] and auction["item_name"].find(item_skeleton) != -1:
            if auction["tier"] == "LEGENDARY" and auction["item_name"].find("Lvl 100") != -1 and auction["starting_bid"] < 9000000:
                print("Wither skeleton leg lvl 100 : " + str(auction["starting_bid"]))

        # Recherche l'objet "Tarantula Helmet" pour des enchères mythiques à bas prix.
        elif auction["bin"] and auction["item_name"].find(item_helmet_tar) != -1:
            if auction["tier"] == "MYTHIC" and auction["item_lore"].find("25,000") != -1 and auction["starting_bid"] < 20000000:
                print("Potential helmet tarantula : " + str(auction["starting_bid"]))
            if auction["tier"] == "MYTHIC" and auction["item_lore"].find("50,000") != -1 and auction["starting_bid"] < 30000000:
                print("Potential helmet tarantula : " + str(auction["starting_bid"]))

    except KeyError:
        pass
