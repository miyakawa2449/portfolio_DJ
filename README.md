# Django Portfolio & Blog CMS

ウェブエンジニアのポートフォリオサイトとブログを組み合わせたCMSをDjangoで構築するプロジェクトです。

## 概要

- **ポートフォリオサイト**: 1ページ完結型のランディングページ
- **技術ブログ**: 情報発信用のブログシステム
- **管理画面**: Django Adminを活用したコンテンツ管理
- **公開予定URL**: https://miyakawa.code

## 技術スタック

- **Backend**: Python 3.13.9, Django 5.2.7
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
│   ├── settings.py     # 環境変数対応済み
│   ├── urls.py
│   └── wsgi.py
├── portfolio/           # ポートフォリオアプリ
│   ├── models.py       # （Phase 2で実装予定）
│   ├── views.py
│   ├── admin.py
│   └── migrations/
├── blog/               # ブログアプリ
│   ├── models.py       # （Phase 2で実装予定）
│   ├── views.py
│   ├── admin.py
│   └── migrations/
├── docs/               # プロジェクトドキュメント
│   └── faq.md          # よくある質問と回答
├── reports/            # 開発レポート
│   └── 2025-10-22/    # 日次レポート
├── .claude/            # Claude Code設定
│   └── commands/       # カスタムコマンド
├── docker-compose.yml  # Docker設定
├── Dockerfile         # Python 3.13.9をソースからビルド
├── requirements.txt   # Python依存パッケージ
├── manage.py          # Django管理コマンド
├── .env.example       # 環境変数テンプレート
└── .gitignore         # Git除外設定
```

## 開発フェーズ

- [x] Phase 1: Docker環境構築 ✅ **完了** (2025-10-22)
  - Python 3.13.9ソースビルド成功
  - Django 5.2.7 + MySQL 8.0環境構築
  - portfolio、blogアプリ作成済み
- [ ] Phase 2: モデル構築 **← 現在ここ**
  - ポートフォリオセクション管理
  - ブログ記事・カテゴリー管理
- [ ] Phase 3: フロントエンド実装
  - Tailwind CSS導入
  - レスポンシブデザイン
- [ ] Phase 4: 機能拡張
  - 画像アップロード
  - リッチテキストエディタ
- [ ] Phase 5: 本番環境準備
  - セキュリティ設定
  - 静的ファイル配信
- [ ] Phase 6: AWS Lightsailデプロイ
  - HTTPS設定
  - ドメイン接続

## トラブルシューティング

### hash sum mismatchエラーが発生した場合
Dockerビルド時にエラーが発生した場合は、`docs/faq.md`の「トラブルシューティング」セクションを参照してください。

### スーパーユーザー作成時のエラー
`Superuser creation skipped due to not running in a TTY`エラーが出た場合は、別のターミナルから以下を実行:
```bash
docker exec -it portfolio_dj-web-1 python manage.py createsuperuser
```

## 開発ドキュメント

- **CLAUDE.md**: プロジェクト全体の仕様と開発方針
- **docs/faq.md**: よくある質問とトラブルシューティング
- **reports/**: 日次開発レポート（進捗・学習内容）

## ライセンス

このプロジェクトは MIT License のもとで公開されています。

## 作者

**Tsuyoshi Miyakawa**
- GitHub: [@miyakawa2449](https://github.com/miyakawa2449)

## リポジトリ

https://github.com/miyakawa2449/portfolio_DJ