from flask import jsonify, request
from datetime import datetime
import psycopg2

def writer_endpoints(app, r, conn):

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
    
    @app.route('/writer', methods=['GET'])
    def get_writer():
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM writer;')
        circles = cursor.fetchall()
        cursor.close()
        return jsonify(circles)

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
            conn.commit()
            cursor.close()
            return jsonify({'sucess': f"id = {writter_id}"})
        
        except psycopg2.Error as e:
            cursor.close()
            return jsonify({'error': f'Failed to post new writer: {e}'}), 500
    
    @app.route('/writer', methods=['PATCH'])
    def put_writer():
        cursor = conn.cursor()
        username = request.headers.get('X-Remote-User')
        id = getOrCreateWritterId(username)
        try:
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
    
    # @app.route('/writer/<int:id>', methods=['DELETE'])
    # def delete_writer(id):
    #     cursor = conn.cursor()
    #     # username = request.headers.get('X-Remote-User')
    #     try:
    #         cursor.execute('SELECT * FROM writer WHERE id = %s;', (id,))
    #         writer = cursor.fetchone()
    #         if not writer:
    #             cursor.close()
    #             return jsonify({'error': f'Invalid User with id: {id}'}), 200

    #         cursor.execute('DELETE FROM writer WHERE id = %s;', (id,))
    #         cursor.execute('DELETE FROM writerCircle WHERE writerId = %s;', (id,))

    #         cursor.close()
    #         return jsonify({'success': f'Deleted writer {writer[0]}'}), 200

    #     except psycopg2.Error as e:
    #         cursor.close()
    #         return jsonify({'error': f'Failed to delete writer: {e}'}), 500