import json
from scrap_insta import scrap_insta_reel, scrap_insta_publication
from scrap_tiktok import scrap_tiktok

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
# Initialisation des listes pour chaque type de contenu
instagram_posts = []
instagram_reels = []
tiktok_videos = []

# Tri des URLs
for url in urls:
    if "instagram.com/p/" in url:
        instagram_posts.append(url)
    elif "instagram.com/reel/" in url:
        instagram_reels.append(url)
    elif "tiktok.com" in url and "/video/" in url:
        tiktok_videos.append(url)
    else:
        print(f"Type de contenu non pris en charge pour l'URL {url}")

# Scraping des publications Instagram
for url in instagram_posts:
    try:
        scrap_insta_publication(url, selected_path, selected_tiktokeuse, selected_back)
        print(f"Scraping réussi pour la publication Instagram : {url}")
    except Exception as e:
        print(f"Scraping échoué pour la publication Instagram {url}: {e}")

# Scraping des reels Instagram
for url in instagram_reels:
    try:
        scrap_insta_reel(url, selected_path, selected_tiktokeuse, selected_back)
        print(f"Scraping réussi pour le reel Instagram : {url}")
    except Exception as e:
        print(f"Scraping échoué pour le reel Instagram {url}: {e}")

# Scraping des vidéos TikTok
for url in tiktok_videos:
    try:
        scrap_tiktok(url, selected_path, selected_tiktokeuse, selected_back)
        print(f"Scraping réussi pour le tiktok : {url}")
    except Exception as e:
        print(f"Scraping échoué pour le tiktok {url}: {e}")





