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
# Détermination du système d'exploitation
os_name = platform.system().lower()

# Sélection du chemin du pilote en fonction du système d'exploitation et du navigateur
if os_name == "linux":
    path_to_driver = '/home/solenopsis/Documents/work/business/postauto/fichier-de-travail-temporaire/srcap/geckodriver'  # Chemin pour Linux
elif os_name == "windows":
    path_to_driver = "C:\\path\\to\\chromedriver.exe"  # Chemin pour Windows

# Initialisation du navigateur
if "linux" in os_name:
    service = FirefoxService(executable_path=path_to_driver)
    driver = webdriver.Firefox(service=service)
elif "windows" in os_name:
    driver = webdriver.Chrome(executable_path=path_to_driver)

driver.get('https://snaptik.app/fr')
time.sleep(2)

# button consent
button = driver.find_element(By.CLASS_NAME, 'fc-button-label')
button.click()

# Trouver le champ de saisie et y insérer un lien
form_url = driver.find_element(By.ID, 'url')
form_url.send_keys('https://www.tiktok.com/@romandoduik/video/7354096861323480353')  # Remplacez ceci par l'URL réelle que vous souhaitez utiliser

# Simuler la pression de la touche "Entrée"
time.sleep(2)
form_url.send_keys(Keys.RETURN)


# Tentative de trouver et cliquer sur le bouton
try:
    button2 = driver.find_element(By.CLASS_NAME, 'ns-69urh-e-16')
    button2.click()
except NoSuchElementException:
    print("Le bouton n'a pas été trouvé, on continue le script.")
    # Ici, le script continue même si le bouton n'est pas trouvé

try:
    # Ajustez le temps d'attente selon les besoins
    wait = WebDriverWait(driver, 10)  # Attendre jusqu'à 10 secondes
    button3 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.video-links > a.download-file')))
    button3.click()
    print("Bouton cliqué.")
except TimeoutException:
    print("Le bouton n'était pas cliquable après 10 secondes d'attente.")

