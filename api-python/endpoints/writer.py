from flask import jsonify, request
from datetime import datetime
import psycopg2

def writer_endpoints(app, r, conn):

    def getWriterID(username):
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM writer WHERE pseudo = %s;', (username,))
            writter = cursor.fetchone()
            cursor.close()
            if writter:
                return writter[0]
            else:
                return None
        except psycopg2.Error as _:
            return 
        
    # username = request.headers.get('X-Remote-User')
    # id = getOrCreateWritterId(username)
        
    # Endpoints functions
    @app.route('/writer', methods=['GET'])
    def get_writers():
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM writer;')
            writer = cursor.fetchall()
            cursor.close()
            return jsonify(writer), 200
        except psycopg2.Error as e:
            cursor.close()
            return jsonify({'error': f'Failed to get writers: {e}'}), 500
    
    
    @app.route('/writer/<int:id>', methods=['GET'])
    def get_writer_by_id(id):
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM writer WHERE id = %s;', (id,))
            writer = cursor.fetchone()
            cursor.close()
            if writer:
                return jsonify(writer), 200
            else:
                return jsonify({'error': 'writer not found'}), 404
        except psycopg2.Error as e:
            cursor.close()
            return jsonify({'error': f'Failed to get writer: {e}'}), 500
            
    
    @app.route('/writer', methods=['POST'])
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
            cursor.close()
            return jsonify({"json", f"ify {str(writter_id)}"}), 200
        except psycopg2.Error as e:
            cursor.close()
            return jsonify({'error', f'Failed to post new writer: {e}'}), 500
    
    @app.route('/writer', methods=['PUT'])
    def put_writer():
        cursor = conn.cursor()
        username = "Adrien-Elek"
        # username = request.headers.get('X-Remote-User')
        try:
            cursor.execute('SELECT * FROM writer WHERE pseudo = %s;', (username,))
            writer = cursor.fetchone()
            if not writer:
                cursor.close()
                return jsonify({'error': f'Invalid User {username}'}), 200
            
            body = request.get_json()
            title = body["title"] if body["title"] != None else writer[1]
            name = body["name"] if body["name"] != None else writer[2]
            pseudo = body["pseudo"] if body["pseudo"] != None else writer[3]

            cursor.execute('UPDATE writer SET title = %s, name = %s, pseudo = %s where id = %s;', (title, name, pseudo, writer[0],))
            cursor.close()
            return jsonify({'success': f'Update writer {writer[0]}'}), 200

        except psycopg2.Error as e:
            cursor.close()
            return jsonify({'error': f'Failed to post new writer: {e}'}), 500
    
    @app.route('/writer/<int:id>', methods=['DELETE'])
    def delete_writer(id):
        cursor = conn.cursor()
        # username = request.headers.get('X-Remote-User')
        try:
            cursor.execute('SELECT * FROM writer WHERE id = %s;', (id,))
            writer = cursor.fetchone()
            if not writer:
                cursor.close()
                return jsonify({'error': f'Invalid User with id: {id}'}), 200

            cursor.execute('DELETE FROM writer WHERE id = %s;', (id,))
            cursor.execute('DELETE FROM writerCircle WHERE writerId = %s;', (id,))

            cursor.close()
            return jsonify({'success': f'Deleted writer {writer[0]}'}), 200

        except psycopg2.Error as e:
            cursor.close()
            return jsonify({'error': f'Failed to delete writer: {e}'}), 500