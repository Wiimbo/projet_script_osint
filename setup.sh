#!/bin/bash

# Vérifier si git est installé
if ! command -v git &> /dev/null; then
    echo "Installation de git..."
    sudo apt-get update
    sudo apt-get install -y git
    echo "Installation de git terminée."
fi

# Vérifier si python3 est installé
if ! command -v python3 &> /dev/null; then
    echo "Installation de python3..."
    sudo apt-get update
    sudo apt-get install -y python3
    echo "Installation de python3 terminée."
fi

# Vérifier si pip est installé
if ! command -v pip &> /dev/null; then
    echo "Installation de pip..."
    sudo apt-get update
    sudo apt-get install -y python3-pip
    echo "Installation de pip terminée."
fi

# Vérifier si nmap est installé
if ! command -v nmap &> /dev/null; then
    echo "Installation de nmap..."
    sudo apt-get update
    sudo apt-get install -y nmap
    echo "Installation de nmap terminée."
fi

# Vérifier si shodan est installé
if ! python3 -c "import shodan" &> /dev/null; then
    echo "Installation de shodan..."
    sudo pip install shodan
    echo "Installation de shodan terminée."
fi

# Vérifier si whois est installé
if ! command -v whois &> /dev/null; then
    echo "Installation de whois..."
    sudo apt-get update
    sudo apt-get install -y whois
    echo "Installation de whois terminée."

echo "Installation de theHarvester terminée."
