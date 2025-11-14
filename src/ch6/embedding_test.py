"""埋め込みベクトルのテスト"""
import numpy as np
from langchain_ollama import OllamaEmbeddings

# 文章の一覧
sentences = [
    "彼はリンゴを食べたい。",
    "みかんが美味しくて、たくさん食べた。",
    "猫に餌をあげるのを忘れないでください。",
    "Pythonのリスト内包表記の使い方を教えてください。",
    "明日の天気はどうですか？"
]

# OllamaでEmbeddingが取得できるよう準備
embeddings = OllamaEmbeddings(model="granite-embedding:278m")
# 文章をEmbeddingベクトルに変換
embeddings_list = embeddings.embed_documents(sentences)
# ベクトルデータの例を表示
print("embeddings_list[0]:", embeddings_list[0][:5], "...")

def cosine_similarity(a, b):
    """コサイン類似度を計算する"""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# sentences[0]とほかの文章の類似度を調べる
query_embedding = embeddings_list[0]

# 繰り返し[0]との類似度を計算
similarities = []
for i, sentence_embedding in enumerate(embeddings_list):
    similarity = cosine_similarity(query_embedding, sentence_embedding)
    similarities.append((sentences[i], similarity))

# 類似度でソート(降順)
similarities.sort(key=lambda x: x[1], reverse=True)

# 結果を表示
print(f"基準文章： {sentences[0]}")
print("類似度順：")
for i, (sentence, sim) in enumerate(similarities):
    print(f"{i + 1}. {sentence}(類似度：{sim:.2f})")
