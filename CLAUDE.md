# Django CMS Project

## プロジェクト概要
ウェブエンジニアのポートフォリオサイトとブログを組み合わせたCMSをDjangoで構築し、AWSで公開する。
トップページ（ランディングページ）でポートフォリオを1ページで示し、技術ブログで情報発信を行う。
Djangoの標準機能（管理画面、認証システム）を活用し、効率的に開発を進める。

## 技術スタック

### バックエンド
- Python 3.13.9
- Django 5.x（Webフレームワーク）
- Django ORM（データベース操作）
- Django Admin（管理画面）
- Django Authentication（認証システム）

### データベース
- 開発環境：MySQL（Dockerコンテナ）
- 本番環境：MySQL（AWS Lightsail Database）
- 開発と本番で同じMySQL環境を使用することで環境差異を最小化

### フロントエンド
- Tailwind CSS（CSSフレームワーク）
- Django Template Engine
- デザイン：Figma（連携予定）

### デプロイ
- AWS Lightsail
- ドメイン：https://miyakawa.code（設定済み）
- SSL：未設定（実装時に対応予定）
- **Docker**：コンテナベースのデプロイ

## 開発環境
- OS：macOS
- エディタ：VSCode
- Python：3.13.9
- MySQL：インストール済み
- **Docker for Mac**：コンテナ開発環境
- 開発時間：1日2-3時間

### Docker開発環境
- 本番環境（AWS Lightsail）との環境差異を最小化
- デプロイコストを削減
- docker-compose.ymlで開発環境を管理
- Dockerfileで本番環境を再現
- **ボリュームマウント**：ローカルのコード変更が即座にコンテナに反映
- **ポート設定**：8000番ポートでアクセス（http://localhost:8000）
- **環境変数管理**：.envファイルで一元管理（.gitignore対象）
- **コンテナのログ確認**：docker-compose logs -f で確認
- **コンテナの再起動**：コード変更時は自動リロード、設定変更時は手動再起動
- **.dockerignore**：不要なファイルをイメージから除外
- **マルチステージビルド**：本番用Dockerfileでイメージサイズを最適化

## MVP（最小機能）

### 訪問者向け機能
1. **ポートフォリオ（トップページ / ランディングページ）**
   - 1ページ完結型のポートフォリオサイト
   - セクション構成（予定）：
     - About：自己紹介・プロフィール
     - Service：提供できるサービス
     - Skill：技術スタック・スキルセット
     - 実績：過去のプロジェクト・制作物
     - Contact：お問い合わせ
   - 動的コンテンツ（管理画面から編集可能）
   - Figmaデザインに基づく実装
   - 各セクションの表示/非表示、順序変更可能
   - レスポンシブ対応

2. **技術ブログ**
   - 記事一覧ページ
   - 記事詳細ページ
   - カテゴリー別表示

### 管理者向け機能
1. **Django Admin管理画面**
   - ログイン機能（Django標準）
   - ユーザー管理（Django標準）
   
2. **ポートフォリオページ管理**
   - セクションごとのコンテンツ編集
     - About（自己紹介）
     - Service（サービス内容）
     - Skill（スキルセット）
     - 実績（プロジェクト）
     - Contact（連絡先）
   - 見出し・テキスト・画像の変更
   - 表示/非表示切り替え
   - セクション順序の並び替え
   - 実績項目の追加・編集・削除
   
3. **ブログ記事管理**
   - 記事の作成・編集・削除
   - 下書き/公開ステータス管理
   - 画像アップロード
   - カテゴリー・タグ管理

## 開発フェーズ

### Phase 1：Django基礎 + Docker環境構築（Week 1-2）
- **Docker環境構築**
  - Dockerfile作成（Python 3.13.9ベース）
  - docker-compose.yml作成（Django + MySQL構成）
  - 環境変数設定（.env）
  - ボリュームマウント設定
- Djangoプロジェクト初期化
- アプリ作成（portfolio, blog）
- 基本的なビューとURL設定
- テンプレート設定
- 静的ファイル配信
- ポートフォリオトップページの基礎作成（仮データ）
- Docker環境での動作確認

**注意：** Dockerファイルの記述はClaude Codeに相談しながら作成

### Phase 2：モデル構築（Week 3）
- **ポートフォリオモデル作成**
  - PortfolioSection モデル（セクション管理）
  - セクションタイプ（About, Service, Skill, 実績, Contact）
  - Project モデル（実績・プロジェクト個別管理）
  - Skill モデル（スキル個別管理）※必要に応じて
  - 順序管理フィールド
  - 表示/非表示フラグ
- **ブログモデル作成**
  - Post モデル（記事）
  - Category モデル（カテゴリー）
- マイグレーション実行
- Django Admin登録・カスタマイズ
- 記事の一覧・詳細ビュー作成
  
**注意：** モデル設計の詳細は実装時にClaude Codeと相談しながら決定

### Phase 3：フロントエンド実装（Week 4-5）
- Tailwind CSS導入
- Figmaデザインの実装
- **ポートフォリオトップページの動的表示**
  - データベースからセクション取得
  - セクションタイプ別テンプレート作成（About, Service, Skill, 実績, Contact）
  - 画像・テキストの動的レンダリング
  - スムーススクロール実装
  - 1ページ完結型のUI/UX
- ブログ一覧・詳細ページのデザイン適用
- レスポンシブ対応
- ページネーション実装
  
**注意：** セクションの具体的な内容やデザイン詳細は実装しながら決定

### Phase 4：機能拡張（Week 6-7）
- カテゴリー機能実装
- タグ機能追加
- 画像アップロード機能
- リッチテキストエディタ導入（django-ckeditor等）
- SEO対策（メタタグ）
- 検索機能

### Phase 5：本番環境準備（Week 8）
- 環境変数管理（django-environ）
- MySQL対応設定
- 静的ファイル収集設定
- セキュリティ設定強化
- DEBUG=False設定

### Phase 6：AWS Lightsailデプロイ（Week 9）
- Lightsail インスタンス作成（Ubuntu推奨）
- Docker / Docker Compose インストール
- Lightsail データベース設定（MySQL）
- **Dockerイメージのビルドとデプロイ**
  - 本番用Dockerfileの調整
  - docker-compose.production.yml設定
  - 環境変数の本番設定
- Nginx設定（リバースプロキシ）
- SSL証明書設定（Let's Encrypt）
- ドメイン（miyakawa.code）のSSL対応
- 静的ファイル配信設定
- コンテナの自動起動設定

**Docker使用のメリット：**
- 開発環境と本番環境の差異を最小化
- デプロイが簡単（docker-compose up -d）
- 環境の再現性が高い
- トラブルシューティングが容易

## Djangoの主要概念

### プロジェクト構造
```
portfolio_DJ/
├── manage.py
├── Dockerfile                 # Docker設定
├── docker-compose.yml         # 開発環境用Docker Compose
├── docker-compose.production.yml  # 本番環境用Docker Compose
├── .env                       # 環境変数（gitignore対象）
├── .dockerignore              # Dockerイメージから除外するファイル
├── requirements.txt           # Python依存パッケージ
├── config/                    # プロジェクト設定
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/                 # ポートフォリオアプリ（トップページ）
│   ├── models.py              # PortfolioSection, Project, Skill モデル
│   ├── views.py
│   ├── urls.py
│   ├── admin.py               # セクション・実績管理画面
│   └── templates/
│       └── portfolio/
│           └── index.html     # 1ページ完結型ポートフォリオ
├── blog/                      # ブログアプリ
│   ├── models.py              # Post, Category モデル
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       └── blog/
│           ├── list.html
│           └── detail.html
├── docs/                      # プロジェクト仕様書
│   ├── database.md            # データベース仕様書
│   ├── routing.md             # URL/ルーティング仕様書
│   ├── models.md              # モデル詳細仕様書
│   ├── faq.md                 # FAQ（よくある質問）
│   └── deployment.md          # デプロイ手順書
├── reports/                   # 日次レポート
│   └── 2025-10-22/
│       ├── 01_morning.md
│       ├── 02_afternoon.md
│       └── 03_summary.md
└── .claude/                   # Claude Code設定
    └── commands/
        ├── start-session.md   # セッション開始コマンド
        ├── update-docs.md     # 仕様書更新コマンド
        └── add-faq.md         # FAQ追加コマンド
```

### MTV パターン
- **Model**：データベース構造の定義
- **Template**：HTML表示
- **View**：ビジネスロジック

## 開発時の注意事項

### Django特有のベストプラクティス
- **アプリは小さく単一責任で**：portfolio、blog など機能ごとに分割
- **モデルに多くのロジックを**：ビジネスロジックはモデルに集約
- **クラスベースビュー活用**：ListView、DetailView など
- **マイグレーションは必ず確認**：データベース変更前に内容チェック
- **動的コンテンツの設計**：
  - セクション型モデルで柔軟性を確保
  - 順序フィールド（order）で並び順管理
  - 汎用的な設計を心がける（将来の拡張を考慮）

### セキュリティ
- CSRF対策（Django標準）
- SQLインジェクション対策（ORMを使用）
- XSS対策（テンプレートエスケープ）
- SECRET_KEYは環境変数で管理
- ALLOWED_HOSTSを本番環境で設定
- .gitignoreで秘密情報を除外

## セキュリティガイドライン

### Djangoが自動的に守ってくれること
以下の脆弱性は、Djangoを正しく使えば自動的に防御される：

✅ **SQLインジェクション**
- Django ORMを使用すれば自動防御
- 生のSQLクエリ（`.raw()`, `.extra()`）は避ける

✅ **XSS（クロスサイトスクリプティング）**
- テンプレート変数 `{{ variable }}` は自動エスケープ
- `|safe` フィルターは信頼できるデータのみ使用

✅ **CSRF（クロスサイトリクエストフォージェリ）**
- フォームに `{% csrf_token %}` を含める
- Django Middlewareが自動検証

✅ **パスワードハッシュ化**
- Djangoのユーザーモデルが自動的にハッシュ化
- 平文で保存されることはない

### フェーズ別セキュリティチェックリスト

#### Phase 1-2：基礎設定（今すぐ実施）

**必須項目：**
- [ ] `.env`ファイルを作成し、秘密情報を管理
- [ ] `.gitignore`に`.env`を追加
- [ ] `SECRET_KEY`を生成（50文字以上のランダム文字列）
- [ ] データベースパスワードを強力に設定（12文字以上、英数字+記号）
- [ ] `DEBUG=True`を`.env`に設定（開発環境用）

**環境変数の例：**
```bash
# .env
SECRET_KEY=django-insecure-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
DB_NAME=portfolio_db
DB_USER=portfolio_user
DB_PASSWORD=強力なパスワード12文字以上
DB_HOST=db
DB_PORT=3306
DEBUG=True
```

**セキュリティキーの生成：**
Claude Codeに依頼：
```
「Django用のSECRET_KEYを生成してください」
```

#### Phase 3-4：機能実装時

**ファイルアップロード対策：**
- [ ] 許可する拡張子を制限
- [ ] ファイルサイズを制限（5MB推奨）
- [ ] `ImageField`を使用（画像の実体を検証）
- [ ] アップロード先ディレクトリをメディアルート配下に限定

```python
# models.py
from django.core.validators import FileExtensionValidator

class Post(models.Model):
    image = models.ImageField(
        upload_to='blog/%Y/%m/',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif'])],
        help_text='最大5MB、jpg/png/gif形式'
    )

# settings.py
MAX_UPLOAD_SIZE = 5 * 1024 * 1024  # 5MB
ALLOWED_IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/gif']
```

**フォーム入力の検証：**
- [ ] ModelFormを使用（自動バリデーション）
- [ ] カスタムバリデーターで追加検証
- [ ] ユーザー入力を信頼しない

**Claude Codeに相談：**
```
「画像アップロード機能のセキュリティ対策を実装してください」
```

#### Phase 5：本番環境準備

**必須設定：**
- [ ] `DEBUG=False`に変更
- [ ] `ALLOWED_HOSTS`を設定（`['miyakawa.code']`）
- [ ] 本番用の新しい`SECRET_KEY`を生成
- [ ] HTTPSを強制（`SECURE_SSL_REDIRECT=True`）
- [ ] セキュリティヘッダーを設定
- [ ] 静的ファイルを正しく配信
- [ ] 管理画面URLを変更（`/admin/`以外）

```python
# settings.py（本番環境）
DEBUG = False
ALLOWED_HOSTS = ['miyakawa.code']
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

**Claude Codeに相談：**
```
「本番環境のセキュリティ設定を確認してください」
```

#### Phase 6：デプロイ時

**デプロイ前チェックリスト：**
- [ ] Django内蔵のセキュリティチェックを実行
- [ ] 不要なパッケージを削除
- [ ] ログ設定を確認
- [ ] データベース接続情報の確認
- [ ] SSL証明書の設定

```bash
# セキュリティチェック実行
python manage.py check --deploy
```

### よくあるセキュリティリスクと対策

#### 1. 環境変数の漏洩
**リスク：** `.env`ファイルをGitにコミット
**対策：**
- `.gitignore`に必ず`.env`を追加
- コミット前に`git status`で確認
- Claude Codeに確認：
```
「.gitignoreが正しく設定されているか確認してください」
```

#### 2. DEBUGモードの本番使用
**リスク：** エラー詳細が公開され、内部構造が露呈
**対策：**
- 本番環境では必ず`DEBUG=False`
- エラーページをカスタマイズ（404.html, 500.html）

#### 3. 脆弱なパスワード
**リスク：** ブルートフォース攻撃
**対策：**
- 12文字以上
- 英数字+記号の組み合わせ
- パスワード生成をClaude Codeに依頼可能

#### 4. SQLインジェクション
**リスク：** 生のSQLクエリ実行
**対策：**
- 常にORMを使用
- `.raw()`や`.extra()`を避ける
- どうしても必要な場合はパラメータ化

```python
# ❌ 危険
User.objects.raw(f"SELECT * FROM users WHERE name = '{user_input}'")

# ✅ 安全
User.objects.raw("SELECT * FROM users WHERE name = %s", [user_input])

# ✅ 最も安全（ORM使用）
User.objects.filter(name=user_input)
```

#### 5. XSS（クロスサイトスクリプティング）
**リスク：** ユーザー入力をそのまま表示
**対策：**
- テンプレートの自動エスケープに頼る
- `|safe`フィルターは慎重に使用
- JavaScriptにユーザー入力を渡す場合は`escapejs`を使用

```django
<!-- ✅ 安全（自動エスケープ） -->
{{ user_comment }}

<!-- ❌ 危険 -->
{{ user_comment|safe }}

<!-- ✅ JavaScriptで使う場合 -->
<script>
const comment = "{{ user_comment|escapejs }}";
</script>
```

#### 6. ファイルアップロードの脆弱性
**リスク：** 悪意あるファイルのアップロード
**対策：**
- `ImageField`で画像の実体を検証
- ファイルサイズ制限
- 拡張子ホワイトリスト
- アップロードファイルは非実行ディレクトリに保存

### Claude Codeでのセキュリティレビュー

#### 実装後の確認
**毎回の開発サイクルで：**
```
「今実装した機能にセキュリティ上の問題はありますか？」
```

#### フェーズ完了時のレビュー
```
「Phase 2で実装したコード全体をセキュリティの観点でレビューしてください。
OWASP Top 10の観点でチェックしてください。」
```

#### デプロイ前の最終チェック
```
「本番環境にデプロイする前のセキュリティチェックリストを実行してください。
以下を含めてください：
1. DEBUG設定
2. ALLOWED_HOSTS
3. SECRET_KEY
4. HTTPS設定
5. セキュリティヘッダー
6. 環境変数の確認」
```

#### カスタムコマンドの作成
`.claude/commands/security-check.md`を作成：

```markdown
---
name: security-check
description: セキュリティチェックを実行
---

以下の観点でセキュリティチェックを実行してください：

1. **環境変数**
   - .envファイルが.gitignoreに含まれているか
   - 秘密情報がコードに直接書かれていないか

2. **Django設定**
   - DEBUG設定は適切か（開発:True, 本番:False）
   - ALLOWED_HOSTSは設定されているか
   - SECRET_KEYは環境変数から読み込んでいるか

3. **入力検証**
   - フォームにCSRFトークンが含まれているか
   - ファイルアップロードに制限があるか
   - ユーザー入力の検証が適切か

4. **テンプレート**
   - ユーザー入力が適切にエスケープされているか
   - |safeフィルターが適切に使用されているか

5. **データベース**
   - ORMを使用しているか
   - 生のSQLクエリがある場合、パラメータ化されているか

6. **本番環境設定（Phase 5以降）**
   - HTTPS設定
   - セキュリティヘッダー
   - セッションセキュリティ

問題が見つかった場合、具体的な修正方法を提案してください。
```

**使い方：**
```bash
/security-check
```

### セキュリティの学習リソース

- Django公式セキュリティドキュメント
- OWASP Top 10（Webアプリケーションの主要な脆弱性）
- Mozilla Web Securityガイドライン

### 重要な心構え

**完璧を目指さない：**
- セキュリティは100%完璧にはできない
- フェーズごとに必要なことを確実に実施
- 不明な点はClaude Codeに相談

**Djangoを信頼する：**
- Djangoのベストプラクティスに従えば、多くの脆弱性は自動的に防げる
- 「Djangoらしい」書き方を心がける

**定期的な更新：**
- Djangoとパッケージを定期的にアップデート
- セキュリティパッチは優先的に適用

**不安なときは：**
```
「この実装はセキュリティ上安全ですか？」
```
とClaude Codeに相談すればOK

### データベース
- **開発時はDocker上のMySQL**：本番環境と同じ環境で開発
- **マイグレーションは頻繁に**：モデル変更のたびに実行
- **初期データはfixtureで**：テストデータを簡単に投入
- **Docker環境でのデータ永続化**：ボリュームマウントでデータ保持

### コード品質
- Django命名規則に従う
- PEP 8に準拠
- 適切なディレクトリ構造を維持
- コメントは必要最小限

### Git管理
- 機能ごとにコミット
- わかりやすいコミットメッセージ
- ブランチを活用（main, develop, feature/*）
- マイグレーションファイルはコミットする
- **.gitignoreで除外するもの**：
  - .env（環境変数ファイル）
  - db.sqlite3（開発時のDBファイル）※Docker環境では不使用
  - __pycache__/（Pythonキャッシュ）
  - *.pyc（コンパイル済みPython）
  - venv/（仮想環境）※Docker環境では不使用
  - .DS_Store（macOS）
  - staticfiles/（収集後の静的ファイル）
  - media/（アップロードファイル）※必要に応じて

## Django標準機能の活用

### Django Admin（管理画面）
- カスタマイズ可能な管理画面がデフォルト
- list_display、search_fields等で簡単にカスタマイズ
- 権限管理も標準装備

### Django Authentication
- ユーザー登録・ログイン機能
- パスワードハッシュ化
- セッション管理
- 権限・グループ管理

### その他便利な機能
- フォーム処理（ModelForm）
- ページネーション
- 静的ファイル管理
- メール送信
- キャッシュフレームワーク

## 開発レポート管理

### 日次レポートの運用方針
**重要：** Claude Codeはセッションベースのため、セッション終了後の会話履歴は取得できない。そのため、**作業の区切りごとにこまめにレポートを作成する**ことを推奨。

### レポート作成のタイミング
1. **作業の区切りごと**（午前終了時、午後終了時など）
2. **Claude Codeセッション終了前**
3. **重要な実装が完了したとき**
4. **大きな問題を解決したとき**

### レポート保存場所
```
reports/
├── 2025-10-22/
│   ├── 01_morning.md      # 午前の作業
│   ├── 02_afternoon.md    # 午後の作業
│   └── 03_summary.md      # 1日のまとめ（任意）
├── 2025-10-23/
│   └── ...
```

### レポート内容
各レポートには以下を記録：
- **作業内容**：何を実装したか
- **実装した機能**：具体的なコード・ファイル
- **詰まったポイント**：エラーや問題
- **解決策**：どう解決したか
- **学んだこと**：新しい知識・発見
- **次回やること**：TODO
- **参考リンク**：参照したドキュメント等

### Claude Codeへの依頼方法

**セッション終了前：**
```
「今のセッションの作業内容をreports/YYYY-MM-DD/01_morning.mdにまとめてください」
```

**Gitコミット履歴から作成：**
```
「今日のGitコミット履歴を見て、作業レポートを作成してください」
```

**既存レポートへの追記：**
```
「reports/YYYY-MM-DD/01_morning.mdに今の作業内容を追記してください」
```

### レポート活用方法
- 週次で振り返り、進捗確認
- 詰まったポイントをCLAUDE.mdに反映
- 学習の記録として活用
- デバッグ時の参考資料
- 将来の類似作業での参照

### バックアップ推奨
- reportsフォルダはGitにコミット
- 重要な学びはCLAUDE.mdにも転記

### 注意事項
- Claude Codeのセッションを跨いだ記録は不可能
- 記録漏れを防ぐため、こまめな作成を心がける
- 完全自動化は難しいため、手動メモとの併用も検討

## Claude Code活用方針

### セッション開始時のルーティン
**カスタムコマンドで作業提案を自動化**

`.claude/commands/start-session.md`を作成して使用：

```markdown
---
name: start-session
description: セッション開始時のチェックと作業提案
---

以下の手順で作業提案を行ってください：

1. CLAUDE.mdを読み込んで、プロジェクトの現在のフェーズを確認
2. reports/フォルダ内の最新のレポート（直近3日分）を確認
3. 前回の「次回やること」を確認
4. 現在のGitブランチとコミット履歴を確認
5. 以下の形式で今日の作業を提案：

## 今日の推奨作業

### 前回までの進捗
[最新レポートから要約]

### 今日やるべきこと
1. [優先度高]
2. [優先度中]
3. [優先度低]

### 確認事項
- 前回の積み残しタスク
- 未解決の問題

提案後、作業を開始するか確認してください。
```

**使い方：**
```bash
# Claude Code起動後
/start-session
```

**チェック範囲：**
- CLAUDE.md：プロジェクト全体の状況
- 直近3日分のreports：最新の作業内容
- Gitログ：最近のコミット履歴

### 相談タイミング
- 各フェーズ開始時に実装方針を相談
- Django特有の概念（MTV、マイグレーション等）で迷ったとき
- エラーが出たら即相談
- ベストプラクティスを知りたいとき

### 仕様書の自動生成
**プロジェクトの仕様書をClaude Codeで自動生成・更新**

#### 管理する仕様書
```
docs/
├── database.md      # データベース仕様書
├── routing.md       # URL/ルーティング仕様書
├── models.md        # モデル詳細仕様書
├── faq.md          # FAQ（よくある質問）
└── deployment.md    # デプロイ手順書
```

#### 仕様書作成のタイミング

**モデル作成・変更時：**
```
「今作成したモデルをdocs/database.mdに仕様書として追加してください。
以下の情報を含めてください：
- テーブル名
- フィールド一覧（型、制約、説明）
- リレーション
- インデックス
- 使用例」
```

**URL設定時：**
```
「今設定したURLをdocs/routing.mdに追加してください」
```

**一括更新：**
カスタムコマンド `/update-docs` を作成（.claude/commands/update-docs.md）

```markdown
---
name: update-docs
description: プロジェクトの仕様書を最新状態に更新
---

以下の仕様書を現在のコードベースから自動生成・更新してください：

1. **docs/database.md**
   - 全モデルのフィールド定義
   - リレーション図
   - インデックス情報

2. **docs/routing.md**
   - 全URLパターン
   - View一覧
   - パラメータ説明

3. **docs/models.md**
   - モデルごとの詳細説明
   - メソッド一覧
   - 使用例

各ファイルが存在しない場合は新規作成してください。
```

**使い方：**
```bash
/update-docs
```

#### 仕様書のメリット
- 常に最新の仕様が文書化される
- デバッグ時の参照資料
- 将来の機能追加時の参考
- チーム開発時の共有資料
- デプロイ時の確認資料

### FAQ管理（よくある質問）
**開発中の質問と回答を蓄積してナレッジベース化**

#### FAQファイルの場所
`docs/faq.md`

#### FAQ作成のタイミング

**方法1：質問解決時に即座に追加（推奨）**

カスタムコマンド `/add-faq` を作成（.claude/commands/add-faq.md）

```markdown
---
name: add-faq
description: 今の質問をFAQに追加
---

直前の質問と回答を以下の形式でdocs/faq.mdに追加してください：

### Q: [質問内容]
**A:** [回答内容]

[コード例があれば含める]

**日付:** [今日の日付]  
**関連ファイル:** [該当ファイルがあれば]

適切なカテゴリー（Django基礎、モデル設計、Docker関連、Tailwind CSS、トラブルシューティング、デプロイ等）に分類してください。
カテゴリーが存在しない場合は新規作成してください。
```

**使い方：**
```bash
# 質問して解決した後
/add-faq
```

**方法2：日次レポート作成時に一括追加**

```
「今日のセッションで質問したことをdocs/faq.mdに追加してください。
Q&A形式で、カテゴリー別に整理してください」
```

#### FAQの構成例

```markdown
# FAQ - よくある質問と回答

## 目次
- [Django基礎](#django基礎)
- [モデル設計](#モデル設計)
- [Docker関連](#docker関連)
- [Tailwind CSS](#tailwind-css)
- [トラブルシューティング](#トラブルシューティング)
- [デプロイ](#デプロイ)

## Django基礎

### Q: マイグレーションファイルはGitにコミットすべき？
**A:** はい、コミットすべきです。マイグレーションファイルはデータベーススキーマの変更履歴であり、チームメンバー全員が同じスキーマを共有する必要があるためです。

**日付:** 2025-10-22  
**関連ファイル:** `portfolio/migrations/0001_initial.py`

---

### Q: `related_name`は必須？
**A:** 必須ではありませんが、推奨されます。逆参照時のクエリが明確になり、コードの可読性が向上します。

```python
# 推奨
projects = models.ForeignKey(
    Project, 
    related_name='sections',
    on_delete=models.CASCADE
)

# 使用例
project.sections.all()  # わかりやすい
```

**日付:** 2025-10-22

---

## Docker関連

### Q: ボリュームマウントとCOPYの違いは？
**A:** 
- **ボリュームマウント**: ローカルファイルをコンテナにリアルタイム反映（開発用）
- **COPY**: ファイルをイメージに焼き込む（本番用）

開発環境ではボリュームマウント、本番環境ではCOPYを使用します。

**日付:** 2025-10-22

---

## トラブルシューティング

### Q: `ModuleNotFoundError: No module named 'XXX'`が出る
**A:** 依存パッケージがインストールされていません。

**解決方法:**
```bash
# requirements.txtに追加
echo "package-name==version" >> requirements.txt

# Dockerイメージを再ビルド
docker-compose up --build
```

**日付:** 2025-10-22
```

#### FAQのメンテナンス

**定期的な整理（週次推奨）：**
```
「docs/faq.mdを整理して、重複を削除し、カテゴリーを最適化してください」
```

**検索しやすくする：**
- カテゴリー別に分類
- 目次を作成
- 日付を記録（情報の鮮度確認用）
- 関連ファイルへのリンク

#### FAQのメリット
- 学んだことが蓄積される
- 同じ質問を繰り返さない
- トラブルシューティングのナレッジベース
- 将来の自分への参考資料
- チームメンバーへの共有資料
- 開発効率の向上

### 実装詳細
- **Docker環境の構築はClaude Codeに依頼**
  - Dockerfile（Python 3.13.9ベース）
  - docker-compose.yml（開発環境）
  - docker-compose.production.yml（本番環境）
  - .dockerignore設定
  - ベストプラクティスに沿った設定
- Djangoプロジェクトの初期設定はClaude Codeに依頼
- **ポートフォリオページのモデル設計を相談**
  - セクション構成（About, Service, Skill, 実績, Contact）
  - 柔軟で拡張可能な構造
  - 詳細な項目は実装時に決定
- ブログのモデル設計で相談
- Admin画面のカスタマイズ方法を相談
- セクション管理のUI/UX設計
- Figma連携は Phase 3 で実施
  
**重要：** 
- ポートフォリオの各セクションの具体的な内容・項目は実装しながら柔軟に決定していく
- Dockerファイルの記述内容は必ず確認し、理解できない部分はClaude Codeに説明を求める

### 避けること
- 最初から複雑なカスタマイズをしない
- Django標準の仕組みを無理に変えない
- 理解できないコードをそのまま使わない

## 後で検討する機能

### ポートフォリオ拡張機能
- プロジェクト詳細ページ（実績の個別ページ）
- スキルレベル表示（チャート・グラフ）
- お問い合わせフォーム機能強化
- メール通知機能
- GitHubリポジトリ連携
- コンタクトフォームのスパム対策
- 多言語対応（日本語/英語）

### ブログ拡張機能
- コメント機能（django.contrib.comments）
- いいね機能
- 関連記事表示
- RSS/Atomフィード
- サイトマップ自動生成
- 記事の予約投稿
- タグクラウド

### ユーザー管理
- 複数管理者対応（標準機能）
- 権限管理（標準機能）
- ユーザープロフィール

### パフォーマンス
- キャッシュ機能（Django標準）
- 画像最適化
- CDN連携

### SEO・分析
- Google Analytics連携
- Open Graph対応
- 構造化データ

## AWS Lightsail デプロイ情報

### 現在の状態
- ドメイン：https://miyakawa.code（設定済み）
- SSL証明書：未設定
- インスタンス：未作成

### デプロイ時の実装項目
- Lightsail インスタンス作成（Ubuntu推奨）
- Docker / Docker Compose インストール
- Lightsail データベース作成（MySQL）
- **Dockerを使ったデプロイ**
  - 本番用docker-compose.production.ymlの配置
  - 環境変数ファイルの設定（.env.production）
  - Dockerイメージのビルド
  - コンテナの起動と動作確認
- Nginx設定（リバースプロキシまたはDocker Composeに含める）
- SSL証明書取得と設定（Let's Encrypt/Certbot）
- 静的ファイル収集（collectstatic）
- ログ管理設定
- コンテナの自動起動設定（systemdまたはDocker restart policy）

**Dockerを使うメリット：**
- 開発環境と本番環境の環境差異が最小限
- デプロイが簡単（設定ファイルのコピー + docker-compose up）
- 環境の再現性が高い（Dockerfileで環境が定義される）
- トラブルシューティングが容易（同じ環境をローカルで再現可能）
- スケーリングが容易

## 技術的な制約・前提

### スキルレベル
- Python基礎：理解済み（Python 3.13.9使用）
- SQL：読めるが書けない→Django ORMでカバー可能
- Django：未経験→段階的に学習
- **Docker：見様見真似でファイルを書けるレベル→Claude Codeでサポート**
- AWS：デプロイ経験なし→Phase 6で学習

**注意：** 
- Python 3.13は最新版のため、一部パッケージで互換性の問題が出る可能性あり。その際はClaude Codeと相談しながら解決する。
- Dockerファイルの記述はClaude Codeに相談しながら、ベストプラクティスに沿って作成する。

### 優先順位
1. 動くものを作る（Django標準機能を活用）
2. 理解しながら進める
3. 完璧を求めすぎない（内容は実装しながら決める）
4. 必要になったら機能追加

## Djangoの学習リソース

### 公式ドキュメント
- Django公式チュートリアル（必読）
- Django公式ドキュメント（日本語版あり）

### 推奨学習順序
1. Django基礎概念（MTV、アプリ、マイグレーション）
2. モデル定義とORM
3. ビューとURL設定
4. テンプレート
5. 管理画面カスタマイズ
6. フォーム処理

---

**備考**
- この要件は開発を進めながら更新する
- 各フェーズで学んだことを追記する
- 詰まったポイントや解決策も記録する
- Djangoの「Don't Repeat Yourself (DRY)」原則を意識する