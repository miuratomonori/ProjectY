import mysql.connector as mydb
import pandas as pd

# MySQL接続設定
conn = None

try:
    # コネクションの作成
    conn = mydb.connect(
        host='localhost',
        port='3306',
        user='ncc',
        password='ncc',
        database='sample'
    )

    cursor = conn.cursor()  # カーソルオブジェクトを作成

    # `student` と `attendance` を結合してデータを取得
    select_sql = '''
    SELECT 
        s.studentId, 
        s.studentNo, 
        s.studentName, 
        a.subject, 
        a.status
    FROM 
        student s
    LEFT JOIN 
        attendance a
    ON 
        s.studentId = a.studentId
    '''
    cursor.execute(select_sql)

    # フェッチしてDataFrameに変換
    columns = [col[0] for col in cursor.description]  # カラム名を取得
    rows = cursor.fetchall()  # 全てのデータを取得
    result_df = pd.DataFrame(rows, columns=columns)  # pandas DataFrameに変換

    # ターミナルにデータを表示
    print("Fetched Data:")
    print(result_df)

    # データをExcelファイルに書き込み
    output_file = 'syusseki.xlsx'
    result_df.to_excel(output_file, index=False, engine='openpyxl')
    print(f"データを {output_file} に書き込みました。")

    cursor.close()

except Exception as e:
    print(f"Error Occurred: {e}")

finally:
    if conn is not None and conn.is_connected():
        conn.close()
