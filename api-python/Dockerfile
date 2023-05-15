# Utilisez une image de base Python
FROM python:3.8-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Expose le port sur lequel l'application écoutera
COPY app.py .
COPY templates ./templates
COPY endpoints ./endpoints
EXPOSE 5001

# Démarre l'application Flask
CMD ["python", "app.py"]
