---
date: "2023-05-08"
title: "Next.js×DockerのときなぜかTailwind CSSが使えない"
tags: ["Next.js", "Docker", "TailwindCSS"]
categories: ["React"]
archives: ["2023/05"]
emoji: "🧪"
toc: true
---

Next.jsとDockerを使用する際、なぜかTailwind CSSが効かないトラブル。いろいろ調べてみるが何もわからない...。Dockerfileなども変えてみたが何一つわからない...。お手上げである...。

## やったことリスト
- Tailwind CSSの再インストール
- パソコンの再起動
- プロジェクトの作り直し
- 公式テンプレの使用

## 結果
```shell
2023-05-08 22:56:15 warn - No utility classes were detected in your source files. If this is unexpected, double-check the `content` option in your Tailwind CSS configuration.
2023-05-08 22:56:15 warn - https://tailwindcss.com/docs/content-configuration
```

## まとめ
Dockerやめたい