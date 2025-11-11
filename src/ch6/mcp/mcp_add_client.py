"""MCPサーバーに接続してツールを呼び出す"""
import asyncio
from fastmcp import Client

async def main():
    """クライアントメイン処理"""
    # MCPクライアントの初期化
    client = Client("http://127.0.0.1:8000/mcp/")
    async with client:
        # MCPサーバーに接続を行う
        await client.ping()
        # 利用可能なツールのリストを取得
        tools = await client.list_tools()
        print("利用可能なツール：", [tool.name for tool in tools])
        # 足し算ツールを呼び出す
        result = await client.call_tool("add", {"a": 5, "b": 7})
        # 結果を表示
        print("結果:", result.data)

if __name__ == "__main__":
    asyncio.run(main())
