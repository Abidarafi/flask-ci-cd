from flask import Flask
import psycopg2
import os

app = Flask(_name_)

@app.route("/")
def hello():
    # Koneksi PostgreSQL dari Railway
    conn = psycopg2.connect(os.environ.get("DATABASE_URL"))
    cur = conn.cursor()
    cur.execute("SELECT NOW()")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return f"Connected to DB! Current time: {result[0]}"

if _name_ == "_main_":
    app.run(debug=True)