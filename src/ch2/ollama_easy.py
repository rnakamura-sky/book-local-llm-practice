"""
Chapter2 Ollamaを使う一番簡単なPythonプログラム
    ollamaモジュール使用した簡単なサンプル
"""
import ollama

# Ollamaを呼び出す
def generate(prompt, model="llama3.2"):
    """
    /api/generateを呼び出す関数を定義

    テキストとは異なり、requestsで実装したメソッドと同様な書き方をする
    """
    response = ollama.generate(
        model=model,
        prompt=prompt,
        options={"temperature": 0.7},
    )
    # 結果を返す
    return response["response"]

if __name__ == "__main__":
    # 猫の名前を考えるよう指示
    print(generate("猫の名前を1つだけ考えてください。"))
