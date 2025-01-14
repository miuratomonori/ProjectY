# pip install opencv-python
# OpenCV (Open Source Computer Vision Library) ライブラリを利用
import cv2
# pip install pyzbar 
# pyzbarバーコードやQRコードを読み取り、解析するためのライブラリ
from pyzbar.pyzbar import decode

def read_qr_code(return_type=False):
    """
    PCのカメラを使用してQRコードを読み取り、解析した結果を返す関数。
    
    Args:
        return_type (bool): 読み取り結果にコードのタイプ（形式）も含めるかどうか。デフォルトはFalse。
    
    Returns:
        str: 読み取ったコードのデータ。コードが見つからなかった場合はNoneを返す。
        tuple: (str, str) 読み取ったコードのデータとそのタイプ。return_typeがTrueの場合。
    """

    # カメラのキャプチャを開始
    cap = cv2.VideoCapture(0)
    
    try:
        while True:
            # カメラからフレームを読み込む
            ret, frame = cap.read()
            if not ret:
                continue  # フレームが正しく読み込めなかった場合、次のフレームを読み込む
            
            # コードのデコード
            decoded_objects = decode(frame)
            for obj in decoded_objects:
                # コードタイプも返す場合
                if return_type:
                    return (obj.data.decode('utf-8'), obj.type)
                else:
                    # QRコードのデータのみを返す
                    return obj.data.decode('utf-8')
            
            # フレームを表示（デバッグ用）コメントアウトで表示しなくなります。
            cv2.imshow('Code Reader', frame)
            
            # [ESC] を押すと読み取りを停止
            if cv2.waitKey(1) & 0xFF == 27: # [ESC] キーのASCIIコードは27
                break
            
    finally:
        # カメラのキャプチャを解放
        cap.release()
        # 作成したウィンドウをすべて閉じる
        cv2.destroyAllWindows()

    return None


########################################
# 関数のテスト
if __name__ == "__main__":
    
    # コードのみ読み込み
    print("読み取ったデータ:", read_qr_code())  
    
    # タイプ情報も含めて結果を表示
    # print("読み取ったデータ:", read_qr_code(True))  

