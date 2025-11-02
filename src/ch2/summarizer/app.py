"""
Chapter2 Flaskで問い合わせ
"""
from flask import Flask, request, render_template
import ollama

# Flaskアプリケーションの作成
app = Flask(__name__)
# Ollamaのクライアントの作成
client = ollama.Client()
client_model = "llama3.2" # 使用するモデルの指定

# ルートURLにアクセスしたときの処理
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    ルートアクセス
    """
    summary = None
    original_text = ""
    # POSTリクエストが送信されたときの処理
    if request.method == 'POST':
        # フォームから送信されたテキストを取得
        original_text = request.form['text']
        # Ollamaにアクセスして要約を生成
        prompt = f"次の文章を1文で要約してください。:\n\n{original_text}"
        response = client.generate(model=client_model, prompt=prompt)
        summary = response['response']
    # HTMLテンプレートをレンダリング
    return render_template('index.html', summary=summary, text=original_text)

if __name__ == '__main__':
    app.run(debug=True)
