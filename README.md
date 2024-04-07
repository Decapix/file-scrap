

## Instructions d'installation et d'exécution

Suivez les étapes ci-dessous pour configurer et exécuter le script.

## Configuration de l'environnement

1. Créez un environnement virtuel Python :

   ```
   py -m venv .env
   ```

2. Activez l'environnement virtuel :

   - Sur Windows :

     ```bash
     .env\Scripts\activate
     ```

   - Sur macOS et Linux :

     ```bash
     source .env/bin/activate
     ```

3. Installez les dépendances nécessaires :

   ```bash
   pip install instaloader json selenium platform
   ```

## Configuration du script

- installer firfox et un web driver pour selenium : https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-win-aarch64.zip
- Éditez le fichier `back_url.json` avec les répertoires correct
- Éditez le fichier `param.json` avec les répertoires correct

## Exécution du script

Lancez le script en utilisant la commande suivante :

```bash
py scrap.py
```


j'ai 
python3.12.2
selenium==4.19.0


