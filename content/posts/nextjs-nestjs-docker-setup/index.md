---
date: "2023-05-05"
title: "Docker×Next.js×NestJS×PostgreSQLの環境構築をしてみる"
tags: ["Docker", "Next.js", "NestJS"]
categories: ["環境構築"]
archives: ["2023/05"]
toc: true
---

皆さんこんにちは。Sandyマンです。今回は、「Docker×Next.js×NestJS×PostgreSQL」の環境構築をしていきます！ それではやっていきましょう！
（Docker未経験なので間違ってるかもです...。）

## 必要なもの
- Docker Desktop or Docker CE
- WindowsならWSL2
- 好きなエディタ

Dockerをインストールしてない人はさっさと公式サイトに飛んでインストールしましょう！！

## 1.いろいろフォルダとかを作る
今回はWSL2上でDockerを使って、こんな感じで作ろうと思います。
```
my-app
┗frontend
┗backend
┗nginx
```
Nginxはリバースプロキシ用に入れてあります。それぞれ適当にmkdirして作っておきます。

## 2.Next.jsの環境構築
まず最初に、Next.jsの環境構築をしていきます。frontend内で、`npx create-next-app .`と打っていい感じにします。（いい感じとは）できたら、Dockerfileを作成して書き込んでいきます。内容はだいたいこんな感じです。~~まあChatGPTに丸投げしたんだけど~~
```
# ベースイメージとして公式のNode.jsイメージを指定
FROM node:18-alpine

# アプリケーションのディレクトリを設定
WORKDIR /app

# package.jsonとpackage-lock.jsonをコピー
COPY package*.json ./

# 依存関係のインストール
RUN npm install

# アプリケーションのソースコードをコピー
COPY . .

# アプリケーションのビルド
RUN npm run build

# ポート3000で実行
EXPOSE 3000

# アプリケーションの起動
CMD ["npm", "start"]
```

## 3.NestJSの環境構築
次は、NestJSのほうをやっていきます。NestJSの方のコマンドはこんな感じです。（backendディレクトリ内で実行）
```shell
npm install -g @nestjs/cli
nest new .
```
次にDockerfileを作成して書き込んでいきます。~~もちろんこれもChatGPT ~~
```
# ベースイメージとして公式のNode.jsイメージを指定
FROM node:18-alpine

# アプリケーションのディレクトリを設定
WORKDIR /app

# package.jsonとpackage-lock.jsonをコピー
COPY package*.json ./

# 依存関係のインストール
RUN npm install

# アプリケーションのソースコードをコピー
COPY . .

# ポート4000で実行
EXPOSE 4000

# アプリケーションの起動
CMD ["nest", "start"]
```

## 4.Nginxの環境構築
Nginxのリバースプロキシとか正直よくわからないんですけど、なんかやった方がいいらしいのでやっていきます。リバースプロキシについては、今度記事にしてまとめてみようと思います。

Nginxディレクトリの中に、nginx.confを作ります。作ったら下のように書き込んでいきます。
```
http {
    server {
        listen 80;
        server_name localhost;

        location / {
            proxy_pass http://frontend:3000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        location /api {
            proxy_pass http://backend:4000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```

ついでにDockerfileも作ります。一行だけ`FROM nginx:latest`とだけ書いておきましょう。

## 5.docker-compose.ymlの作成
では、docker-compose.ymlを作成していきます。（最近はcompose.yamlとかいうらしい）プロジェクトディレクトリ直下に、docker-compose.ymlを作成して書き込んでいきます。
```
version: '3'

services:
  frontend:
    container_name: my-app-frontend
    build: ./frontend
    command: npm run dev
    volumes:
      - ./frontend/src:/app/src
      - ./frontend/package.json:/app/package.json
      - ./frontend/package-lock.json:/app/package-lock.json
    ports:
      - "3000:3000"
    depends_on:
      - backend

  backend:
    container_name: my-app-backend
    build: ./backend
    command: npm run start:dev
    volumes:
      - ./backend/src:/app/src
      - ./backend/package.json:/app/package.json
      - ./backend/package-lock.json:/app/package-lock.json
    ports:
      - "4000:4000"
    depends_on:
      - db

  db:
    container_name: my-app-db
    image: postgres:latest
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - db-data:/var/lib/postgresql/data

  nginx:
    container_name: my-app-nginx
    build:
      context: ./nginx
      dockerfile: Dockerfile
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
    ports:
      - "80:80"
    depends_on:
      - frontend
      - backend

volumes:
  db-data:
```

## 6.動作確認
ここまで来たら、後は動かすだけです。`docker-compose up -d`で動かしてみましょう。いい感じにできたら成功です！

## まとめ
ということで、Dockerでの環境構築でした。Dockerは初めてで手探りでやってみたので、もしかしたら間違っているところがあるかもしれません（多分ある）もしあったら、ブログのリポジトリをGitHubで公開してるので、そちらに送ってくださると助かります！それではさようならーーーーーーーー！

GitHubのリンク
[https://github.com/SuperSandyman/sandyman-papermod-blog](https://github.com/SuperSandyman/sandyman-papermod-blog)


