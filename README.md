
# プロジェクト名

このプロジェクトは、Next.jsフロントエンドとFastAPIバックエンドを使用しています。

## セットアップ

1. フロントエンドのセットアップ:
   ```
   npx create-next-app frontend
   cd frontend
   npm install
   ```

2. バックエンドのセットアップ:
   ```
   cd backend
   poetry install
   ```

3. 環境変数の設定:
   `.env.example`をコピーして`.env`を作成し、必要な値を設定してください。

## 開発サーバーの起動

- フロントエンド: `cd frontend && npm run dev`
- バックエンド: `cd backend && poetry run uvicorn app.main:app --reload`

## ビルドと本番環境での実行

- フロントエンド:
  ```
  cd frontend
  npm run build
  npm run start
  ```

- バックエンド:
  ```
  cd backend
  poetry run uvicorn app.main:app
  ```

または、Docker Composeを使用:
docker-compose up

## テスト

- フロントエンド: `cd frontend && npm test`
- バックエンド: `cd backend && poetry run pytest`
