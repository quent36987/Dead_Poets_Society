# Utilisez une image de base Python
FROM python:3.8-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers de l'application dans le conteneur
# Installe les dépendances de l'application
#requitements.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Expose le port sur lequel l'application écoutera
COPY app.py .
EXPOSE 5001

# Démarre l'application Flask
CMD ["python", "app.py"]
