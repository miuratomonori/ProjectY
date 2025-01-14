from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# データベースの初期化（サンプルデータ挿入）
def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            name TEXT NOT NULL,
            student_id TEXT NOT NULL UNIQUE,
            registration_number TEXT NOT NULL,
            major TEXT NOT NULL,
            subject TEXT NOT NULL,
            attendance_count INTEGER NOT NULL,
            absence_count INTEGER NOT NULL
        )
    ''')
    # サンプルデータ
    students = [
        ("Alice", "202301", "REG123", "Computer Science", "Mathematics", 10, 2),
        ("Bob", "202302", "REG124", "Electrical Engineering", "Physics", 8, 4),
        ("Charlie", "202303", "REG125", "Mechanical Engineering", "Chemistry", 12, 0),
        ("Diana", "202304", "REG126", "Mathematics", "Biology", 9, 3),
    ]
    c.executemany("INSERT OR IGNORE INTO students (name, student_id, registration_number, major, subject, attendance_count, absence_count) VALUES (?, ?, ?, ?, ?, ?, ?)", students)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/get_data", methods=["GET"])
def get_data():
    filter_name = request.args.get("filter_name", "")
    filter_subject = request.args.get("filter_subject", "")
    filter_student_id = request.args.get("filter_student_id", "")
    filter_major = request.args.get("filter_major", "")

    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    # フィルタリング条件を構築
    query = "SELECT * FROM students WHERE 1=1"
    params = []

    if filter_name:
        query += " AND name LIKE ?"
        params.append(f"%{filter_name}%")
    if filter_subject:
        query += " AND subject LIKE ?"
        params.append(f"%{filter_subject}%")
    if filter_student_id:
        query += " AND student_id = ?"
        params.append(filter_student_id)
    if filter_major:
        query += " AND major LIKE ?"
        params.append(f"%{filter_major}%")

    c.execute(query, params)
    data = [{"name": row[0], "student_id": row[1], "registration_number": row[2], "major": row[3], "subject": row[4], "attendance_count": row[5], "absence_count": row[6]} for row in c.fetchall()]
    conn.close()

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
