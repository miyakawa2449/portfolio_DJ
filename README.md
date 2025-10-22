# Django Portfolio & Blog CMS

ウェブエンジニアのポートフォリオサイトとブログを組み合わせたCMSをDjangoで構築するプロジェクトです。

## 概要

- **ポートフォリオサイト**: 1ページ完結型のランディングページ
- **技術ブログ**: 情報発信用のブログシステム
- **管理画面**: Django Adminを活用したコンテンツ管理
- **公開予定URL**: https://miyakawa.code

## 技術スタック

- **Backend**: Python 3.13, Django 5.2.7
- **Database**: MySQL 8.0
- **Frontend**: Tailwind CSS, Django Template Engine
- **Deployment**: Docker, AWS Lightsail

## 開発環境のセットアップ

### 必要なソフトウェア

- Docker Desktop
- Git

### 環境構築手順

1. リポジトリをクローン
```bash
git clone https://github.com/miyakawa2449/portfolio_DJ.git
cd portfolio_DJ
```

2. 環境変数ファイルを作成（.envファイルはリポジトリに含まれていません）
```bash
cp .env.example .env
# .envファイルを編集して必要な値を設定
```

3. Dockerコンテナをビルド・起動
```bash
docker-compose up --build
```

4. マイグレーション実行（初回のみ）
```bash
docker-compose exec web python manage.py migrate
```

5. スーパーユーザー作成（初回のみ）
```bash
docker-compose exec web python manage.py createsuperuser
```

6. ブラウザでアクセス
- サイト: http://localhost:8000
- 管理画面: http://localhost:8000/admin

## プロジェクト構造

```
portfolio_DJ/
├── config/              # Djangoプロジェクト設定
├── portfolio/           # ポートフォリオアプリ
├── blog/               # ブログアプリ
├── docs/               # プロジェクトドキュメント
├── reports/            # 開発レポート
├── docker-compose.yml  # Docker設定
├── Dockerfile         # Dockerイメージ設定
└── requirements.txt   # Python依存パッケージ
```

## 開発フェーズ

- [x] Phase 1: Docker環境構築
- [ ] Phase 2: モデル構築
- [ ] Phase 3: フロントエンド実装
- [ ] Phase 4: 機能拡張
- [ ] Phase 5: 本番環境準備
- [ ] Phase 6: AWS Lightsailデプロイ

## ライセンス

このプロジェクトは MIT License のもとで公開されています。

## 作者

**Tsuyoshi Miyakawa**
- GitHub: [@miyakawa2449](https://github.com/miyakawa2449)

## リポジトリ

https://github.com/miyakawa2449/portfolio_DJ