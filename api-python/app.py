from flask import Flask, jsonify, request, render_template
import psycopg2
from datetime import datetime
import redis


app = Flask(__name__)

# Configuration de la connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="postgresql",
    port=5432
)
cur = conn.cursor()


r = redis.Redis(
    host='redis',
    port=6379,
    decode_responses=True # <-- this will ensure that binary data is decoded
)


@app.route('/')
def hello():
    return "Hello, Flask Dockerized!"

@app.route('/headers')
def headers():
    return render_template('headers.html',headers=request.headers.items())

# Route pour obtenir toutes les lettres
@app.route('/circles', methods=['GET'])
def get_letters():
     #get the username with keycloak (Oidc-Claim-Preferred-Username)
     username = request.headers.get('Oidc-Claim-Preferred-Username')

     r.publish('my-channel', username)
     cursor = conn.cursor()
     cursor.execute('SELECT * FROM circle;')
     letters = cursor.fetchall()
     cursor.close()
     return jsonify(letters)

# Route pour obtenir la liste des tables existantes
@app.route('/tables', methods=['GET'])
def get_tables():
    cursor = conn.cursor()

    try:
        # Exécution de la requête SQL pour obtenir la liste des tables
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

        # Récupération des noms de tables dans un tuple
        tables = cursor.fetchall()

        # Fermeture du curseur
        cursor.close()

        # Conversion du tuple en une liste de noms de tables
        table_names = [table[0] for table in tables]

        return jsonify({'tables': table_names}), 200
    except psycopg2.Error as e:
        cursor.close()
        return jsonify({'error': f'Failed to get tables: {e}'}), 500

# Route pour obtenir une lettre par ID
@app.route('/letters/<int:id>', methods=['GET'])
def get_letter_by_id(id):
     cursor = conn.cursor()
     cursor.execute('SELECT * FROM letter WHERE id = %s;', (id,))
     letter = cursor.fetchone()
     cursor.close()
     if letter:
         return jsonify(letter)
     else:
         return jsonify({'error': 'Letter not found'})

# Route pour mettre à jour une lettre par ID
@app.route('/circles/<int:id>', methods=['POST'])
def update_letter(id):
    cursor = conn.cursor()

    # Récupération des données envoyées dans le corps de la requête
    circleid = id
    writerid = 1  # Remplacez par la valeur souhaitée pour writerid
    postAt = datetime.now()
    content = request.json['content']
    subject = request.json['subject']

    # Vérification des champs obligatoires
    if circleid is None or content is None or subject is None:
            return jsonify({'error': 'circleid, content, and subject are required fields'}), 400

    try:
        # Exécution de la requête SQL pour insérer la nouvelle lettre
        cursor.execute(
            'INSERT INTO letter (circleId, writerId, postAt, content, subject) VALUES (%s, %s, %s, %s, %s) RETURNING id;',
            (circleid, writerid, postAt, content, subject)
        )

        # Récupération de l'ID généré pour la nouvelle lettre
        letter_id = cursor.fetchone()[0]

        # Validation de la transaction et fermeture du curseur
        conn.commit()
        cursor.close()

        return jsonify({'message': f'Letter created successfully with ID {letter_id}'}), 201
    except psycopg2.Error as e:
        conn.rollback()
        cursor.close()
        return jsonify({'error': f'Failed to create letter: {e}'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
