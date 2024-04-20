---
title: "VPSのUbuntuでDirectusをホスティングしたときのメモ"
date: "2024-04-20"
tags: ["Ubuntu", "Directus", "ヘッドレスCMS"]
categories: ["Directus"]
draft: true
---

皆さんこんにちは！Sandyマンです。

先日、当ブログのコンテンツ管理をマークダウン+Gitから、ヘッドレスCMSの「Directus」へ移行してみました。Ubuntuでセルフホスティングして運用しているのですが、その際に日本語の情報がほとんどなかったので、軽く記録を残しておきます...。

## 参考サイト
- [Deploying Directus to an Ubuntu Server（Directus公式）](https://docs.directus.io/blog/deploy-directus-ubuntu-server.html)
- [Docker Guide（Directus公式）](https://docs.directus.io/self-hosted/docker-guide.html#example-docker-compose)
- [Configuration Options（Directus公式）](https://docs.directus.io/self-hosted/config-options.html)

基本的には公式の通りに実施すれば大丈夫でした。一番上の記事はUbuntu Serverが対象のものですが、Ubuntuでも問題なく進めることができました。

## docker-compose.ymlの設定
docker-compose.ymlの設定内容が、サイトによって結構違ったので少し悩みました。最終的には以下のようにしました。
```yml
version: '3'

services:
  db:
    image: postgis/postgis:13-master
    container_name: postgres
    ports:
      - 5432:5432
    volumes:
      - db-store:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: 'postgres'
      POSTGRES_USER: 'postgres'
      POSTGRES_DB: 'postgres'

  cache:
    image: redis:6

  directus:
    image: directus/directus:latest
    ports:
      - 8055:8055
    volumes:
      - ./extensions:/directus/extensions
    depends_on:
    - db
    - cache
    environment:
      KEY: "hogehogehogehoge"
      SECRET: "fugafugafugafuga"
      ADMIN_EMAIL: "admin@example.com"
      ADMIN_PASSWORD: "d1r3ctu5"
      DB_CLIENT: 'pg'
      DB_HOST: 'db'
      DB_PORT: '5432'
      DB_DATABASE: 'postgres'
      DB_USER: 'postgres'
      DB_PASSWORD: 'postgres'
      STORAGE_LOCATIONS: 'supabase'
      STORAGE_SUPABASE_DRIVER: 'supabase'
      STORAGE_SUPABASE_SERVICE_ROLE: 'service_role'
      STORAGE_SUPABASE_BUCKET: 'Directus'
      STORAGE_SUPABASE_PROJECT_ID: 'project_id'
      MAX_PAYLOAD_SIZE: '10mb'
      FILES_MAX_UPLOAD_SIZE: '10mb'
      WEBSOCKETS_ENABLED: 'true'
      CACHE_ENABLED: 'true'
      CACHE_STORE: 'redis'
      REDIS: 'redis://cache:6379'
      EXTENSIONS_AUTO_RELOAD: 'true'
      CACHE_AUTO_PURGE: 'true'
      EMAIL_FROM: ''aaaaa@aaaaa.com'
      EMAIL_TRANSPORT: 'smtp'
      EMAIL_SMTP_HOST: 'xxxxxx.aaaaa.com'
      EMAIL_SMTP_PORT: 'xxx'
      EMAIL_SMTP_USER: 'xxxxxxxx@xxxxx.com'
      EMAIL_SMTP_PASSWORD: 'piyopiyo'

volumes:
  db-store:
 ```
ファイルストレージにはSupabaseを利用してみました。今のところ、私の環境ではこれでしっかり動いています。

```
MAX_PAYLOAD_SIZE: '10mb'
FILES_MAX_UPLOAD_SIZE: '10mb'
```
の部分ですが、これを書いておかないと容量の大きい画像ファイルがアップロードできないので注意してください。

Emailのところは、パスワードを忘れた際の再設定などに必要です。

## まとめ
ということで、Directusをインストールしたときのメモでした。少しでも参考になると嬉しいです。それでは！

