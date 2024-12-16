from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# データベースの初期化
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    # サンプルユーザー作成
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('test_user', 'password123')")
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    print('test')

    data = request.json
    number = data.get("number")
    password = data.get("passwd")

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (number, password))
    user = c.fetchone()
    conn.close()
    
    if user:
        return jsonify({"success": True, "message": "ログイン成功!"})
    else:
        return jsonify({"success": False, "message": "IDまたはパスワードが間違っています。"})
    

@app.route("/admin")
def dashboard():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)
