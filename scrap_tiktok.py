"""pour linux ou windows, dans tous les cas, seras firefox"""

import time
import platform
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import json
import os
import shutil
from datetime import datetime
from pathlib import Path



def scrap_tiktok(url_list):
    # Lire le fichier param.json
    with open("param.json", "r") as f:
        params = json.load(f)

    download_count = 0  # Compteur pour les téléchargements réussis

    # need firefox
    path_to_driver = params["driver"]
    service = FirefoxService(executable_path=path_to_driver)
    driver = webdriver.Firefox(service=service)

    for url_tik in url_list:
        driver.get('https://tikdownload.com/')
        time.sleep(2)

        # Gestion du bouton de consentement
        try:
            button = driver.find_element(By.CLASS_NAME, 'fc-button-label')
            button.click()
        except NoSuchElementException:
            print("Le bouton de consentement n'a pas été trouvé, on continue le script. (cecis n'est pas une erreur, stresse pas)")

        # Remplir le formulaire avec l'URL et soumettre
        try:
            form_url = driver.find_element(By.ID, 'form-field-url')
            form_url.send_keys(url_tik)
            time.sleep(0.5)
            form_url.send_keys(Keys.RETURN)

            # Attendre et cliquer sur le bouton de téléchargement
            wait = WebDriverWait(driver, 10)
            button3 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.tiktok-info > a.download-btn')))
            button3.click()
            download_count += 1
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Erreur lors du téléchargement de la vidéo : {url_tik}")
            print(str(e))
        time.sleep(5)

    # Fermer le navigateur après les téléchargements
    driver.quit()

    # Retourner le nombre de téléchargements réussis
    return download_count





def move_videos(download_folder, target_folder, tiktokeuse, back, num_files):
    # Assurez-vous que le dossier cible existe
    Path(target_folder).mkdir(parents=True, exist_ok=True)

    # Trouver tous les fichiers .mp4 dans le dossier de téléchargement
    mp4_files = [f for f in Path(download_folder).glob('*.mp4')]

    # Trier les fichiers par date de modification, les plus récents en premier
    mp4_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)

    # Sélectionner les x derniers fichiers
    latest_files = mp4_files[:num_files]

    # Déplacer et renommer les fichiers
    for file in latest_files:
        # Format du nouveau nom de fichier
        today = datetime.today().strftime('%d.%m.%Y-%H.%M.%S')
        new_filename = f"{today}-{tiktokeuse}-{back}.mp4"
        new_filepath = Path(target_folder) / new_filename

        # Vérifier si le fichier existe déjà et modifier le nom si nécessaire
        counter = 2
        while new_filepath.exists():
            new_filename = f"{today}-{tiktokeuse}-{back}-{counter}.mp4"
            new_filepath = Path(target_folder) / new_filename
            counter += 1

        # Déplacer et renommer le fichier
        shutil.move(str(file), str(new_filepath))
