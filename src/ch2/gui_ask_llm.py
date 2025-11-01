"""
Chapter2
GUIでOllamaに問い合わせる
"""
import ollama
import TkEasyGUI as eg

# OllamaのAPIを使うための設定
client = ollama.Client()
client_model = "llama3.2" # モデル名を指定

# 一行入力ダイアログを表示
prompt = eg.input(
    "プロンプトを入力してください。",
    default="白い猫の名前を1つ考えて"
)

# 入力がなければ処理終了
if prompt is None:
    quit()

# LLMに質問して結果を表示
response = client.generate(model=client_model, prompt=prompt)
result = response["response"]

# 答えをメモダイアログに表示
eg.popup_memo(result, title="LLMの応答")
