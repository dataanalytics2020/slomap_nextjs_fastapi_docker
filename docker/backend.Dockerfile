# Python 3.9をベースイメージとして使用
FROM python:3.9

# コンテナ内の作業ディレクトリを /app に設定
WORKDIR /app

# Poetryをインストール
RUN pip install poetry

# pyproject.toml と poetry.lock をコピー
# これらのファイルだけを先にコピーすることで、依存関係が変更されていない場合にキャッシュを活用できる
COPY backend/pyproject.toml backend/poetry.lock ./

# Poetryの設定を変更し、仮想環境を作成せずに直接システムにインストールするように指定
# その後、依存関係をインストール
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# バックエンドのソースコードをコピー
COPY backend .

# コンテナ起動時に実行されるコマンド
# Poetry経由でUvicornを使用してFastAPIアプリケーションを起動
# --host 0.0.0.0 でコンテナ外からのアクセスを許可
# --reload で開発時のコード変更を自動で反映
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]