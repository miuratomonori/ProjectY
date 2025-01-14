import os
from flask import Flask, render_template, jsonify, request
from readqr import read_qr_code
import subprocess

app = Flask(__name__)

@app.route("/read_qr", methods=["GET"])
def read_qr():
    subject = request.args.get('subject', 'kokugo')
    qr_data = read_qr_code(return_type=False)
    print(f"読み取ったQRコードのデータ: {qr_data}")  # デバッグ用

    if qr_data:
        try:
            # スクリプトの絶対パスを指定
            base_path = os.path.dirname(os.path.abspath(__file__))
            if subject == "kokugo":
                script_path = os.path.join(base_path, "attendance_kokugo.py")
            elif subject == "sannsuu":
                script_path = os.path.join(base_path, "attendance_sannsuu.py")
            else:
                return jsonify({'status': 'error', 'message': 'Invalid subject'})

            # スクリプトを実行
            subprocess.run(["python", script_path, qr_data], check=True)
            return jsonify({'status': 'success', 'qr_data': qr_data})
        except subprocess.CalledProcessError as e:
            print(f"スクリプトの実行中にエラーが発生しました: {e}")
            return jsonify({'status': 'error', 'message': 'スクリプト実行エラー'})
    else:
        return jsonify({'status': 'error', 'message': 'QRコードが読み取れませんでした'})

@app.route("/")
def index():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)
