from flask import jsonify, request
from datetime import datetime
import psycopg2
from .utilsEndpoints import getOrCreateWritterId

def writer_endpoints(app, r, conn):

    @app.route('/writers', methods=['POST'])
    def post_writer():
        cursor = conn.cursor()
        try:
            body = request.get_json()
            title = body["title"]
            name = body["name"]
            pseudo = body["pseudo"]

            cursor.execute('SELECT * FROM writer WHERE pseudo = %s;', (pseudo,))
            writter = cursor.fetchone()
            if writter:
                cursor.close()
                return jsonify({'failure': f'{pseudo} already exist'}), 200
            
            cursor.execute('INSERT INTO writer (title, name, pseudo) VALUES (%s,%s,%s) RETURNING id;', (title, name, pseudo,))
            writter_id = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            return jsonify({'sucess': f"id = {writter_id}"})
        
        except psycopg2.Error as e:
            cursor.close()
            return jsonify({'error': f'Failed to post new writer: {e}'}), 500
    
    @app.route('/writers', methods=['PATCH'])
    def put_writer():
        cursor = conn.cursor()
        try:
            username = request.headers.get('X-Remote-User')
            id = getOrCreateWritterId(username, app, r, conn)

            cursor.execute('SELECT * FROM writer WHERE id = %s;', (id,))
            writer = cursor.fetchone()
            
            body = request.get_json()
            title = body["title"] if body["title"] != None else writer[1]
            pseudo = body["pseudo"] if body["pseudo"] != None else writer[2]

            cursor.execute('UPDATE writer SET title = %s, pseudo = %s where id = %s;', (title, pseudo, writer[0],))
            conn.commit()
            cursor.close()
            return jsonify({'success': f'Update writer {writer[0]}'}), 200

        except psycopg2.Error as e:
            cursor.close()
            return jsonify({'error': f'Failed to post new writer: {e}'}), 500
