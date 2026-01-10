---
title: 2026年版、openSUSE Tumbleweedの個人的環境構築
tags: []
categories: []
date: '2026-01-31'
draft: true
---
いろいろあってOSを再インストールすることになったので、個人的なセットアップ方法を簡単にまとめてみます。インストールするOSは私の好きなopenSUSE Tumbleweedです。

## OSインストール編
### KDE Plasma 6
デスクトップ環境はKDE Plasma 6を選択します。KDEは動作も軽量で見た目も近代的、もうWindowsを超えてるのではないか？というくらい完成度が高く、ずっと愛用しています。また、KDE Connectというスマホとの連携機能がかなり優秀なのも良いです。

### Systemd-boot
デフォルトではGRUB2-BLSになっていると思いますが、GRUB2-BLSではデュアルブートがうまくいかない（Windowsが検知されない）例が多く報告されているので、今回はSystemd-bootにします。シンプルな感じで良いです。

## インストール後
### Wayland
ログインの際に、セッションをX11からWaylandにしておきます。なんとなくWaylandのほうがウインドウの動きなどが軽快です。

### fcitx5-mozc
日本語入力はデフォルトではibus-mozcが入っているのかな？と思いますが、Fcitx5のほうがWaylandとの相性がいいのでインストールし変更します。ただ、TumbleweedのFcitz5はなぜか5.1.13で更新が止まっていて、これがかなりのバクを含むバージョンなため、個人でビルドしインストールします。私は過去にビルドした5.1.14のものを使いまわしました。なかなかいい感じです。

### Noto Sans CJK JP
日本語フォントは安定のNoto Sans CJK JPをインストールし、KDEの設定から変更します。読みやすくて良いです。

### Zsh & Starship

### Konsole

### Microsoft Edge

### Visual Studio Code

### mise
