"""pour linux ou windows, dans tous les cas, seras firefox"""
import os
import requests
from datetime import datetime
from pathlib import Path
import shutil

# Configurer les headers avec un user-agent aléatoire
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4182.0 Safari/537.36'
}

def get_video_id_from_url(url):
    """
    Extrait l'ID de la vidéo à partir de l'URL TikTok donnée.
    """
    # L'ID de la vidéo se trouve après '/video/' et avant le prochain slash ou signe d'interrogation
    parts = url.split('/video/')[1]
    video_id = parts.split('?')[0]
    return video_id


def download_video(video_id, directory):
    API_URL = f'https://api22-normal-c-alisg.tiktokv.com/aweme/v1/feed/?aweme_id={video_id}&iid=7318518857994389254&device_id=7318517321748022790&channel=googleplay&app_name=musical_ly&version_code=300904&device_platform=android&device_type=ASUS_Z01QD&version=9'
    
    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        
        # Vérifier si la vidéo existe
        if data['aweme_list'][0]['aweme_id'] != video_id:
            print('La vidéo n\'existe pas ou a été supprimée.')
            return None

        video_url = data['aweme_list'][0]['video']['play_addr']['url_list'][0]
        video_content = requests.get(video_url, headers=headers, stream=True)

        # Définir le chemin de téléchargement
        download_path = os.path.join(directory, f'{video_id}.mp4')

        with open(download_path, 'wb') as f:
            for chunk in video_content.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        print(f'Vidéo téléchargée: {download_path}')
        return download_path
    else:
        print('Erreur lors de la récupération de la vidéo.')
        return None

def scrap_tiktok(url, directory, tiktokeuse, back):
    video_id = get_video_id_from_url(url)

    # Jules version
    num_files = len([name for name in os.listdir(destination_directory) if os.path.isfile(os.path.join(destination_directory, name))])
    new_filename = f"Back {num_files + 1}.mp4"
    destination_directory = str(directory)

    # date version
    # today = datetime.today().strftime('%d.%m.%Y-%H.%M.%S')
    # new_filename = f"{today}-{tiktokeuse}-{back}.mp4"

    # Télécharger la vidéo
    download_path = download_video(video_id, destination_directory)

    if download_path:
        # Construire le nouveau chemin de fichier
        new_file_path = os.path.join(destination_directory, new_filename)

        try:
            # Renommer et déplacer le fichier
            shutil.move(download_path, new_file_path)
            print(f"Vidéo renommée et déplacée: {new_file_path}")
        except Exception as e:
            print(f"Erreur lors du déplacement/renommage du fichier: {e}")
    else:
        print("Le téléchargement de la vidéo a échoué.")
