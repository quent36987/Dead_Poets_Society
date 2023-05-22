from flask import jsonify, request
from datetime import datetime
import psycopg2

def circles_endpoints(app, r, conn):

    def getOrCreateWritterId(username):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM writer WHERE name = %s;', (username,))
        writter = cursor.fetchone()
        if writter:
            return writter[0]
        else:
            cursor.execute('INSERT INTO writer (name,pseudo) VALUES (%s,%s) RETURNING id;', (username,username))
            writter_id = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            return writter_id
        
    
    # Route pour obtenir toutes les lettres d'un cercle
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
    
    # Create a new circle
    @app.route('/circles', methods=['POST'])
    def create_circle():
        cursor = conn.cursor()

        name = request.json['name']
        try:
            cursor.execute(
                'INSERT INTO circle (name) VALUES (%s) RETURNING id;',
                (name,)
            )
            circle_id = cursor.fetchone()[0]
            conn.commit()
            cursor.close()

            return jsonify({'message': f'circle created successfully with ID {circle_id}'}), 201
        except psycopg2.Error as e:
            conn.rollback()
            cursor.close()
            return jsonify({'error': f'Failed to create circle: {e}'}), 500
    
    # Delete circle with id

    # @app.route('/circles/<int:id>', methods=['DELETE'])
    # def delete_circle(id):
    #     cursor = conn.cursor()

    #     try:
    #         cursor.execute('DELETE FROM circle WHERE id = %s;', (id,))
    #         cursor.execute('DELETE FROM \"writerCircle\" WHERE circleId = %s;', (id,))
    #         cursor.execute('DELETE FROM letter WHERE circleId = %s;', (id,))

    #         # Manque l'update du champ reply pour toutes les lettres qui référence des lettres supprimés
            
    #         conn.commit()
    #         cursor.close()

    #         return jsonify({'message': f'circle deleted successfully with ID {id}'}), 201
    #     except psycopg2.Error as e:
    #         conn.rollback()
    #         cursor.close()
    #         return jsonify({'error': f'Failed to delete circle: {e}'}), 500
    
    # Join a new circle
    @app.route('/circles/<int:id>/join', methods=['POST'])
    def join_circle(id):
        cursor = conn.cursor()
        username = request.headers.get('X-Remote-User')
        try:
            userId = getOrCreateWritterId(username)
            cursor.execute('INSERT INTO \"writerCircle\" VALUES (%s, %s);', (id, userId,))
            conn.commit()
            cursor.close()
            return jsonify({'sucess': f'Sucess in joining circle with id {id}'})
        
        except psycopg2.Error as e:
            conn.rollback()
            cursor.close()
            return jsonify({'error': f'Failed to join circle: {e}; id = {id}, userId = {userId}'}), 500
        
    # Quit a circle
    @app.route('/circles/<int:id>/quit', methods=['PATCH'])
    def quit_circle(id):
        cursor = conn.cursor()
        username = request.headers.get('X-Remote-User')
        try:
            userId = getOrCreateWritterId(username)
            cursor.execute('DELETE FROM \"writerCircle\" WHERE \"circleId\" = %s AND \"writerId\" = %s;', (id, userId,))
            conn.commit()
            cursor.close()
            return jsonify({'sucess': f'Sucess in quiting circle with id {id}'})
        
        except psycopg2.Error as e:
            conn.rollback()
            cursor.close()
            return jsonify({'error': f'Failed to quit circle: {e}'}), 500

        
