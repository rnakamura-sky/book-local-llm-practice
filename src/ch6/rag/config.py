"""RAG QA設定ファイル"""
import os
# パスの指定
DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
DIR_TEXT_DATA = os.path.join(DIR_ROOT, "text")
DIR_VECTOR_DB = os.path.join(DIR_ROOT, "chroma.db")
TARGET_EXT = [".md", ".txt"] # 対象ファイルの拡張子
# OllamaのEmbeddingのモデル設定
EMBEDDING_MODEL = "granite-embedding:278m"
# LLMモデル設定
LLM_MODEL = "qwen3:8b"
TEMPERATIRE = 0.4
# 検索設定

