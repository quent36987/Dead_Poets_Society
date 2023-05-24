from flask import Flask, jsonify, request, render_template
import psycopg2
import redis


if __name__ == '__main__':
    try:
        import endpoints.circles as cir
        import endpoints.writer as wr
        import endpoints.letter as le
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

    cir.circles_endpoints(app, r, conn)
    wr.writer_endpoints(app, r, conn)
    le.letter_endpoints(app, r, conn)

    # Route pour obtenir la liste des tables existantes
    @app.route('/tables', methods=['GET'])
    def get_tables():
        cursor = conn.cursor()

        try:
            # Exécution de la requête SQL pour obtenir la liste des tables
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

            # Récupération des noms de tables dans un tuple
            tables = cursor.fetchall()

            # Fermeture du curseur
            cursor.close()

            # Conversion du tuple en une liste de noms de tables
            table_names = [table[0] for table in tables]

            return jsonify({'tables': table_names}), 200
        except psycopg2.Error as e:
            cursor.close()
            return jsonify({'error': f'Failed to get tables: {e}'}), 500
    app.run(debug=True, host='0.0.0.0', port=5001)
