

## Instructions d'installation et d'exécution

Suivez les étapes ci-dessous pour configurer et exécuter le script.

## Configuration de l'environnement (optionel)

1. Créez un environnement virtuel Python3.12 :

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
   pip install instaloader==4.11 requests==2.31.0
   ```

## Configuration du script

- Éditez le fichier `back_url.json` avec les répertoires correct

## Exécution du script

Lancez le script en utilisant la commande suivante :

```bash
py scrap.py
```


