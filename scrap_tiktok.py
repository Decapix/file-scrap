import os
import shutil
from datetime import datetime
import yt_dlp

def get_video_id_from_url(url):
    """
    Extrait l'ID de la vidéo à partir de l'URL TikTok donnée.
    """
    parts = url.split('/video/')[1]
    video_id = parts.split('?')[0]
    return video_id

def download_video_with_ytdlp(url, directory):
    """
    Utilise yt-dlp pour télécharger la vidéo à partir de l'URL fournie.
    """
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(directory, '%(id)s.%(ext)s'),
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(url, download=True)
            video_id = info_dict.get('id', None)
            file_ext = info_dict.get('ext', 'mp4')
            download_path = os.path.join(directory, f'{video_id}.{file_ext}')
            return download_path
        except yt_dlp.utils.DownloadError:
            print('Erreur lors de la récupération de la vidéo.')
            return None

def scrap_tiktok(url, directory, tiktokeuse, back):
    video_id = get_video_id_from_url(url)
    num_files = len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])
    new_filename = f"Back {num_files + 1}.mp4"
    destination_directory = str(directory)

    # Télécharger la vidéo avec yt-dlp
    download_path = download_video_with_ytdlp(url, destination_directory)

    if download_path:
        new_file_path = os.path.join(destination_directory, new_filename)

        try:
            shutil.move(download_path, new_file_path)
            print(f"Vidéo renommée et déplacée: {new_file_path}")
        except Exception as e:
            print(f"Erreur lors du déplacement/renommage du fichier: {e}")
    else:
        print("Le téléchargement de la vidéo a échoué.")