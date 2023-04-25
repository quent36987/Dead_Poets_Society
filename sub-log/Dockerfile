# Utilisez une image de base Python
FROM python:3.8-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Expose le port sur lequel l'application écoutera
COPY app.py .

# Démarre l'application Flask
CMD ["python", "-u", "app.py"]
