import os
import subprocess

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def create_project_structure():
    # プロジェクトのルートディレクトリ（現在のカレントディレクトリ）
    root = os.getcwd()

    # フロントエンド
    frontend = os.path.join(root, "frontend")
    # Next.jsプロジェクトの作成は手動で行うため、ここではディレクトリのみ作成
    create_directory(frontend)

    # バックエンド
    backend = os.path.join(root, "backend")
    create_directory(backend)
    create_directory(os.path.join(backend, "app"))
    create_directory(os.path.join(backend, "app", "api"))
    create_directory(os.path.join(backend, "app", "models"))
    create_directory(os.path.join(backend, "app", "schemas"))
    create_directory(os.path.join(backend, "tests"))

    # バックエンドのサンプルファイル
    write_file(os.path.join(backend, "app", "main.py"), """
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
""")

    write_file(os.path.join(backend, "pyproject.toml"), """
[tool.poetry]
name = "backend"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.9"
fastapi = "^0.68.0"
uvicorn = "^0.15.0"

[tool.poetry.dev-dependencies]
pytest = "^6.2.5"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
""")

    write_file(os.path.join(backend, ".flake8"), """
[flake8]
max-line-length = 88
extend-ignore = E203, E266, E501, W503
""")

    # Docker
    docker = os.path.join(root, "docker")
    create_directory(docker)

    write_file(os.path.join(docker, "frontend.Dockerfile"), """
FROM node:14

WORKDIR /app

COPY frontend/package*.json ./
RUN npm install

COPY frontend .

CMD ["npm", "run", "dev"]
""")

    write_file(os.path.join(docker, "backend.Dockerfile"), """
FROM python:3.9

WORKDIR /app

RUN pip install poetry

COPY backend/pyproject.toml backend/poetry.lock ./
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY backend .

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
""")

    # ルートディレクトリのファイル
    write_file(os.path.join(root, "docker-compose.yml"), """
version: '3'
services:
  frontend:
    build:
      context: .
      dockerfile: docker/frontend.Dockerfile
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
    environment:
      - NODE_ENV=development

  backend:
    build:
      context: .
      dockerfile: docker/backend.Dockerfile
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
    environment:
      - PYTHONUNBUFFERED=1
""")

    write_file(os.path.join(root, ".gitignore"), """
# Node.js
node_modules/
.next/

# Python
__pycache__/
*.pyc
.pytest_cache/

# Environment
.env

# IDEs
.vscode/
.idea/

# Misc
*.log
""")

    write_file(os.path.join(root, ".env.example"), """
FRONTEND_URL=http://localhost:3000
BACKEND_URL=http://localhost:8000
""")

    write_file(os.path.join(root, "README.md"), """
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
""")

    write_file(os.path.join(root, "CHANGELOG.md"), """
# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

- Initial project setup
""")

    write_file(os.path.join(root, "Makefile"), """
run-frontend:
	cd frontend && npm run dev

run-backend:
	cd backend && poetry run uvicorn app.main:app --reload

docker-up:
	docker-compose up

docker-down:
	docker-compose down
""")

    write_file(os.path.join(root, ".pre-commit-config.yaml"), """
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.4.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
-   repo: https://github.com/psf/black
    rev: 21.5b1
    hooks:
    -   id: black
-   repo: https://github.com/PyCQA/flake8
    rev: 3.9.2
    hooks:
    -   id: flake8
""")

    print("プロジェクト構造が生成されました。")
    print("Next.jsプロジェクトを作成するには、以下のコマンドを実行してください：")
    print("npx create-next-app frontend")

if __name__ == "__main__":
    create_project_structure()