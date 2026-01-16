---
title: 開発環境現状確認 2026
tags: []
categories: []
date: '2026-01-31'
draft: true
---
開発環境現状確認という記事を書くのが流行っていそうな雰囲気だったので私も便乗します。

## OS
openSUSE TumbleweedというLinuxディストリビューションを使用しています。Windows11→Manjaro→Kubuntu→いろいろ→Ubuntuときて、結果的にopenSUSEに落ち着きました。

## デスクトップ環境
デスクトップ環境はKDE Plasma 6を使い続けています。KDEは動作も軽量で見た目も近代的で、もうWindowsを超えてるのではないか？というくらい完成度が高いなと感じています。また、KDE Connectというスマホとの連携機能がかなり優秀なのも良いです。

## ブートローダー
デフォルトではGRUB2-BLSになっていますが、GRUB2-BLSではデュアルブートがうまくいかない（Windowsが検知されない）例が多く報告されているので、Systemd-bootを使っています。シンプルな感じで良いです。

<!-- ## Wayland
ログインの際に、セッションをX11からWaylandにしておきます。なんとなくWaylandのほうがウインドウの動きなどが軽快です。 -->

## fcitx5-mozc
日本語入力はデフォルトではibus-mozcが入っているのかな？と思いますが、Fcitx5のほうがWaylandとの相性がいいのでインストールし変更します。ただ、TumbleweedのFcitz5はなぜか5.1.13で更新が止まっていて、これがかなりのバクを含むバージョンなため、個人でビルドしインストールします。私は過去にビルドした5.1.14のものを使いまわしました。なかなかいい感じです。

### Noto Sans CJK JP
日本語フォントは安定のNoto Sans CJK JPをインストールし、KDEの設定から変更します。読みやすくて良いです。

### Zsh & Starship
シェルはZsh、そのカスタマイズにはStarshipを導入します。前にも書いたので詳しくは[この記事](https://www.sandyman.dev/posts/portable-ssd-ubuntu/)を見てください。

### Konsole
ターミナルエミュレータはKDE標準搭載のKonsoleをそのまま利用します。最近、GhosttyやWeztermというやつらが流行っているらしいですが、デフォルトのこれが十分高機能な（気がする）のでKonsoleを使います。

### Microsoft Edge
ブラウザはMicrosoft Edgeをインストールします。なんとなくChromeは使いたくないが、Firefoxは非対応サイトがあるし...の結果、Edgeに落ち着きました。Chromeより機能も充実していて割と軽いのでおすすめです。

### Visual Studio Code
エディタはVisual Studio Codeをインストールします。最近はCursorやAntigravity等のAIエディタが流行っているような気がしますが、そこはあえて

### mise
