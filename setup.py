import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="kidney-disease-classification",
    version="0.1.0",
    author="Ly Amadou",
    author_email="amzoly.lionpanjshir@gmail.com",
    description="A simple kidney disease classification model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LIONPANJSHIR/kidney-Disease-Classification-MLflow-DVC.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)