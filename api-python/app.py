from flask import Flask, jsonify, request, render_template
import psycopg2
import redis


if __name__ == '__main__':
    try:
        import endpoints.circles as circles
        import endpoints.writers as writers
        import endpoints.letters as letters
    except ImportError as e:
        raise Exception(__name__) from e
    
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

    circles.circles_endpoints(app, r, conn)
    writers.writer_endpoints(app, r, conn)
    len.letter_endpoints(app, r, conn)
    
    app.run(debug=True, host='0.0.0.0', port=5001)
