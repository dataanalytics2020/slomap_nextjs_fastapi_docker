# Node.js version 14をベースイメージとして使用
FROM node:14

# コンテナ内の作業ディレクトリを /app に設定
WORKDIR /app

# package.json と package-lock.json をコピー
# これらのファイルだけを先にコピーすることで、依存関係が変更されていない場合にキャッシュを活用できる
COPY frontend/package*.json ./

# npm install を実行して依存関係をインストール
RUN npm install

# フロントエンドのソースコードをコピー
COPY frontend .

# コンテナ起動時に実行されるコマンド
# npm run dev で開発サーバーを起動
CMD ["npm", "run", "dev"]