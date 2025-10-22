# 2025-10-22 午前の作業レポート

## 作業内容
Django + MySQLのポートフォリオサイト開発環境をDockerで構築

## 実装した機能

### 1. Docker環境の構築
- **Dockerfile**：Python 3.13.9ベース → Ubuntu 24.04ベースに変更
- **docker-compose.yml**：Django（web）+ MySQL（db）のマルチコンテナ構成
- **requirements.txt**：Django 5.2.7, mysqlclient 2.2.7, python-dotenv, Pillow
- **.dockerignore**：不要ファイルの除外設定
- **.env**：環境変数（SECRET_KEY、DB_PASSWORD生成済み）

### 2. FAQドキュメントの作成
- `docs/faq.md`：Docker関連とセキュリティのQ&A追加

## 詰まったポイント

### 主な問題：hash sum mismatchエラー
- **症状**：apt-get実行時にパッケージのハッシュ値不一致
- **発生環境**：
  - python:3.13.9-slim
  - python:3.13-slim
  - python:3.12-slim
  - python:3.13.9-slim-bookworm
  - ubuntu:24.04
- **影響パッケージ**：linux-libc-dev、libperl5.40、libjansson4など

## 解決策（試行したが未解決）
1. Dockerキャッシュの完全クリア（`docker system prune -a`）
2. apt-getオプションの追加：
   - `--fix-missing`
   - `--no-install-recommends`
   - `apt-get clean`の実行
3. ベースイメージの変更（複数のバージョンを試行）
4. Docker Engineの設定変更（ユーザーが実施）

## 学んだこと
1. **hash sum mismatchエラーについて**
   - ミラーサーバーやネットワークの問題で発生
   - Dockerビルド時の一般的な問題
   - タイミングによって解決することがある

2. **Docker環境構築のベストプラクティス**
   - requirements.txtを先にコピー（キャッシュ効率化）
   - 不要なファイルは.dockerignoreで除外
   - apt-getのクリーンアップでイメージサイズ削減

3. **mysqlclientとMySQLの違い**
   - MySQL：データベースサーバー本体
   - mysqlclient：PythonからMySQLに接続するドライバー

## 次回やること
1. hash sum mismatchエラーの解決
   - 時間を置いて再試行
   - 別のミラーサーバーの利用を検討
   - 最悪の場合、一時的にSQLiteで開発開始

2. Djangoプロジェクトの初期化
   - プロジェクト名：config
   - `docker-compose run --rm web django-admin startproject config .`

3. アプリケーションの作成
   - portfolio（ポートフォリオページ用）
   - blog（技術ブログ用）

4. 基本設定ファイルの調整
   - settings.pyのデータベース設定
   - 環境変数の読み込み設定

5. .gitignoreファイルの作成

## 参考リンク
- Docker公式ドキュメント
- Django公式チュートリアル
- MySQLクライアントライブラリのインストールガイド

## 作業時間
- 開始：10:20頃
- 終了：11:00頃
- 作業時間：約40分

## 備考
- ユーザーが一旦休憩に入ったため、作業を中断
- hash sum mismatchエラーは時間を置くと解決する可能性がある
- 開発環境と本番環境の差異を最小化するため、MySQLでの環境構築を継続予定