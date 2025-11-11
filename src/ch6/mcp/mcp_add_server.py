"""足し算を行うMCPサーバー"""
from fastmcp import FastMCP

# FastMCPサーバーの初期化
mcp = FastMCP("AdditionServer")

# MCPツールの定義
@mcp.tool()
def add(a: int, b: int) -> int:
    """a と b を足して返す"""
    return a + b

if __name__ == "__main__":
    # HTTPモードで起動
    mcp.run(transport="http", host="127.0.0.1", port=8000)
