from flask import Flask, jsonify
from flask_cors import CORS
from db import get_connection

app = Flask(__name__)
CORS(app)


@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "flask-backend"
    })


@app.route("/api/db-health")
def db_health():
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]

        return jsonify({
            "status": "healthy",
            "database": "postgresql",
            "version": version
        })

    except Exception as error:
        return jsonify({
            "status": "unhealthy",
            "database": "postgresql",
            "error": str(error)
        }), 500

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


@app.route("/api/users")
def users():
    return jsonify({
        "users": [
            {
                "id": 1,
                "name": "Admin"
            },
            {
                "id": 2,
                "name": "Developer"
            }
        ]
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
