"""MCPクライアント"""
import asyncio
from fastmcp import Client
import ollama
import json

# OllamanのChatモデルの設定
LLM_MODEL = "qwen3:8b"
# LLMのプロンプトテンプレート
LLM_PROMPT = """\
あなたは優秀なAIアシスタントです。
ユーザーの質問に対して、適切な回答を提供してください。
あなたは、次のツールを利用できます。可能なら以下のツールを利用してください。
{tools}
なお、ツールを呼び出す際は、次のフォーマットの出力のみを出力してください。
```
{{"tool": "ツール名", "args": {{ "引数名": "値", "引数名": "値" }} }}
```
"""

async def main():
    """MCPクライアントメイン処理"""
    # MCPクライアントの初期化
    client = Client("http://127.0.0.1:80001/mcp")
    async with client:
        await client.ping()
        # 利用可能なツールのリストを取得
        desc = ""
        tools = await client.list_tools()
        for tool in tools:
            desc += f"- ツール名: {tool.name}\n"
            desc += f"  - 説明: {tool.description}\n"
            desc += f"  - 引数: {json.dumps(tool.inputSchema['properties'])}\n"
            if tool.outputSchema:
                desc += f"  - 出力: {json.dumps(tool.outputSchema['properties'])}\n"
        print("利用可能なツールの説明:")
        print(desc)
        # OllamaのChatモデルを初期化
        sys_prompt = LLM_PROMPT.format(tools=", ".join(tool.name for tool in tools))
        messages = [{"role": "system", "content": sys_prompt}]

        # チャットのメインループ
        while True:
            print("-" * 60)
            print("終了するときは'q'を入力してください。")
            user_input = input(">>> ")
            if user_input.lower() == "q":
                break
            if user_input.strip() == "":
                continue
            # ユーザーの入力をメッセージに追加
            messages.append({"role": "user", "content": user_input})

