import requests
import re

def get_bazaar_product_data():
    url = f"https://api.hypixel.net/v2/skyblock/bazaar"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur lors de la requête : {response.status_code}")
        return None


bazaar_data = get_bazaar_product_data()
bazaar_data = bazaar_data["products"]
# Initialisation du dictionnaire pour stocker les pourcentages de bénéfice
profit_dict = {}


# Parcours de chaque produit dans bazaar_data
for product_id, product_info in bazaar_data.items():
    # Vérification si le produit ne commence pas par "ENCHANTMENT_"
    if not product_id.startswith("ENCHANTMENT_"):
        # Récupération des informations sur le produit
        sell_price = product_info['quick_status']['sellPrice']
        buy_price = product_info['quick_status']['buyPrice']

        # Vérification si les prix ne sont pas nuls
        if sell_price != 0.0 and buy_price != 0.0:
            # Calcul du pourcentage de bénéfice
            profit_percentage = (buy_price / sell_price)

            # Stockage dans le dictionnaire profit_dict
            profit_dict[product_id] = profit_percentage

# Tri du dictionnaire par ordre croissant de pourcentage de bénéfice
sorted_profit = sorted(profit_dict.items(), key=lambda x: x[1])

# Affichage des produits triés par bénéfice croissant
for product_id, profit_percentage in sorted_profit:
    print(f"productId: {product_id}")
    print(f"buyPrice: {bazaar_data[product_id]['quick_status']['buyPrice']}")
    print(f"sellPrice: {bazaar_data[product_id]['quick_status']['sellPrice']}")
    print(f"Profit Percentage: {profit_percentage}")
    print()