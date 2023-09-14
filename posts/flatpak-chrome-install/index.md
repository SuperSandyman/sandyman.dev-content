---
date: "2022-12-15"
title: "Flatpakを使ってUbuntuにChromeをインストールする"
thumbnail: "images/chrome.webp"
tags: ["Chrome", "Linux", "Flatpak"]
categories: ["Linux"]
archives: ["2022/12"]
toc: true
aliases: ["/flatpak-chrome-install"]
emoji: "🎁"
---

## はじめに
私が普段使っているブラウザはFirefoxなのですが、グリーンチャンネルWebで香港国際競走を見ようとしたらなんとFirefoxに対応してませんでした！！これは大変だ！ということで、急遽レース開始の7分前くらいにChromeをインストールすることになったのですが、結構戸惑ったのでメモを残しておきます。

## 実施環境
- Kubuntu 22.04.1 (KubuntuとUbuntuはほぼ同じ)
- Linux 5.15
- ThinkPad X1 Carbon Gen10

## Flatpakでインストール
Google公式からdebファイルを落としてインストールすることもできたらしいのですが、Snap版Firefoxの仕様でなぜかダウンロードリンクが表示されなかったので、Flatpakでインストールすることにしました。

## Flatpakを導入しよう
まずはFlatpakを導入します。インストールのコマンドはこれです。
```
sudo apt install flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```
実行し終わったら、念の為再起動しておきます。

## Chromeをインストールする
それでは、Chromeをインストールしていきます。下のコマンドでChromeをインストールしていきます。
```
flatpak install flathub com.google.Chrome
```
インストールには少し時間がかかるので焦らず待ちましょう。インストールが終わったらどっかに追加されているはずです。これで競馬が見れますね！！~~あれもうレースはじまってる...~~

## まとめ
ということで、今回はChromeをインストールしてみました！他にもFlatpakでいろいろなソフトをインストールできるのでぜひ使ってみてください。ソフトウェアについてはここから見れます！[https://flathub.org/home](https://flathub.org/home)

それではさようならー！！





