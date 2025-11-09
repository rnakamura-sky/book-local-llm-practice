FROM ubuntu:24.04

# Whisper.cppのぼりドに必要なパッケージを追加
RUN rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && apt-get update \
    && DEBIAN_FRONTED=noninteractive \
        apt-get install -y --no-install-recommends \
        curl git build-essential cmake ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV LANG=C.UTF-8
ENV WORKDIR=/app/whisper.cpp

# Whisper.cppのインストール
RUN mkdir -p $WORKDIR
WORKDIR $WORKDIR

# GitHubからリポジトリの取得
RUN git clone --branch v1.7.5 \
    https://github.com/ggerganov/whisper.cpp.git $WORKDIR

# ビルド
RUN make
# モデルのダウンロード
RUN make -j small

# Whisper.cppのサーバーを起動
CMD ["./build/bin/whisper-server", \
        "-m", "./models/ggml-small.bin", \
        "--port", "50022", "--host", "0.0.0.0"]
