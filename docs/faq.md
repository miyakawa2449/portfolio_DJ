# FAQ - よくある質問と回答

## 目次
- [Docker関連](#docker関連)
- [セキュリティ](#セキュリティ)
- [トラブルシューティング](#トラブルシューティング)

## Docker関連

### Q: 作成した内容を説明してください（Dockerfile）
**A:** Dockerfileは、Dockerイメージを構築するための設定ファイルです。主な構成要素：

1. **ベースイメージ**
   - `FROM python:3.13.9-slim`: Python 3.13.9の軽量版を使用
   - 通常版より小さく、本番環境に適している

2. **環境変数**
   - `PYTHONUNBUFFERED=1`: 標準出力をバッファリングしない（ログがリアルタイムで表示）
   - `PYTHONDONTWRITEBYTECODE=1`: .pycファイルを作成しない

3. **システム依存関係**
   - MySQLクライアントライブラリ（mysqlclient用）
   - ビルドツール（C拡張モジュール用）

4. **最適化**
   - requirements.txtを先にコピー（Docker層のキャッシュ効率化）
   - 不要なapt-getキャッシュを削除

5. **開発サーバー**
   - `0.0.0.0:8000`でDjango開発サーバーを起動（外部からアクセス可能）

**日付:** 2025-10-22  
**関連ファイル:** `Dockerfile`

---

### Q: docker-compose.ymlの内容を説明してください
**A:** docker-compose.ymlは複数のDockerコンテナを定義・管理するファイルです。主な構成要素：

1. **webサービス（Django）**
   - Dockerfileからビルド
   - ポート8000でアクセス可能
   - ローカルファイルをボリュームマウント（開発時の即時反映）
   - 環境変数で設定を管理

2. **dbサービス（MySQL）**
   - MySQL 8.0を使用
   - utf8mb4文字コード（日本語・絵文字対応）
   - データはmysql_dataボリュームで永続化

3. **環境変数**
   - .envファイルから読み込み
   - データベース接続情報とDjango設定を一元管理

**日付:** 2025-10-22  
**関連ファイル:** `docker-compose.yml`

## セキュリティ

### Q: これは何するコマンド？（SECRET_KEYとDB_PASSWORD生成）
**A:** Pythonの`secrets`モジュールを使って安全なランダム文字列を生成するコマンドです。

```python
python3 -c "import secrets; print(f'SECRET_KEY: django-insecure-{secrets.token_urlsafe(50)}'); print(f'DB_PASSWORD: {secrets.token_urlsafe(16)}')"
```

**何をするか：**
1. **SECRET_KEY生成**：
   - `secrets.token_urlsafe(50)`：50文字のランダムな文字列を生成
   - URL安全な文字（英数字、ハイフン、アンダースコア）のみ使用
   - Djangoのセキュリティ機能（CSRF保護など）で使用

2. **DB_PASSWORD生成**：
   - `secrets.token_urlsafe(16)`：16文字のランダムなパスワードを生成
   - MySQLデータベースのパスワードとして使用

**なぜ必要か：**
- 推測困難な強力なパスワード/キーを生成
- セキュリティ上重要な値を手動で考える必要がない
- `secrets`モジュールは暗号学的に安全な乱数生成器を使用

**日付:** 2025-10-22  
**関連ファイル:** `.env`

## トラブルシューティング

### Q: hash sum mismatchエラーの解決方法は？
**A:** Docker環境でapt-getコマンド実行時に発生する「hash sum mismatch」エラーの解決策です。

**最終的に採用した解決策：Python 3.13.9をソースからビルド**

```dockerfile
FROM ubuntu:24.04

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DEBIAN_FRONTEND=noninteractive

# APT設定（hash sum mismatchエラー対策）
RUN echo "Acquire::http::Pipeline-Depth 0;" > /etc/apt/apt.conf.d/99custom && \
    echo "Acquire::http::No-Cache true;" >> /etc/apt/apt.conf.d/99custom && \
    echo "Acquire::BrokenProxy true;" >> /etc/apt/apt.conf.d/99custom

# Python 3.13.9のソースからビルド
RUN apt-get update && apt-get install -y \
        build-essential \
        default-libmysqlclient-dev \
        pkg-config \
        wget \
        zlib1g-dev \
        libncurses5-dev \
        libgdbm-dev \
        libnss3-dev \
        libssl-dev \
        libreadline-dev \
        libffi-dev \
        libsqlite3-dev \
        libbz2-dev \
        liblzma-dev \
        tk-dev && \
    rm -rf /var/lib/apt/lists/*

# Python 3.13.9をソースからビルド・インストール
RUN cd /tmp && \
    wget https://www.python.org/ftp/python/3.13.9/Python-3.13.9.tgz && \
    tar xzf Python-3.13.9.tgz && \
    cd Python-3.13.9 && \
    ./configure --enable-optimizations --with-ensurepip=install && \
    make -j$(nproc) && \
    make altinstall && \
    cd / && \
    rm -rf /tmp/Python-3.13.9*

# Python 3.13.9をデフォルトに設定
RUN update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.13 1 && \
    update-alternatives --install /usr/bin/python python /usr/local/bin/python3.13 1 && \
    update-alternatives --install /usr/bin/pip3 pip3 /usr/local/bin/pip3.13 1
```

**エラーの原因：**
- APTミラーサーバーの問題
- ネットワーク接続の不安定さ
- Docker Hub上のイメージのパッケージリスト不整合

**解決プロセス：**
1. 複数のベースイメージを試行（python:3.13.9-slim、python:3.13-slim、ubuntu:24.04）
2. APT設定の追加（Pipeline-Depth、No-Cache、BrokenProxy）
3. 最終的にソースビルドに移行（確実性とセキュリティ面で優位）

**メリット：**
- Python 3.13.9確実にインストール（PPAは3.13.8のみ提供）
- セキュリティホール（3.13.8）を回避
- 環境の完全制御

**日付:** 2025-10-22  
**関連ファイル:** `Dockerfile`, `reports/2025-10-22/01_morning.md`