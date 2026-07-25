# Module permettant d’interagir avec le système d’exploitation :
# fichiers, dossiers, variables d’environnement, etc.
import os

# Classe facilitant la manipulation des chemins de fichiers
# de manière compatible avec Windows, Linux et macOS
from pathlib import Path

# Module permettant d’afficher et d’enregistrer des messages
# pendant l’exécution du programme
import logging


# Configuration du système de journalisation (logging)
logging.basicConfig(
    level=logging.INFO,  # Affiche les messages de niveau INFO ou supérieur
    format="%(asctime)s - %(levelname)s - %(message)s"
    # asctime    : date et heure du message
    # levelname  : niveau du message (INFO, WARNING, ERROR...)
    # message    : contenu du message
)


# Nom principal du projet et du package Python
project_name = "CNNClassifier"


# Liste des dossiers et fichiers qui composeront la structure du projet
list_of_files = [

    # Fichier vide permettant à Git de conserver le dossier des workflows
    ".github/workflows/.gitkeep",

    # Initialise le package Python principal
    f"src/{project_name}/__init__.py",

    # Contiendra les composants du projet :
    # ingestion, préparation, entraînement et évaluation
    f"src/{project_name}/components/__init__.py",

    # Contiendra les fonctions utilitaires réutilisables
    f"src/{project_name}/utils/__init__.py",

    # Contiendra la gestion des fichiers de configuration
    f"src/{project_name}/config/__init__.py",

    # Contiendra les pipelines d’entraînement et de prédiction
    f"src/{project_name}/pipeline/__init__.py",

    # Contiendra les classes et structures de configuration
    f"src/{project_name}/entity/__init__.py",

    # Contiendra les constantes globales du projet
    f"src/{project_name}/constants/__init__.py",

    # Configuration générale du projet
    "config/config.yaml",

    # Définition des étapes du pipeline DVC
    "dvc.yaml",

    # Paramètres des modèles et des expérimentations
    "params.yaml",

    # Dépendances Python nécessaires au projet
    "requirements.txt",

    # Configuration de l’installation du projet comme package Python
    "setup.py",

    # Notebook destiné aux essais, recherches et expérimentations
    "research/trials.ipynb",

    # Page HTML utilisée comme interface web du modèle
    "templates/index.html"
]


for path in list_of_files :
    # Crée un objet Path à partir du chemin de fichier
    filepath = Path(path)

    # Vérifie si le fichier ou dossier existe déjà
    filedir, filename = os.path.split(filepath)  # Sépare le chemin en dossier et nom de fichier

    if filedir != "":
        # Crée le dossier s’il n’existe pas déjà
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Le dossier '{filedir}' a été créé avec succès.")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Crée un fichier vide s’il n’existe pas ou s’il est vide
        with open(filepath, "w") as f:
            pass  # Crée un fichier vide
        logging.info(f"Le fichier '{filepath}' a été créé avec succès.")
    else:
        logging.info(f"Le fichier '{filepath}' existe déjà et n’est pas vide.")