# FAQ - よくある質問と回答

## 目次
- [Django基礎](#django基礎)
- [Docker関連](#docker関連)
- [セキュリティ](#セキュリティ)
- [トラブルシューティング](#トラブルシューティング)

## Django基礎

### Q: views.pyとtemplatesの役割分担は？
**A:** DjangoのMVTパターンで、ViewとTemplateは明確に役割が分離されています。

**views.py（ビュー）の役割：**
- **何のデータを取得するか**を定義
- ビジネスロジックの処理
- データベースからのデータ取得
- どのテンプレートを使うか指定

**templates（テンプレート）の役割：**
- **どう表示するか**を定義
- HTMLの構造とデザイン
- ビューから渡されたデータの表示方法

**例：ブログ記事表示の流れ**
```python
# views.py - データ取得のロジック
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # 使うテンプレート指定
    
    def get_queryset(self):
        return Post.objects.filter(is_published=True)  # 公開記事を取得
```

```html
<!-- templates/blog/post_list.html - 表示方法 -->
{% for post in posts %}
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
{% endfor %}
```

**メリット：**
- ロジックとデザインが独立
- デザイナーとプログラマーが同時作業可能
- 表示変更時はテンプレートのみ修正

**日付:** 2025-11-04  
**関連ファイル:** `blog/views.py`, `blog/templates/`

---

## Docker関連

### Q: Dockerを使っているプロジェクトで仮想環境（venv）は必要？
**A:** Docker使用時は**ローカルの仮想環境は不要**です。

**理由：**
1. **Dockerコンテナが仮想環境の役割を果たす**
   - コンテナ内に独立したPython環境が構築される
   - requirements.txtの依存関係もコンテナ内で管理
   - ローカルとコンテナの環境は完全に分離

2. **すべてのコマンドはコンテナ内で実行**
   ```bash
   # ❌ ローカルで実行（間違い）
   python manage.py createsuperuser
   
   # ✅ Dockerコンテナ内で実行（正しい）
   docker-compose exec web python manage.py createsuperuser
   ```

3. **ローカルの環境（base, venv等）は影響しない**
   - Anacondaの(base)環境のままでOK
   - 新たにvenvを作る必要なし

**日付:** 2025-11-04  
**関連ファイル:** `docker-compose.yml`, `Dockerfile`

---

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