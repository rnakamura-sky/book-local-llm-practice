"""
Chapter2 WebSocketを使用したチャットツール3
         Streamモードを使用
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
    messages = data["messages"]
    print("[User]", messages)

    # LLMにメッセージを送信
    response = client.chat(
        model=client_model,
        messages=messages,
        stream=True)
    # ストリームモードで逐次受信
    text = ""
    for chunk in response:
        # チャンクを受信したら、クライアントに送信
        if "message" in chunk:
            subtext = chunk["message"]["content"]
            emit("bot_stream", {"message": subtext})
            text += subtext
    # ストリームの終了を通知
    emit("bot_stream_end", {"text": text})
    print("[Bot]", text)

if __name__ == '__main__':
    socketio.run(app, debug=True)
