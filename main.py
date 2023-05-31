#!/usr/lib/python
import importlib
import os
import ipaddress
import subprocess
import importlib.util
import sys
import shodan

print("PENSER A ETRE EN ROOT\n")

# Demander à l'utilisateur de choisir entre deux options

print("Veuillez choisir une option :\n")
print("1. nmap(IP)")
print("2. TheHarvester(domaine)")
print("3. Shodan(IP)")
print("4. Whois(domaine/ip)\n")
option = input("Votre choix : ")


#NMAP 


if option == "1":

    while True:
        try:
            adresse_ip = ipaddress.ip_address(input("ip address :"))
            break
        except ValueError:
            print("it's not an Ip Address (exemple: 192.168.0.1)")

    print("Ip address saved:",adresse_ip)

# options de commandes Nmap disponibles
    nmap_options = {
        1:"Interactive mode    -sS -A",
        2:"OS detection     -sS -O",
        3:"Scan UDP ports    -sU",
        4:"Version detection    -sS -sV",
    }

# demander à l'utilisateur quelle option Nmap utiliser
    print("\nVeuillez sélectionner une option Nmap :")
    for key, value in nmap_options.items():
        print(f"{key}. {value}")
    option = int(input("Option : "))
    option = nmap_options.get(option)

# exécuter le scan Nmap avec les options choisies
    resultat = subprocess.run(f"nmap {option} {adresse_ip}", shell=True, capture_output=True, text=True)

# nom de base du fichier
    nom_fichier1 = "resultat_scan_nmap"

# compteur pour les noms de fichier
    compteur = 0

# tant que le fichier existe, incrémenter le compteur
    while os.path.exists(nom_fichier1 + str(compteur) + ".txt"):
        compteur += 1

# créer le nom de fichier avec le compteur
    nom_fichier1 = nom_fichier1 + str(compteur) + ".txt"

# écrire le résultat dans un fichier texte
    with open(nom_fichier1, "w") as fichier:
        fichier.write(f"Commande Nmap exécutée : nmap {option} {adresse_ip}\n\n")
        fichier.write(resultat.stdout)

    print(f"Scan terminé avec l'option : {option} . Résultats enregistrés dans '{nom_fichier1}'.")






#TheHarvester

elif option == "2":
    
    domain = input("Entrez le nom de domaine : ")
   
    # nom de base du fichier
    nom_fichier2 = f"{domain}_theHarvester"

    # Utilisation de TheHarvester pour récupérer les informations et les enregistrer dans un fichier texte
    commande = f"theHarvester -d {domain} -l 500 -b all"
    resultat = os.popen(commande).read()
    with open(f"{nom_fichier2}.txt", "w") as fichier:
        fichier.write(resultat)

    

    # compteur pour les noms de fichier
    compteur = 0

    # tant que le fichier existe, incrémenter le compteur
    while os.path.exists(nom_fichier2 + str(compteur) + ".txt"):
        compteur += 1

    # créer le nom de fichier avec le compteur
    nom_fichier2 = nom_fichier2 + str(compteur) + ".txt"

    print(f"Scan theHarvester terminé. Résultats enregistrés dans '{nom_fichier2}'.")





#SHODAN 

elif option == "3":

    # Clé API Shodan
    API_KEY = "VxKNazIXFq5lHj3e0aryaIMvHUpHUPoT"
    
    # Demande de l'adresse IP à l'utilisateur
    ip_address = input("Entrez une adresse IP : ")

    # Initialisation de l'API Shodan
    api = shodan.Shodan(API_KEY)

    # Nom du fichier de sortie
    output_file = "shodan_results.txt"

    # Vérification de l'existence du fichier de sortie
    if os.path.exists(output_file):
        file_count = 1
        while True:
            new_output_file = f"shodan_results{file_count}.txt"
            if not os.path.exists(new_output_file):
                output_file = new_output_file
                break
            file_count += 1

    try:
        # Recherche dans Shodan
        results = api.host(ip_address)

        # Extraction des informations nécessaires
        hostnames = results.get('hostnames', [])
        domains = results.get('domains', [])
        country = results.get('country_name', 'N/A')
        city = results.get('city', 'N/A')
        organization = results.get('org', 'N/A')
        isp = results.get('isp', 'N/A')
        asn = results.get('asn', 'N/A')
        ports = results.get('data', [])

        # Enregistrement des résultats dans un fichier texte
        with open(output_file, "w") as file:
            file.write(f"Hostnames\t: {', '.join(hostnames)}\n")
            file.write(f"Domains\t: {', '.join(domains)}\n")
            file.write(f"Country\t: {country}\n")
            file.write(f"City\t: {city}\n")
            file.write(f"Organization\t: {organization}\n")
            file.write(f"ISP\t: {isp}\n")
            file.write(f"ASN\t: {asn}\n")
            file.write("Open ports:\n")
            for port_info in ports:
                port = port_info.get('port', 'N/A')
                transport = port_info.get('transport', 'N/A')
                product = port_info.get('product', 'N/A')
                version = port_info.get('version', 'N/A')
                file.write(f"\t{port}/{transport}\tService: {product}\tVersion: {version}\n")
                if product != 'N/A':
                    file.write(f"\t\tActive Service: {product}\n")

        print(f"Les résultats ont été enregistrés dans le fichier {output_file}")

    except shodan.APIError as e:
        print("Erreur lors de la recherche dans Shodan :", e)



#WHOIS

elif option == "4":

    import subprocess
    import os

    def get_whois_info(domain):
        try:
            result = subprocess.run(["whois", domain], capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout
            else:
                return f"Erreur lors de l'exécution de la commande whois : {result.stderr}"
        except FileNotFoundError:
            return "La commande whois n'est pas disponible sur votre système."

    # Demander à l'utilisateur de saisir un nom de domaine
    domain = input("Entrez un nom de domaine ou une IP: ")

    # Obtenir les informations WHOIS du nom de domaine
    whois_info = get_whois_info(domain)

    # Générer le nom de fichier
    filename = f"{domain}_whois.txt"
    count = 1
    while os.path.exists(filename):
        filename = f"{domain}_whois_{count}.txt"
        count += 1

    # Enregistrer les informations WHOIS dans un fichier
    with open(filename, "w") as file:
        file.write(whois_info)

    print(f"Les informations WHOIS ont été enregistrées dans le fichier {filename}.")
