---
date: "2023-03-28"
title: "【備忘録】UbuntuでLinuxカーネルをビルドしてみたときの手順"
thumbnail: "images/programming2.webp"
tags: ["Linux", "カーネル", "ビルド"]
categories: ["Linux"]
draft: false
archives: ["2023/03"]
toc: true
emoji: "🐧"
description: "Ubuntu系でLinuxカーネルをビルドしてみたときの手順等をまとめた記事です。カーネルのソースコードからビルドしました。"
---

## はじめに
自分でLinuxカーネルをビルドしてみたときの手順などをまとめてみました。結構苦戦したので残しておきます。

## 実行環境
- Ubuntu 22.04.1 LTS (Linux.5.15)
- ThinkPad X1Carbon Gen10

## 手順
sources.list 内のdeb-srcをコメントアウトする。（#を外す）

下のコマンドを実行。
```bash
sudo apt install build-essential bison flex gnupg libncurses-dev libelf-dev libssl-dev wget && sudo apt build-dep
```
[kernel.org](http://kernel.org) から導入したいバージョンのソースコードをダウンロード。

`sudo tar xvf linux-x.xx.xx.tar.xz` みたいにいい感じに解凍する。

解凍したフォルダに移動する。

`cp /boot/config-$(uname -r) .config` を実行する。（今実行しているカーネルのコンフィグをコピーするコマンド）

`make oldconfig` を実行しとにかくエンター！！！

下のコマンドを実行！
```bash
scripts/config --disable SYSTEM_TRUSTED_KEYS
scripts/config --disable SYSTEM_REVOCATION_KEYS
```

`scripts/config --disable DEBUG_INFO &&`と `scripts/config --enable DEBUG_INFO_NONE` を実行する。

`make clean` する。

`make deb-pkg -j(CPUのスレッド数) LOCALVERSION=-xxxxx(何でも良い)`  を実行、終わると/home/usernameにdebファイルが保存されている。

念の為他のPCで動くか確認する。動いたら導入したいPCにインストール。

## まとめ
ということで、Linuxカーネルのビルド手順でした。ビルドするときの参考になれば幸いです。それではさようならーーーーーーーー！

## 参考にした記事など
[https://www.dwarmstrong.org/kernel/](https://www.dwarmstrong.org/kernel/)


[https://stackoverflow.com/questions/56149191/linux-latest-stable-compilation-cannot-represent-change-to-vmlinux-gdb-py](https://stackoverflow.com/questions/56149191/linux-latest-stable-compilation-cannot-represent-change-to-vmlinux-gdb-py)

[https://arch.jpn.org/archives/351](https://arch.jpn.org/archives/351)