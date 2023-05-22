from flask import jsonify, request
from datetime import datetime
import psycopg2

def letter_endpoints(app, r, conn):

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
        
    @app.route('/letter/<int:id>', methods=['GET'])
    def get_letter(id):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM letter WHERE \"circleId\" = %s;', (id,))
        letters = cursor.fetchall()
        cursor.close()
        return jsonify(letters)


    @app.route('/letter', methods=['POST'])
    def post_letter():
        cursor = conn.cursor()
        
        username = request.headers.get('X-Remote-User')
        writerId = getOrCreateWritterId(username)

        circleId = request.json['circleid']
        postAt = updatedAt = datetime.now()
        content = request.json['content']
        subject = request.json['subject']

        try:
            cursor.execute('SELECT * FROM \"writerCircle\" WHERE \"writerId\" = %s AND \"circleId\" = %s;', (writerId, circleId,))
            res = cursor.fetchone()

            if not res:
                cursor.close()
                return jsonify("error", "you cannot post in this circle")

            cursor.execute(
                'INSERT INTO letter (\"circleId\", \"writerId\", \"postAt\", \"updatedAt\", content, subject) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;',
                (circleId, writerId, postAt, updatedAt, content, subject,)
            )

            letter_id = cursor.fetchone()[0]
            cursor.close()

            return jsonify({'message': f'letter posted successfully with ID {letter_id}'}), 201
        except psycopg2.Error as e:
            conn.rollback()
            cursor.close()
            return jsonify({'error': f'Failed to publish letter: {e}'}), 500
        
    
    @app.route('/letter/<int:id>', methods=['PATCH'])
    def put_letter(id):
        username = request.headers.get('X-Remote-User')
        writerId = getOrCreateWritterId(username)

        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM letter WHERE id = %s;', (id,))
            letter = cursor.fetchone()
            if letter[2] != writerId:
                cursor.close()
                return jsonify({'message': f'you cannot edit a letter you did not post'}), 400
            
            updatedAt = datetime.now()
            content = request.json['content']
            subject = request.json['subject']

            cursor.execute(
                'UPDATE letter SET \"updatedAt\" = %s, content = %s, subject = %s WHERE id = %s RETURNING id;',
                (updatedAt, content, subject, id)
            )
            letter_id = cursor.fetchone()[0]
            conn.commit()
            cursor.close()

            return jsonify({'message': f'letter modified successfully with ID {letter_id}'}), 200
            
        except psycopg2.Error as e:
            conn.rollback()
            cursor.close()
            return jsonify({'error': f'Failed to modify letter: {e}'}), 500
    
    @app.route('/letter/<int:id>', methods=['DELETE'])
    def delete_letter(id):
        username = request.headers.get('X-Remote-User')
        writerId = getOrCreateWritterId(username)

        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM letter WHERE id = %s;', (id,))
            letter = cursor.fetchone()
            if letter[2] != writerId:
                cursor.close()
                return jsonify({'message': f'you cannot edit a letter you did not post'}), 400
            cursor.execute('DELETE FROM letter WHERE id = %s;', (id,))

            # message with id 0 as "This message was deleted"? 
            cursor.execute('UPDATE letter SET \"replyId\" = 0 WHERE \"replyId\" = %s;', (id,))
            conn.commit()
            cursor.close()

            return jsonify({"sucess": f"sucessfully deleted letter with id = {id}"})
        
        except psycopg2.Error as e:
            return jsonify({'error': f'Failed to modify letter: {e}'}), 500
            
    @app.route('/letter/reply/<int:id>', methods=['POST'])
    def reply_to_letter(id):
        cursor = conn.cursor()
        
        username = request.headers.get('X-Remote-User')
        writerId = getOrCreateWritterId(username)

        circleId = request.json['circleid']
        postAt = updatedAt = datetime.now()
        content = request.json['content']
        subject = request.json['subject']

        try:
            cursor.execute('SELECT * FROM \"writerCircle\" WHERE \"writerId\" = %s AND \"circleId\" = %s;', (writerId, circleId,))
            res = cursor.fetchone()

            if not res:
                cursor.close()
                return jsonify("error", "you cannot post in this circle")

            cursor.execute(
                'INSERT INTO letter (\"circleId\", \"writerId\", \"postAt\", \"updatedAt\", content, subject, \"replyId\") VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id;',
                (circleId, writerId, postAt, updatedAt, content, subject, id)
            )

            letter_id = cursor.fetchone()[0]
            cursor.close()

            return jsonify({'message': f'letter posted successfully with ID {letter_id}'}), 201
        except psycopg2.Error as e:
            conn.rollback()
            cursor.close()
            return jsonify({'error': f'Failed to publish letter: {e}'}), 500