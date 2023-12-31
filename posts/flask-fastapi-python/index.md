---
title: "ChatGPTに記事書かせたらどうなるのかやってみた？（FlaskとFastAPIの違いについて特徴などを比較）"
tags: ["ChatGPT", "AI生成", "Python", "Flask"]
categories: ["Python"]
archive: ["2023/02"]
date: "2023-02-15"
toc: true
thumbnail: "images/monitor.webp"
---

## はじめに
皆さんこんにちは。Sandyマンです。今回は、今流行っている「ChatGPT」、こいつを使ってPythonに関する記事を書かせてみました。一応内容は確認して軽く修正も加えてあるので、安心してください（？？？）それではどうぞ！！



...皆さんこんにちは。Sandyマンです！今回は、PythonでWeb系の開発だったりAPIの作成に使われるライブラリ「Flask」と「FastAPI」の違いについて調べてみました！どちらも記法も似ていて、使われることの多いライブラリなので、4つの項目で比較してみました！それではやっていきましょう！

## パフォーマンス
まずパフォーマンスですが、正直あまり大きな違いはないのかなと思います。FastAPI自体、Flaskの影響を受けているので少し軽量かもしれませんが、はっきりと体感できるような大きな違いはないと思います。FlaskからFastAPIにしてもパフォーマンスは大きくは変わらないと思っておいたほうがよさそうですね。

## ドキュメンテーション
FastAPIは、APIのドキュメンテーションを自動生成するためのツールを提供しています。これにより、開発者側はAPIの使用方法が簡単にわかり、メンテナンスや開発が簡単になるというメリットがあります。
一方、Flaskはドキュメンテーションの生成にデフォルトでは対応しておらず、他のライブラリなどをインストールする必要があります。標準搭載というのは大きいですね...！

## 型アノテーション
FastAPIは、Pythonの型アノテーションを活用することで、APIのリクエストやレスポンスについて、データ型を明確に示すことができます。これにより、APIの入力や出力について、開発者側は明確に理解することができ、開発体験が向上します。Flaskは、型アノテーションによるサポートは限られており、データ型について明示的に示すことが難しいです。FastAPIすごい！！

## コード量
さっきも言った通り、FastAPIとFlaskは血がつながっている感じなので、ほとんどコード量も変わりがありません。どっちを選んでもほぼ一緒だと思います。

## まとめ
以上のように、FlaskとFastAPIは、構文や機能などにおいていくつかの違いがあります。それぞれの特徴を理解し、プロジェクトのニーズに合わせて選択することが重要です。

...ということで、ChatGPTさんの記事でした。少し文章表現は変えましたが、ほとんど丸パクリしました。すごくないですか？たまに間違ったことを言ってるところもありますが、かなり優秀だなと思いました。AIが人間を超える日も近いのかもな、と思いましたね...。

次からは人間が書くのでよろしくお願いします（笑）それではさようならーーーーーーーー！
