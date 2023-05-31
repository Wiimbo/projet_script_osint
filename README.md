# projet_script_osint
Ce script Python vise à automatiser diverses tâches de reconnaissance et d'analyse de sécurité.

            ################### IMPORTANT #####################

POUR EVITER TOUT PROBLEME LE SCRIPT DOIT ETRE LANCER SUR UNE DISTRIBUTION KALI LINUX


            ################### PRE REQUIS ####################


Une fois sur votre distribution Kali Linux, le script setup.sh permet de vérifier les installations des outils nécessaires au bon fonctionnement

ATTENTION si vous utilisez une autre distribution que KALI LINUX il y aura potentiellement des problemes (du aux chemins/raccourcis)

- vérifie installation de : 
    -Python3
    -Pip 
    -Git 
    -Shodan
    -Whois
    -NMAP  

Pensez a éxécuter le script en ROOT ( pour les installations nécessaires des modules non cité ci-dessus si nécessaire) ainsi qu'au bon fonctionnement de certains outils


Voici un aperçu de son fonctionnement :


Vérification des modules requis :

Vérifie la présence des modules nécessaires.
Propose l'installation des modules manquants via pip.


Choix de l'option :

Demande à l'utilisateur de choisir parmi les options disponibles : nmap, TheHarvester, Shodan ou Whois.

Option Nmap :

Demande l'adresse IP cible à l'utilisateur.
Affiche les options disponibles pour Nmap.
Exécute la commande Nmap avec les options choisies.
Enregistre les résultats du scan dans un fichier texte.

Option TheHarvester :

Demande à l'utilisateur de saisir un nom de domaine.
Exécute TheHarvester avec le nom de domaine spécifié.
Enregistre les résultats dans un fichier texte.

Option Shodan :

##### utiliser votre clé API (gratuit mais attention limité a 100requetes/mois) #####

Demande à l'utilisateur une adresse IP.
Utilise l'API Shodan pour rechercher des informations sur cette adresse IP.
Enregistre les résultats dans un fichier texte.

Option Whois :

Demande à l'utilisateur de saisir un nom de domaine.
Utilise la commande "whois" pour obtenir les informations WHOIS correspondantes.
Enregistre les résultats dans un fichier texte.


Ce script permet d'automatiser des tâches de reconnaissance et d'analyse de sécurité telles que les scans de ports, la collecte d'informations sur les domaines, la recherche d'informations sur les adresses IP et l'obtention des détails WHOIS. Il offre une manière pratique d'utiliser des outils tels que Nmap, TheHarvester, Shodan et la commande "whois" pour effectuer ces actions.
