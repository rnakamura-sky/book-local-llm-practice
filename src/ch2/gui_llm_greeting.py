"""
Chapter2
GUIでOllamaに問い合わせる(挨拶)
"""
import ollama
import TkEasyGUI as eg

# LLMに与えるプロンプトを指定
default_prompt = """
親しい友人に手紙を書きます。
気の利いた出だしの挨拶を一つだけ考えてください。
簡潔で、心に残るものをお願いします。
"""

# OllamaのAPIを使うための設定
client = ollama.Client()
client_model = "phi4" # モデル名を指定

# プロンプトを提示
prompt = eg.popup_memo(
    default_prompt.strip(),
    header="以下のプロンプトで挨拶文を作成します:",
    title="LLMに与えるプロンプト"
)

# 入力がなければ処理終了
if prompt is None:
    quit()

# 繰り返し、LLMに挨拶文を考えてもらう。
while True:
    # LLMに質問して結果を表示
    response = client.generate(model=client_model, prompt=prompt)
    result = response["response"]

    # 答えをメモダイアログに表示
    r = eg.popup_memo(
        result,
        title="LLMの応答",
        header="続けて挨拶文を生成する場合[OK]を押してください。")

    if r is None:
        break
