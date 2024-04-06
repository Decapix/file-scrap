import json
from scrap_insta import scrap_insta_reel, scrap_insta_publication

# Étape 1: Lire le fichier JSON
with open('back_urls.json', 'r') as file:
    data = json.load(file)

# Étape 2: Demander à l'utilisateur de choisir une tiktokeuse
print("Choisissez une tiktokeuse :")
for index, tiktokeuse in enumerate(data, start=1):
    print(f"{tiktokeuse} : {index}")
selected_index = int(input("Sélectionnez le numéro de votre tiktokeuse : "))
selected_tiktokeuse = list(data.keys())[selected_index - 1]

# Étape 3: Demander à l'utilisateur de choisir un "back"
print(f"Choisissez un back pour {selected_tiktokeuse} :")
backs = data[selected_tiktokeuse]
for index, back in enumerate(backs, start=1):
    print(f"{back} : {index}")
selected_back_index = int(input("Sélectionnez le numéro de votre back : "))
selected_back = list(backs.keys())[selected_back_index - 1]

# Stocker le chemin obtenu dans une variable
selected_path = backs[selected_back]
print(f"Le chemin sélectionné est : {selected_path}, si le chemin est faux, faite ctrl + C, puis modifiez le json")

# Initialisation d'une liste pour stocker les URLs
urls = []

print("Entrez les URLs, une par ligne. Appuyez sur Entrée sans rien écrire pour terminer :")

# Boucle pour lire les entrées utilisateur jusqu'à une ligne vide
while True:
    url = input()
    if url == "":
        break
    urls.append(url)

# bien reçu

print("Bien reçu,")

# Affichage et scraping des URLs
count = 0
for url in urls:
    count += 1
    
    try:
        # Vérification du type de lien et appel de la fonction correspondante
        if "instagram.com/p/" in url:
            scrap_insta_publication(url, selected_path, selected_tiktokeuse, selected_back)
        elif "instagram.com/reel/" in url:
            scrap_insta_reel(url, selected_path, selected_tiktokeuse, selected_back)
        elif "tiktok.com" in url and "/video/" in url:
            scrap_tiktok(url, selected_path, selected_tiktokeuse, selected_back)
        else:
            print(f"Type de contenu non pris en charge pour l'URL {count}")
            break
        
        print(f"Scraping de l'url {count} réussi \n Et tous en coeur : VIVE LES FOURMIS !!!")
    except Exception as e:
        print(f"Scraping de l'url {count} échoué: {e}")



