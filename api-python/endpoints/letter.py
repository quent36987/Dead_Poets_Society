from flask import jsonify, request
from datetime import datetime
import psycopg2

def letter_endpoints(app, r, conn):
    @app.route('/letter', methods=['GET'])
    def get_letters():

        cursor = conn.cursor()
        cursor.execute('SELECT * FROM letter;')
        letter = cursor.fetchall()
        cursor.close()
        return jsonify(letter)
    
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
    
    @app.route('/letter', methods=['POST'])
    def post_letter():
        cursor = conn.cursor()
        
        writerId = 1
        # r.publish('my-channel', username)

        circleId = request.json['circleid']
        postAt = updateAt = datetime.now()
        content = request.json['content']
        subject = request.json['subject']

        try:
            # Exécution de la requête SQL pour insérer la nouvelle lettre
            cursor.execute(
                'INSERT INTO letter (circleId, writerId, postAt, updateAt, content, subject) VALUES (%s, %s, %s, %s, %s) RETURNING id;',
                (circleId, writerId, postAt, updateAt, content, subject)
            )

            # Récupération de l'ID généré pour la nouvelle lettre
            letter_id = cursor.fetchone()[0]

            # Validation de la transaction et fermeture du curseur
            conn.commit()
            cursor.close()

            return jsonify({'message': f'letter created successfully with ID {letter_id}'}), 201
        except psycopg2.Error as e:
            conn.rollback()
            cursor.close()
            return jsonify({'error': f'Failed to publish letter: {e}'}), 500
        
    
    @app.route('/letter/<int:id>', methods=['PUT'])
    def put_letter():
        return "Not implemented : modify letter"
    
    @app.route('/letter/<int:id>', methods=['DELETE'])
    def delete_letter():
        return "Not implemented : delete letter with id"
    
    @app.route('/letter/reply/<int:id>', methods=['POST'])
    def reply_to_letter():
        return "Not implemented : delete letter with id"