"""Transformer モデルの定義"""
import torch
import torch.nn as nn

from utils import *

# CUDA/MPSの使用確認
device = torch.device("cpu")
if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
print(f"Device: {device}")

# Transformerモデル
class TransformerModel(nn.Module):
    """自己回帰型テキスト生成用Transformerモデル"""
    def __init__(
            self,
            vocab_size: int,
            embed_dim: int,
            num_heads: int,
            num_layers: int,
            dropout: float = 0.1
    ):
        """初期化"""
        super().__init__()
        # Embeddingと位置エンコーディングを生成
        self.token_embed = nn.Embedding(vocab_size, embed_dim)
        self.pos_embed = nn.Parameter(torch.zeros(SEQ_LEN, embed_dim))
        # 精度を向上させるためドロップアウト層を追加
        self.dropout = nn.Dropout(dropout)
        # Transformer EncoderLayerを生成
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embed_dim, # 入力の次元元
            nhead=num_heads, # ヘッド数
            dim_feedforward=embed_dim * 4, # FFNの次元数
            dropout=dropout, # ドロップアウト
            batch_first=True, # バッチサイズを最初に指定
        )
        # Transformer Encoderを生成
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers)
        # 出力前の正規化と出力層
        self.layer_norm = nn.LayerNorm(embed_dim)
        self.fc = nn.Linear(embed_dim, vocab_size)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        順伝搬の指定
        x: [batch_size, seq_len] のトークンID
        return: [batch_size, seq_len, vocab_size] のロジット
        """
        seq_len = x.size(1)
        # Embeddingと位置エンコーディングを加算
        tok_emb = self.token_embed(x)
        pos_emb = self.pos_embed[:seq_len, :].unsqueeze(0)
        h = self.dropout(tok_emb + pos_emb)
        # 因果マスク（未来の情報を見ないように指定
        mask = nn.Transformer.generate_square_subsequent_mask(seq_len).to(h.device)
        h = self.transformer(h, mask=mask)
        # 正規化と線形変換
        h = self.layer_norm(h)
        out = self.fc(h)
        return out
