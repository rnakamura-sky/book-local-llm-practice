"""データセット作成"""
import random
from janome.tokenizer import Tokenizer

from config import *
from utils import *

# トークンの数を制限する値
MAX_TOKENS = 20000
# トークン列を初期化
ids = []

# コーパスを読み込む
file_size = os.path.getsize(FILE_CORPUS_TXT) # ファイルサイズ
read_size = 0
with open(FILE_CORPUS_TXT, "r", encoding="utf-8") as f:
    lines = list(f.readlines())
    random.shuffle(lines) # ランダムに並び替え

# 1行ずつ読み込んでトークン化する
for i, line in enumerate(lines):
    if i % 100 == 0:
        per = int(read_size / file_size * 100)
        print(f"読み込み中... {i}行目 ({per}%)")
    # トークンの数が上限を超えたら終了する
    if len(token2id) > MAX_TOKENS:
        print("読み込み完了")
        break
    read_size += len(line)
    # トークン化する
    tokens = text_to_ids(line, True)
    ids.extend(tokens) # トークンを追加する

# ファイルに保存
save_json(token2id, FILE_TOKEN2ID)
save_json(id2token, FILE_ID2TOKEN)
save_json(ids, FILE_IDS, indent=0)
print("保存しました。トークン数：", len(token2id))
