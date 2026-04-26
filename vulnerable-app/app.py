from flask import Flask, request
import sqlite3
import os
import subprocess

app = Flask(__name__)

# Vulnerability 1: Hardcoded Secret
SECRET_KEY = "hardcoded-secret-key-12345"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
DB_PASSWORD = "admin123"

# Setup DB
def init_db():
    conn = sqlite3.connect("users.db")
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    conn.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', 'password123')")
    conn.commit()
    conn.close()

# Vulnerability 2: SQL Injection
@app.route("/user")
def get_user():
    username = request.args.get("username", "")
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    result = conn.execute(query).fetchall()
    return str(result)

# Vulnerability 3: Command Injection
@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    output = os.system("ping -c 1 " + host)
    return str(output)

# Vulnerability 4: Command Injection via subprocess
@app.route("/lookup")
def lookup():
    domain = request.args.get("domain", "")
    result = subprocess.run("nslookup " + domain, shell=True, capture_output=True)
    return result.stdout.decode()

# Vulnerability 5: Eval Injection
@app.route("/calc")
def calc():
    expr = request.args.get("expr", "")
    result = eval(expr)
    return str(result)

# Vulnerability 6: Path Traversal
@app.route("/file")
def read_file():
    filename = request.args.get("name", "")
    with open("/var/www/" + filename) as f:
        return f.read()

# Vulnerability 7: Weak Cryptography
@app.route("/hash")
def hash_password():
    import hashlib
    password = request.args.get("password", "")
    hashed = hashlib.md5(password.encode()).hexdigest()
    return hashed

# Vulnerability 8: Debug Mode Enabled
if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)
