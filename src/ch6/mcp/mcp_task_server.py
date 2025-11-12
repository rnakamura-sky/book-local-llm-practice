"""計算などのタスクを行うMCPサーバー"""
import warnings
from fastmcp import FastMCP
warnings.filterwarnings("ignore", category=DeprecationWarning)

# FastMCPサーバーの初期化
mcp = FastMCP("TaskServer")

# 足し算ツール定義
@mcp.tool()
def add(a: int, b: int) -> int:
    """a と b を足して返す"""
    return a + b

# 掛け算ツールんお定義
@mcp.tool()
def mul(a: int, b: int) -> int:
    """a と b を掛け算して返す"""
    return a * b

# 挨拶ツール
@mcp.tool()
def hello(name :str) -> str:
    """nameに挨拶して返す"""
    return f"{name}さん、こんにちは！"

if __name__ == "__main__":
    # HTTPモードで起動
    mcp.run(transport="http", host="127.0.0.1", port=80001)
