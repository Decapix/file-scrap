import instaloader
from datetime import datetime
import os
import shutil


def scrap_insta_reel(url, directory, tiktokeuse, back):
    loader = instaloader.Instaloader()

    # Obtenir le répertoire du script en cours d'exécution
    current_directory = os.path.dirname(os.path.abspath(__file__))
    today = datetime.today().strftime('%d.%m.%Y-%H.%M.%S')
    new_filename = f"{today}-{tiktokeuse}-{back}"
    destination_directory = str(directory)


    # Télécharger le post à partir de l'URL
    post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
    loader.download_post(post, target="temp")
    print(f"étape 1 ok")


    # Chemin du dossier "temp" dans le répertoire actuel
    temp_directory = os.path.join(current_directory, "temp")

    # Vérifier si le dossier "temp" existe
    if os.path.exists(temp_directory) and os.path.isdir(temp_directory):
        # Lister le contenu du dossier "temp" et rechercher un fichier .mp4
        mp4_files = [file for file in os.listdir(temp_directory) if file.endswith('.mp4')]

        if mp4_files:
            # Supposons que vous souhaitez déplacer le premier fichier .mp4 trouvé
            mp4_file = mp4_files[0]
            source_path = os.path.join(temp_directory, mp4_file)
            destination_path = os.path.join(destination_directory, new_filename)
            try:
                # Déplacer et renommer le fichier .mp4
                shutil.move(source_path, destination_path)
                print(f"étape 2 ok")
            except Exception as e:
                print("deplacer le fichier mp4 a échoué: {e}")
        else:
            print("Aucun fichier .mp4 trouvé dans le dossier temp.")

        # Supprimer le dossier 'temp' et son contenu
        shutil.rmtree(temp_directory)
        print(f"étape 3 ok")




def scrap_insta_publication(url, directory, tiktokeuse, back):
    loader = instaloader.Instaloader()

    # Obtenir le répertoire du script en cours d'exécution
    current_directory = os.path.dirname(os.path.abspath(__file__))
    today = datetime.today().strftime('%d.%m.%Y-%H.%M.%S')
    new_filename = f"{today}-{tiktokeuse}-{back}"
    destination_directory = str(directory)


    # Télécharger le post à partir de l'URL
    post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
    loader.download_post(post, target="temp")
    print(f"étape 1 ok")


    # Chemin du dossier "temp" dans le répertoire actuel
    temp_directory = os.path.join(current_directory, "temp")

    if os.path.exists(temp_directory) and os.path.isdir(temp_directory):
        # Parcourir les fichiers du dossier "temp"
        count = 0
        for filename in os.listdir(temp_directory):
            if filename.endswith('.jpg'):
                count += 1
                # Construire le chemin complet du fichier source et de destination
                source = os.path.join(temp_directory, filename)
                destination = os.path.join(destination_directory, new_filename + "-" + str(count))

                # Déplacer et renommer le fichier
                shutil.move(source, destination)
                print(f"étape 2 ok")

        # Supprimer le dossier "temp" une fois les fichiers déplacés
        shutil.rmtree(temp_directory)
        print(f"étape 3 ok")
    else:
        print(f"Le dossier '{temp_directory}' n'existe pas ou n'est pas un dossier.")

