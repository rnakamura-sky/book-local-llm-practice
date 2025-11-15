"""生成"""
import torch
import random

from config import *
from utils import *
from model import TokenLSTM

# トークン辞書を読み込む
id2token = load_json(FILE_ID2TOKEN)
token2id = load_json(FILE_TOKEN2ID)
vocab_size = len(token2id)

# モデルインスタンスを生成して、保存済みのモデルを読み込む
model = TokenLSTM(vocab_size)
model.load_state_dict(torch.load(FILE_MODEL))
model.eval() # 推論モデルに変更

def generate_text(model, start_text, temperature=0.9):
    """テキストを生成する"""
    max_length = 200 # 生成するテキストの最大長
    result = start_text
    # 開始トークンをID列に変換
    start_tokens = text_to_ids(start_text)
    # 開始トークンをテンソルに変換
    input_ids = torch.tensor(start_tokens).unsqueeze(0)
    hidden = None
    # 繰り返しテキスト生成処理を実行
    for _ in range(max_length):
        # モデルに入力して次のトークンを生成
        output, hidden = model(input_ids, hidden)
        # 出力の次元を調整
        logits = output[:, -1, :].squeeze() / temperature
        # logitsをsoftmaxで確率に変換
        prob = torch.softmax(logits, dim=0)
        # 次の単語(トークンID)を選ぶ
        next_id = torch.multinomial(prob, 1).item()
        if next_id >= 0 and str(next_id) in id2token:
            # トークンIDをテキストに変換
            t = id2token[str(next_id)]
            result += t
            if t == "。": # 文末トークンが出たら終了
                break
        # トークンIDをテンソルに変換
        input_ids = torch.tensor([[next_id]])
    return result

if __name__ == "__main__":
    # テキスト生成
    for _ in range(10):
        start_text = random.choice(["今日は", "人間", "最近", "猫", "春"])
        generated_text= generate_text(model, start_text)
        print("-", generated_text)
