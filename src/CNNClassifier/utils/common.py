# Module utilisé pour créer des dossiers et récupérer la taille des fichiers
import os

# Module utilisé pour lire et écrire des fichiers JSON
import json

# Module utilisé pour lire les fichiers YAML
import yaml

# Bibliothèque permettant de sauvegarder et charger des objets Python
import joblib

# Module utilisé pour convertir des images en Base64 et inversement
import base64

# Type générique représentant n’importe quel type d’objet Python
from typing import Any

# Classe moderne pour manipuler les chemins de fichiers
from pathlib import Path

# Exception générée par ConfigBox lorsqu’une valeur est incorrecte
from box.exceptions import BoxValueError

# Transforme un dictionnaire en objet accessible avec une notation par points
from box import ConfigBox

# Décorateur vérifiant les annotations de types pendant l’exécution
from ensure import ensure_annotations

# Logger personnalisé du projet
from CNNClassifier import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Lit un fichier YAML et retourne son contenu sous forme de ConfigBox.

    Args:
        path_to_yaml: chemin du fichier YAML.

    Returns:
        Contenu du fichier sous forme de ConfigBox.

    Raises:
        BoxValueError: si le fichier YAML est vide.
        Exception: si le fichier est introuvable ou invalide.
    """
    try:
        # Ouvre le fichier YAML en lecture
        with path_to_yaml.open(
            mode="r",
            encoding="utf-8"
        ) as yaml_file:

            # Transforme le contenu YAML en dictionnaire Python
            content = yaml.safe_load(yaml_file)

        # yaml.safe_load retourne None lorsque le fichier est vide
        if content is None:
            raise BoxValueError(
                f"Le fichier YAML est vide : {path_to_yaml}"
            )

        logger.info(
            "Fichier YAML chargé avec succès : %s",
            path_to_yaml
        )

        # Convertit le dictionnaire en ConfigBox
        # Exemple : config.data.root_dir
        return ConfigBox(content)

    except BoxValueError:
        # Enregistre l’erreur puis la transmet au programme appelant
        logger.exception(
            "Le fichier YAML est vide : %s",
            path_to_yaml
        )
        raise

    except Exception:
        # logger.exception enregistre également la traceback
        logger.exception(
            "Impossible de charger le fichier YAML : %s",
            path_to_yaml
        )
        raise


@ensure_annotations
def create_directories(
    path_to_directories: list,
    verbose: bool = True
) -> None:
    """
    Crée les dossiers indiqués dans une liste.

    Args:
        path_to_directories: liste des chemins à créer.
        verbose: active l’affichage des logs si True.
    """
    for directory_path in path_to_directories:

        # parents=True crée également les dossiers parents manquants
        # exist_ok=True évite une erreur si le dossier existe déjà
        Path(directory_path).mkdir(
            parents=True,
            exist_ok=True
        )

        if verbose:
            logger.info(
                "Dossier créé ou déjà existant : %s",
                directory_path
            )


@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """
    Enregistre un dictionnaire dans un fichier JSON.

    Args:
        path: emplacement du fichier JSON.
        data: dictionnaire à enregistrer.
    """
    try:
        # Crée le dossier parent s’il n’existe pas
        path.parent.mkdir(parents=True, exist_ok=True)

        # Ouvre le fichier en écriture
        with path.open(
            mode="w",
            encoding="utf-8"
        ) as json_file:

            # indent=4 produit un fichier lisible
            # ensure_ascii=False conserve correctement les accents
            json.dump(
                data,
                json_file,
                indent=4,
                ensure_ascii=False
            )

        logger.info(
            "Fichier JSON enregistré : %s",
            path
        )

    except Exception:
        logger.exception(
            "Impossible d’enregistrer le fichier JSON : %s",
            path
        )
        raise


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Charge un fichier JSON et retourne son contenu sous forme de ConfigBox.

    Args:
        path: chemin du fichier JSON.

    Returns:
        Contenu du fichier sous forme de ConfigBox.
    """
    try:
        # Ouvre le fichier JSON en lecture
        with path.open(
            mode="r",
            encoding="utf-8"
        ) as json_file:
            json_data = json.load(json_file)

        logger.info(
            "Fichier JSON chargé avec succès : %s",
            path
        )

        # Permet l’accès aux valeurs avec la notation par points
        return ConfigBox(json_data)

    except Exception:
        logger.exception(
            "Impossible de charger le fichier JSON : %s",
            path
        )
        raise


@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """
    Sauvegarde un objet Python dans un fichier binaire avec Joblib.

    Args:
        data: objet à sauvegarder, par exemple un modèle ML.
        path: chemin du fichier de sauvegarde.
    """
    try:
        # Crée le dossier parent si nécessaire
        path.parent.mkdir(parents=True, exist_ok=True)

        # Sérialise l’objet dans un fichier
        joblib.dump(data, path)

        logger.info(
            "Objet binaire sauvegardé : %s",
            path
        )

    except Exception:
        logger.exception(
            "Impossible de sauvegarder l’objet : %s",
            path
        )
        raise


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Charge un objet Python sauvegardé avec Joblib.

    Args:
        path: chemin du fichier binaire.

    Returns:
        Objet Python chargé depuis le fichier.
    """
    try:
        # Désérialise le contenu du fichier
        data = joblib.load(path)

        logger.info(
            "Objet binaire chargé avec succès : %s",
            path
        )

        return data

    except Exception:
        logger.exception(
            "Impossible de charger l’objet : %s",
            path
        )
        raise


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Retourne la taille d’un fichier en kilo-octets.

    Args:
        path: chemin du fichier.

    Returns:
        Taille formatée, par exemple « 125 KB ».
    """
    try:
        # Récupère la taille en octets puis la convertit en kilo-octets
        size_in_kb = round(path.stat().st_size / 1024)

        logger.info(
            "Taille du fichier %s : %s KB",
            path,
            size_in_kb
        )

        return f"{size_in_kb} KB"

    except Exception:
        logger.exception(
            "Impossible de récupérer la taille du fichier : %s",
            path
        )
        raise


def decode_image(
    image_string: str,
    filename: Path
) -> None:
    """
    Décode une chaîne Base64 et crée un fichier image.

    Args:
        image_string: image encodée en Base64.
        filename: chemin de destination de l’image.
    """
    try:
        # Convertit la chaîne Base64 en données binaires
        image_data = base64.b64decode(image_string)

        # Crée le dossier parent si nécessaire
        filename.parent.mkdir(parents=True, exist_ok=True)

        # Enregistre les données binaires dans un fichier image
        with filename.open(mode="wb") as image_file:
            image_file.write(image_data)

        logger.info(
            "Image Base64 décodée et enregistrée : %s",
            filename
        )

    except Exception:
        logger.exception(
            "Impossible de décoder l’image : %s",
            filename
        )
        raise


@ensure_annotations
def encode_image_into_base64(image_path: Path) -> str:
    """
    Encode une image sous forme de chaîne Base64.

    Args:
        image_path: chemin du fichier image.

    Returns:
        Image encodée sous forme de chaîne Base64.
    """
    try:
        # Ouvre l’image en mode binaire
        with image_path.open(mode="rb") as image_file:

            # Lit l’image et la transforme en Base64
            encoded_bytes = base64.b64encode(
                image_file.read()
            )

        # Convertit les données binaires Base64 en chaîne UTF-8
        encoded_string = encoded_bytes.decode("utf-8")

        logger.info(
            "Image encodée en Base64 : %s",
            image_path
        )

        return encoded_string

    except Exception:
        logger.exception(
            "Impossible d’encoder l’image : %s",
            image_path
        )
        raise