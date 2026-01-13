# Ad Clicker Premium pour Bing

Cet outil en ligne de commande clique des urls comprenant "safehdf.com" ou "coffrefort.safehdf.com" pour une requête sur Bing en utilisant le package [undetected_chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver). Il prend en charge les proxys, l’exécution simultanée de plusieurs navigateurs, le ciblage/exclusion d’annonces et l’exécution en boucle.

* Fonctionnalités supplémentaires de la version Premium

    * 🛠️ Fichier de configuration unique pour toutes les options
    * 🖥️ Interface graphique pour configurer et lancer
    * 🗑️ Nettoyage du cache et des cookies à la fermeture du navigateur
    * 📄 Fichier externe pour les user agents
    * 🖼️ Définir la taille de la fenêtre du navigateur
    * 🎲 Décaler les fenêtres du navigateur avec des offsets aléatoires
    * 🌍 Définir l’URL d’ouverture en fonction du pays du proxy
    * 🈵 Définir la langue du navigateur en fonction du pays du proxy
    * 🖱️ Défilements et mouvements de souris aléatoires sur les pages
    * 🔗 Cliquer des liens non sponsorisés avec filtrage de domaines ou au hasard
    * 🔄 Ordre de clic personnalisé entre liens sponsorisés et non sponsorisés
    * ⏱️ Définir une plage min/max d’attente pour les pages sponsorisées et non sponsorisées
    * 📜 Limiter le défilement max sur la page de résultats
    * 🍪 Utiliser des cookies personnalisés collectés
    * ⏳ Définir l’intervalle d’exécution
    * 📊 Résumé des statistiques
    * 🛍️ Cliquer les annonces Shopping du haut (jusqu’à 5)
    * 🔐 Intégration 2captcha
    * 📨 Notifications Telegram
    * 📝 Générer un rapport quotidien des clics
    * 📱 Ouvrir les liens trouvés sur un appareil Android
    * 🪝 Hooks pour étendre l’outil avec un comportement personnalisé
    * 💻 Tableau de bord de contrôle à distance ([s’abonner ici](https://buy.stripe.com/00gdU8c3rg8KcUMdR7)) ([voir comment ça marche](https://vimeo.com/1072189164))

        ![rapport de clics](assets/dashboard.png)

<br>

* Nécessite Python 3.9 à 3.11
* Nécessite la dernière version de Chrome


## Configuration

* Exécutez les commandes suivantes dans le dossier du projet pour installer les dépendances requises.
    * `python -m venv env`
    * `.\env\Scripts\activate`
    * `python -m pip install -r requirements.txt`





## Lancement

* Vous devez voir `(env)` au début de votre invite de commandes pour indiquer que l’environnement virtuel est activé.

* Avant d’exécuter les commandes ci-dessous pour la première fois, lancez `python ad_clicker.py -q test` une fois, puis stoppez avec CTRL+C après l’ouverture du navigateur.

* Lancez `python ad_clicker.py` pour un run unique avec un seul navigateur.
* Lancez `python run_ad_clicker.py` pour un run unique avec plusieurs navigateurs.
* Lancez `python run_in_loop.py` pour exécuter en boucle avec un ou plusieurs navigateurs.
* Lancez `python gui.py` pour ouvrir l’interface graphique de configuration/exécution.

    ![gui](assets/bing_ad_clicker_gui.png)

* Lancez `python ad_clicker.py --report_clicks` pour générer un rapport de clics.
* Lancez `python ad_clicker.py --report_clicks --date` pour générer un rapport de clics pour la date donnée au format JJ-MM-AAAA.
* Lancez `python ad_clicker.py --report_clicks --excel` pour générer un rapport de clics et écrire les résultats dans un fichier Excel.

    * Exemple de rapport
    ![rapport de clics](assets/click_report.png)

<br>

### Options de configuration

Toutes les options peuvent être définies dans `config.json` à la racine du projet.

Les valeurs ci-dessous sont celles par défaut dans le fichier de configuration.

```json
{
    "paths": {
        "query_file": "sample_queries.txt",
        "proxy_file": "",
        "user_agents": "user_agents.txt",
        "filtered_domains": "domains.txt"
    },
    "webdriver": {
        "proxy": "",
        "auth": true,
        "incognito": false,
        "country_domain": false,
        "language_from_proxy": false,
        "ss_on_exception": false,
        "window_size": "",
        "shift_windows": false
    },
    "behavior": {
        "query": "",
        "ad_page_min_wait": 10,
        "ad_page_max_wait": 15,
        "nonad_page_min_wait": 15,
        "nonad_page_max_wait": 20,
        "max_scroll_limit": 0,
        "check_shopping_ads": true,
        "excludes": "",
        "random_mouse": false,
        "custom_cookies": false,
        "click_order": 5,
        "browser_count": 2,
        "multiprocess_style": 1,
        "loop_wait_time": 60,
        "wait_factor": 1.0,
        "running_interval_start": "00:00",
        "running_interval_end": "00:00",
        "2captcha_apikey": "",
        "hooks_enabled": false,
        "telegram_enabled": false,
        "send_to_android": false
    }
}
```

* **query_file** : Chemin du fichier qui contient les requêtes à rechercher. Utilisé avec `run_ad_clicker.py` et `run_in_loop.py`. Mettez une requête par ligne.

* **proxy_file** : Chemin du fichier contenant les proxys. Mettez un proxy par ligne.

* **user_agents** : Chemin du fichier contenant les user agents. Valeur par défaut : `user_agents.txt`.

* **filtered_domains** : Chemin du fichier contenant les domaines à filtrer pour cliquer des liens non sponsorisés. Valeur par défaut : `domains.txt` à la racine du projet. Si vous ne voulez pas filtrer les domaines, laissez `domains.txt` vide et 3 liens seront choisis aléatoirement.

* **proxy** : Utiliser le proxy indiqué avec `ad_clicker.py`. Les paramètres `proxy_file` et `proxy` ne peuvent pas être utilisés en même temps.

* **auth** : Utiliser un proxy avec identifiant et mot de passe. Si c’est `true`, vos proxys doivent être au format `username:password@host:port`.

* **incognito** : Exécuter en mode incognito. Notez que l’extension proxy n’est pas activée en mode incognito.

* **country_domain** : Définir l’URL d’ouverture en fonction du pays du proxy.

* **language_from_proxy** : Définir la langue (locale) du navigateur en fonction du pays du proxy.

* **ss_on_exception** : Activer la capture d’écran en cas d’exception.

* **window_size** : Définir la taille de la fenêtre au format `largeur,hauteur` en pixels.

* **shift_windows** : Décaler les fenêtres avec des offsets x,y aléatoires.
    * Si vous utilisez un zoom d’affichage différent de 100 %, utilisez cette option avec `window_size`.
    * Si une `window_size` personnalisée est fournie, elle détermine la nouvelle largeur/hauteur de la fenêtre. Sinon, la résolution de l’écran est utilisée.

* **query** : Requête de recherche. Les paramètres `query_file` et `query` ne peuvent pas avoir de valeur en même temps.
    * Une requête comme "wireless speaker@amazon#ebay  # mediamarkt" recherche "wireless speaker" et clique les liens contenant les mots de filtre dans l’URL ou le titre.

    * Les espaces autour de "@" et "#" sont ignorés, donc "wireless speaker@amazon#ebay" et
    "wireless speaker @ amazon  # ebay" prennent "wireless speaker" comme requête et "amazon" et "ebay" comme mots de filtre.

    * Si vous fournissez un domaine cible comme mot de filtre, n’utilisez pas les parties "http" ou "www". Utilisez plutôt "requete@domainname.com" ou même "requete@domainname". Gardez-le le plus court possible pour obtenir un match.

* **ad_page_min_wait** : Nombre minimal de secondes à attendre sur la page sponsorisée. La valeur est choisie aléatoirement entre min/max.
* **ad_page_max_wait** : Nombre maximal de secondes à attendre sur la page sponsorisée.
* **nonad_page_min_wait** : Nombre minimal de secondes à attendre sur la page non sponsorisée.
* **nonad_page_max_wait** : Nombre maximal de secondes à attendre sur la page non sponsorisée.

* **max_scroll_limit** : Nombre maximal de défilements sur la page de résultats. Par défaut (0), défile jusqu’en bas.

* **check_shopping_ads** : Activer le clic des annonces Shopping affichées en haut (jusqu’à 5) si présentes. Elles apparaissent plus souvent avec des proxys résidentiels.

* **excludes** : Exclure les annonces contenant certains mots dans l’URL ou le titre.
    * Une valeur comme "amazon.com,mediamarkt.com,for 2022,Soundbar" clique les liens sauf ceux contenant ces mots.
    * Séparez plusieurs éléments par des virgules.

* **random_mouse** : Activer les mouvements aléatoires de la souris sur les pages.

* **custom_cookies** : Utiliser des cookies personnalisés collectés. Ils doivent être dans `cookies.txt` à la racine du projet.

* **click_order** : Ordre des clics pour les liens sponsorisés et non sponsorisés.
    * 1 : cliquer tous les liens non sponsorisés d’abord, puis les liens sponsorisés
    * 2 : cliquer tous les liens sponsorisés d’abord, puis les liens non sponsorisés
    * 3 : cliquer 1 lien non sponsorisé, puis 1 lien sponsorisé, puis tous les non sponsorisés restants, enfin tous les sponsorisés restants
    * 4 : cliquer 1 lien non sponsorisé, puis 1 lien sponsorisé à chaque tour
    * 5 : mélanger les liens sponsorisés et non sponsorisés et cliquer selon l’ordre créé (par défaut)

* **browser_count** : Nombre maximum de navigateurs à exécuter en parallèle. Utilisé avec `run_ad_clicker.py` et `run_in_loop.py`.
    * Si la valeur est 0, le nombre de cœurs CPU est utilisé.

* **multiprocess_style** : Style d’exécution multiprocess. Utilisé avec `run_ad_clicker.py` et `run_in_loop.py`.
    * 1 : requête différente dans chaque navigateur (par défaut)
        * ex. : les requêtes sont mélangées, puis 5 navigateurs recherchent les 5 premières requêtes.
    * 2 : même requête pour chaque navigateur
        * ex. : 5 navigateurs recherchent la première requête. Après leur exécution, le groupe suivant traite la seconde requête, etc.

    * Si le nombre de requêtes ou de proxys est inférieur au nombre de navigateurs à exécuter, ils sont recyclés.
