---
title: "外付けSSDにUbuntuをインストールして開発環境を作ろう"
date: "2024-11-05"
tags: ["Ubuntu", "Linux"]
categories: ["Linux"]
draft: false
---

実機でUbuntuを使いたいけど、デュアルブートは怖いしWindowsを消したくはない...。と思って調べていると、こんな記事を発見。

[Windows PCに安定したネイティブLinux環境を構築する方法](https://zenn.dev/karaage0703/articles/0ca67e19aa772e)

これいいじゃん！ということで、外付けSSDにUbuntuをインストールして開発環境を作ってみました。

## 実施環境
- ThinkPad X1 Carbon Gen10 （Win11をインストール済）
- SK hynix SSD Tube T31 512GB
- インストーラー用のUSBメモリ

外付けSSDはAmazonで安かったSK hynixのやつです。今のところしっかり動作しています。

## 手順
1. ISOを落としてRufusとかでブートディスクを作る
2. ブートメニューでUSBメモリを選択して起動
3. インストールする

基本的には普通にインストールすれば良いですが、**インストール先のSSDの選択には気をつけましょう**。間違うとWindowsが抹消されてしまいます...。

## インストール後の設定
以下、インストール後に実施した設定などを書いておきます。

### ディレクトリ名を英語に変更
「ダウンロード」や「ドキュメント」みたいなやつを英語に変更します。
```sh
LANG=C xdg-user-dirs-gtk-update
```

### ZshをインストールしStarshipを導入
Zshをインストールして、Starshipというターミナルを超かっこよくできるツールを導入します。まずはZshの導入から。
```sh
sudo apt install zsh
chsh -s $(which zsh)
```

次にStarshipの導入。私はCargoを使ったのですが、スクリプトのほうが簡単そうなのでそちらを書いておきます。
```sh
curl -sS https://starship.rs/install.sh | sh
```

そしたら`~/.zshrc`の最後に以下を追記します。
```sh
eval "$(starship init zsh)"
```

これでターミナルを立ち上げ直すと、ちょっとカラフルになってるはずです。もっとイケてる感じにしたいので、プリセットを導入します。（その前にNerd Fontを導入してね！めんどいから書かないけど）今回はTokyo Nightというプリセットを例にします。
```sh
starship preset tokyo-night -o ~/.config/starship.toml
```

`~/.config/starship.toml`に以下の内容を書き込みます。
```toml
format = """
[░▒▓](#a3aed2)\
[  ](bg:#a3aed2 fg:#090c0c)\
[](bg:#769ff0 fg:#a3aed2)\
$directory\
[](fg:#769ff0 bg:#394260)\
$git_branch\
$git_status\
[](fg:#394260 bg:#212736)\
$nodejs\
$rust\
$golang\
$php\
[](fg:#212736 bg:#1d2230)\
$time\
[ ](fg:#1d2230)\
\n$character"""

[directory]
style = "fg:#e3e5e5 bg:#769ff0"
format = "[ $path ]($style)"
truncation_length = 3
truncation_symbol = "…/"

[directory.substitutions]
"Documents" = "󰈙 "
"Downloads" = " "
"Music" = " "
"Pictures" = " "

[git_branch]
symbol = ""
style = "bg:#394260"
format = '[[ $symbol $branch ](fg:#769ff0 bg:#394260)]($style)'

[git_status]
style = "bg:#394260"
format = '[[($all_status$ahead_behind )](fg:#769ff0 bg:#394260)]($style)'

[nodejs]
symbol = ""
style = "bg:#212736"
format = '[[ $symbol ($version) ](fg:#769ff0 bg:#212736)]($style)'

[rust]
symbol = ""
style = "bg:#212736"
format = '[[ $symbol ($version) ](fg:#769ff0 bg:#212736)]($style)'

[golang]
symbol = ""
style = "bg:#212736"
format = '[[ $symbol ($version) ](fg:#769ff0 bg:#212736)]($style)'

[php]
symbol = ""
style = "bg:#212736"
format = '[[ $symbol ($version) ](fg:#769ff0 bg:#212736)]($style)'

[time]
disabled = false
time_format = "%R" # Hour:Minute Format
style = "bg:#1d2230"
format = '[[  $time ](fg:#a0a9cb bg:#1d2230)]($style)'
```

これで立ち上げ直すとかっこいいターミナルになってます。

### GNOMEを拡張機能を入れてWindows風に
ArcMenuとDash to Panelを導入しました。

## まとめ
最終的にこうなりました。

![カスタマイズ後のUbuntuデスクトップのスクリーンショット](my-ubuntu-desktop.png)

まあまあスタイリッシュで使い勝手も良く、安全にWindowsとも両立できているので、個人的には満足しています。外付けSSDにLinux、おすすめです。それでは！

## 参考リンク
- [Linuxのホーム内ディレクトリの英語化](https://zenn.dev/tasiten/articles/7727537e2e975e)
- [Starship](https://starship.rs/ja-JP/)