"""RAGを使ったQAシステム"""
import glob
import os
from typing import List
from langchain.prompts import ChatPromptTemplate
from langchain.schema import Document
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vecorstores import Chroma
from langchain_ollama import ChatOllama, OllamaEmbeddings

import config

# グローバル変数
qa_chain = None
retriever = None

def initialize_system():
    """システム全体を初期化"""
    global qa_chain, retriever
    print("RAGシステムを初期化します...")
    # ドキュメントを読み込んで分割
    documents = load_documents(config.DIR_TEXT_DATA)
    split_docs = split_documents(documents)
    # Embeddingモデルを設定
    embeddings = OllamaEmbeddings(model=config.EMBEDDING_MODEL)
    # Chromaのオブジェクトを取得
    vector_store = Chroma.from_documents(
        documents=split_docs,
        embedding=embeddings,
        persist_directory=config.DIR_VECTOR_DB
    )
    # Retrieverを作成
    retriever = vector_store.as_retriever(
        search_type="similarity", # 検索タイプを類似検索に設定
        search_kwargs={"k": config.RETRIEVAL_K} # 検索で取得する文章数
    )
    print("ベクトルDBに登録しました")
    # LLMを設定
    llm = ChatOllama(
        model=config.LLM_MODEL,
        temperature=config.TEMPERATURE
    )
    def format_docs(docs): # ドキュメントの内容を整形
        return "\n\n".join(doc.page_content for doc in docs)
    # QAチェーン（処理の流れ）を作成
    qa_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | ChatPromptTemplate.from_template(config.QA_TEMPLATE)
        | llm
        | StrOutputParser()
    )

def load_documents(target_dir: str) -> List[Document]:
    """textディレクトリからMarkdownファイルを読み込む"""
    

