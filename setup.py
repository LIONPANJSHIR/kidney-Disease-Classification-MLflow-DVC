import setuptools


# Lecture du README pour l’utiliser comme description détaillée du projet
with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()


# Nom du package Python situé dans le dossier src/
SRC_REPO = "CNNClassifier"

# Nom du dépôt GitHub
REPO_NAME = "kidney-Disease-Classification-MLflow-DVC"

# Nom d’utilisateur GitHub
AUTHOR_USERNAME = "LIONPANJSHIR"


setuptools.setup(
    # Nom du projet lors de son installation avec pip
    name=SRC_REPO,

    # Version actuelle du projet
    version="0.0.0",

    # Informations sur l’auteur
    author="Ly Amadou",
    author_email="amzoly.lionpanjshir@gmail.com",

    # Description courte du projet
    description="A kidney disease classification project using CNN, MLflow and DVC",

    # Description détaillée récupérée depuis README.md
    long_description=long_description,
    long_description_content_type="text/markdown",

    # Adresse du dépôt GitHub
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",

    # Indique que les packages Python se trouvent dans src/
    package_dir={"": "src"},

    # Recherche automatiquement les packages contenant un __init__.py
    packages=setuptools.find_packages(where="src"),

    # Informations utilisées pour classifier le projet
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    # Versions de Python compatibles avec TensorFlow 2.12
    python_requires=">=3.8,<3.12",
)