"""
Chapter2 WebSocketを使用したチャットツール
"""
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import ollama

# Flaskアプリケーション、Socket.IOの初期化
app = Flask(__name__)
app.config["SECRET_KEY"] = "C0HTSwr" # 暗号キーを指定
socketio = SocketIO(app)

# Ollamaのクライアントの作成
client = ollama.Client()
client_model = "llama3.2" # 使用するモデルの指定

# Flaskへのアクセス
@app.route('/', methods=['GET'])
def index():
    """
    ルートアクセス
    """
    return render_template("index.html")

# Socket.IOのイベント
@socketio.on("user_message")
def handle_message(data):
    """
    ユーザーからのメッセージ処理
    """
    message = data["message"]
    print("[User]", message)

    # LLMにメッセージを送信
    response = client.generate(
        model=client_model,
        prompt=message)
    if "response" in response:
        response = response["response"]
        print("[Ollama]", response)
        # レスポンスをクライアントに送信
        emit("bot_response", {"message": response})

if __name__ == '__main__':
    socketio.run(app, debug=True)
