"""
Chapter2 Ollamaを使う一番簡単なPythonプログラム
    ollamaモジュール使用した簡単なサンプル
    クライアントを生成する方法でアクセスします。
"""
import ollama

# OllamaのAPIを使用するための設定
client = ollama.Client()
client_model = "phi4"   # モデル名を設定

# Ollamaで手軽にphi4を使用するための関数を定義
def generate(prompt, temperature=0.7):
    """
    Ollamaを手軽に使用する
    """
    response = client.generate(
        model=client_model,
        prompt=prompt,
        options={"temperature": temperature}
    )
    return response["response"]

if __name__ == "__main__":
    # プロンプトを指定
    prompt = """
次の手順で最強にユニークな猫の名前を考えてください。
1. 10個の候補を列挙
2. 名前のユニーク度を10段階で評価
2. 最もユニークなものを1つ選んでください。
"""
    print(generate(prompt)) # 実行
