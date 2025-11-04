"""
Chapter2 Flaskで問い合わせ(Ajax)
         PyScriptを使用
"""
from flask import Flask, request, render_template
import ollama

# Flaskアプリケーションの作成
app = Flask(__name__)
# Ollamaのクライアントの作成
client = ollama.Client()
client_model = "llama3.2" # 使用するモデルの指定

# ルートURLにアクセスしたときの処理
@app.route('/')
def index():
    """
    ルートアクセス
    """
    # HTMLテンプレートをレンダリング
    return render_template("index.html")

# Ajaxリクエストを処理する。
@app.route('/api/make_summary', methods=['POST'])
def api_summary():
    """
    要約作成API
    """
    # Ajaxリクエストか(application\json)からテキストを取得
    text = request.json.get("text")

    # Ollamaにアクセスして要約を生成
    prompt = f"次の文章を1文で要約してください。:\n\n{text}"
    response = client.generate(model=client_model, prompt=prompt)
    summary = response['response']
    # JSON形式で要約を返す
    return {"result": summary}

if __name__ == '__main__':
    app.run(debug=True)
