# import os
# import sys
# import logging


# # Format appliqué à chaque message de log
# logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"

# # Dossier dans lequel les logs seront enregistrés
# log_dir = "logs"

# # Chemin complet du fichier de logs
# log_file = os.path.join(log_dir, "running_logs.log")

# # Création du dossier "logs" s’il n’existe pas
# os.makedirs(log_dir, exist_ok=True)


# # Configuration générale du système de logging
# logging.basicConfig(
#     level=logging.INFO,
#     format=logging_str,

#     # Les handlers indiquent où envoyer les messages
#     handlers=[
#         # Enregistre les logs dans un fichier
#         logging.FileHandler(
#             log_file,
#             mode="a",          # Ajoute les nouveaux logs sans effacer les anciens
#             encoding="utf-8"
#         ),

#         # Affiche également les logs dans le terminal
#         logging.StreamHandler(sys.stdout)
#     ]
# )


# # Création d’un logger personnalisé pour le projet
# logger = logging.getLogger(
#     "CNNClassifierLogger"
# )
# # logger.info("Le programme a démarré.")
# # logger.warning("Une valeur inhabituelle a été détectée.")
# # logger.error("Une erreur est survenue.")

import sys
import logging
from pathlib import Path


# Format des messages
logging_format = (
    "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
)

# Création du dossier des logs
log_dir = Path("logs")
log_dir.mkdir(parents=True, exist_ok=True)

# Chemin du fichier de logs
log_file = log_dir / "running_logs.log"

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_format,
    handlers=[
        logging.FileHandler(
            log_file,
            mode="a",
            encoding="utf-8"
        ),
        logging.StreamHandler(sys.stdout)
    ]
)

# Logger importé par main.py
logger = logging.getLogger("CNNClassifierLogger")