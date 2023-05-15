from flask import jsonify, request
from datetime import datetime
import psycopg2

def circles_endpoints(app, r, conn):
    # Route pour obtenir toutes les lettres
    @app.route('/circles', methods=['GET'])
    def get_circles():
        #get the username with keycloak (Oidc-Claim-Preferred-Username)
        username = request.headers.get('X-Remote-User')

        r.publish('my-channel', username)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM circle;')
        circles = cursor.fetchall()
        cursor.close()
        return jsonify(circles)
    
    # Route pour mettre à jour une lettre par ID
    @app.route('/circles/<int:id>', methods=['POST'])
    def update_circle(id):
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
                'INSERT INTO circle (circleId, writerId, postAt, content, subject) VALUES (%s, %s, %s, %s, %s) RETURNING id;',
                (circleid, writerid, postAt, content, subject)
            )

            # Récupération de l'ID généré pour la nouvelle lettre
            circle_id = cursor.fetchone()[0]

            # Validation de la transaction et fermeture du curseur
            conn.commit()
            cursor.close()

            return jsonify({'message': f'circle created successfully with ID {circle_id}'}), 201
        except psycopg2.Error as e:
            conn.rollback()
            cursor.close()
            return jsonify({'error': f'Failed to create circle: {e}'}), 500
        
