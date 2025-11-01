"""
Chapter2 Ollamaを使う一番簡単なPythonプログラム
    requestsモジュール使用
"""
import requests

# OllamaのAPIエンドポイント
API_ENDOPOINT = "http://localhost:11434"

def generate(prompt, model="llama3.2"):
    """
    /api/generateを呼び出す関数を定義
    """
    # URLを指定
    url = API_ENDOPOINT + "/api/generate"
    # リクエストボディ
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "temperature": 0.7,
    }
    # HTTP POSTでAPIを呼び出す
    response = requests.post(url, json=payload)
    # 結果を確認
    if response.status_code == 200:
        data = response.json()
        return data["response"]
    else:
        raise Exception(f"API呼び出しに失敗しました：{response.status_code} {response.text}")

if __name__ == "__main__":
    # 猫の名前を考えるよう指示
    print(generate("猫の名前を1つだけ考えてください。"))
