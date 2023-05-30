from flask import jsonify, request
from datetime import datetime
import psycopg2

def getOrCreateWritterId(username, app, r, conn):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM writer WHERE name = %s;', (username,))
        writter = cursor.fetchone()
        if writter:
            return writter[0]
        else:
            try:
                r.publish('new_user', username)
                cursor.execute('INSERT INTO writer (name,pseudo) VALUES (%s,%s) RETURNING id;', (username,username))
                writter_id = cursor.fetchone()[0]
                conn.commit()
                cursor.close()
                return writter_id
            except psycopg2.Error as e:
                return 0