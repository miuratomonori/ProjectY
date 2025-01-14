import mysql.connector as mydb
import sys

if len(sys.argv) < 2:
    print("Error: studentId is required as an argument.")
    sys.exit(1)

student_id = sys.argv[1]

try:
    conn = mydb.connect(
        host='localhost',
        user='ncc',
        password='ncc',
        database='sample'
    )
    cursor = conn.cursor()

    # データ挿入のSQL
    insert_sql = '''
    INSERT INTO attendance (studentId, subject, status)
    VALUES (%s, %s, %s)
    '''
    insert_data = (student_id, "算数", "1")
    
    cursor.execute(insert_sql, insert_data)
    conn.commit()

    print(f"Record inserted: {insert_data}")

except mydb.Error as e:
    print(f"Database error: {e}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
