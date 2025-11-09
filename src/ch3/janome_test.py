"""
Chapter3 Janome使ってみる
"""
from janome.tokenizer import Tokenizer

sample_text = "洞察力があればすぐ怒ることはない。"

# 形態素解析器のインスタンスを作成
tokenizer = Tokenizer()

# 形態素解析を実行してリストに変換
tokens = list(tokenizer.tokenize(sample_text))

# 形態素を「|」区切りで表示
surface_list = [ token.surface for token in tokens ]
print("|".join(surface_list))
print("------")

# 詳細な結果を出力
for t in tokens:
    face = t.surface # 表層形
    pos = t.part_of_speech # 品詞
    base = t.base_form # 基本形
    reading = t.reading # 読み
    phonetic = t.phonetic # 発音
    print(f"{face}\t{pos},{base},{reading},{phonetic}")
