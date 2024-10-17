# Utiliser une image officielle Python comme image parent
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le code de l'application dans le conteneur
COPY . /app

# Installer les dépendances requises
RUN pip install --no-cache-dir flask pycryptodome

# Exposer le port 5000 au monde extérieur
EXPOSE 5000

# Lancer le serveur Flask
CMD ["python", "schnorr_server_vuln.py"]