import os
import mysql.connector
from flask import Flask

app = Flask(__name__)

# Get MySQL connection details from environment variables
db_host = os.environ.get("MYSQL_HOST", "localhost")
db_user = os.environ.get("MYSQL_USER", "root")
db_password = os.environ.get("MYSQL_PASSWORD", "")
db_name = os.environ.get("MYSQL_DB", "test")

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        return connection
    except mysql.connector.Error as e:
        print("Database connection failed:", e)
        return None

@app.route('/')
def hello():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return f'Hello from Flask + Gunicorn! MySQL time is: {result[0]}'
    else:
        return 'Hello from Flask + Gunicorn! But MySQL connection failed.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("FLASK_PORT", 8000)))

