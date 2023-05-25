from flask import jsonify, request
from datetime import datetime
import psycopg2
from .utilsEndpoints import getOrCreateWritterId

def circles_endpoints(app, r, conn):

    # Create a new circle
    @app.route('/circles', methods=['POST'])
    def create_circle():
        cursor = conn.cursor()

        try:
            name = request.json['name']
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
    
    # Join a new circle
    @app.route('/circles/<int:id>/join', methods=['POST'])
    def join_circle(id):
        cursor = conn.cursor()
        try:
            username = request.headers.get('X-Remote-User')
            userId = getOrCreateWritterId(username, app, conn)
            cursor.execute('INSERT INTO \"writerCircle\" VALUES (%s, %s);', (id, userId,))
            conn.commit()
            cursor.close()
            return jsonify({'sucess': f'Sucess in joining circle with id {id}'})
        
        except psycopg2.Error as e:
            conn.rollback()
            cursor.close()
            return jsonify({'error': f'Failed to join circle: {e}; id = {id}, userId = {userId}'}), 500
        
    # Quit a circle
    @app.route('/circles/<int:id>/quit', methods=['PUT'])
    def quit_circle(id):
        cursor = conn.cursor()
        try:
            username = request.headers.get('X-Remote-User')
            userId = getOrCreateWritterId(username, app, conn)
            cursor.execute('DELETE FROM \"writerCircle\" WHERE \"circleId\" = %s AND \"writerId\" = %s;', (id, userId,))
            conn.commit()
            cursor.close()

            return jsonify({'sucess': f'Sucess in quiting circle with id {id}'})
        
        except psycopg2.Error as e:
            conn.rollback()
            cursor.close()
            return jsonify({'error': f'Failed to quit circle: {e}'}), 500
