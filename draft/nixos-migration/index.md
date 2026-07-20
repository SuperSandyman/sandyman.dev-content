---
title: "開発環境をNixOSに移行した"
tags: 
  - "NixOS"
  - "dotfiles"
  - "Nix"
  - "移行"
categories: 
  - "tech"
date: "2026-07-20"
draft: true
---

先日書いた[開発環境現状確認 2026](/posts/2026-dev-env/)では、openSUSE Tumbleweed + KDE Plasma 6 + mise + VSCodeという構成を紹介していました。あれから半年ほど経って、とうとうNixOSに開発環境を移行しました。元の環境から何が変わって、何を諦めて、何を手に入れたのかを書きます。

## 移行前の環境のおさらい

2026-dev-env記事の段階では、こんな構成でした。

- **OS**: openSUSE Tumbleweed（ローリングリリース）
- **デスクトップ環境**: KDE Plasma 6
- **ターミナル**: Konsole
- **シェル**: Zsh + Starship
- **エディタ**: VSCode（メイン）、Neovimには手を出せず
- **ブラウザ**: Microsoft Edge
- **開発ツール管理**: mise（nvm, fnm等の代替）
- **日本語入力**: Fcitx5（Tumbleweedのパッケージが古くて自前ビルド）
- **フォント**: Noto Sans CJK JP / Hack Nerd Font / Consolas

この状態で特に大きな不満はなかったんですが、いくつか気になる点が積み重なっていました。

### 移行を決意した理由

**再現性への不安**: openSUSE Tumbleweedはローリングリリースなので、アップデートのたびに「動かなくなるリスク」がありました。実際、Bluetoothが突然死んだり、Fcitx5のバージョンが古くてハマったり（その時の記事は[こちら](/posts/fix-be201-bluetooth/)）と、地味なトラブルが年に何度かありました。

**設定の散らばり**: Konsoleの設定、シェルのalias、miseのconfig、VSCodeのsettings.json、それぞれが別々の管理下にありました。バックアップはdotfilesリポジトリで一応まとめてはいたものの、「あれ、この設定どこに書いてあったっけ」になることがしばしば。

**miseの限界**: 言語ランタイムの管理はmiseで十分でしたが、システム全体のツール（NeovimとかLSP群とか）まで管理範囲を広げようとすると、どうしてもHomebrewなど他のパッケージマネージャと併用しないといけませんでした。そろそろ全部Nix式で管理したくなった、というのが正直なところです。

## NixOSの構成

というわけで、移行後の現在の構成です。

### 全体構成

システム側と開発環境側でflakeを分けることで、「OSは固定したまま開発ツールだけ更新したい」というユースケースを満たせるようにしています。

```text
flake.nix              # NixOS + Home Manager のエントリポイント
flake.lock
home.nix               # Home Manager の設定
nixos/
├── hosts/nixos/       # ホスト固有の設定
├── modules/
│   ├── base.nix       # 共通ベース設定
│   └── desktop.nix    # デスクトップ環境
└── nix-storage.nix    # ストレージ管理
profiles/
└── development/       # 開発環境（独立したflake）
    ├── flake.nix
    └── packages/
```

ハードウェア構成は以前と変わらず、Intel CPU + KDE Plasma 6 + Waylandの組み合わせです。

### NixOSの設定

**ベース（base.nix）**: ブートローダーはLimine（EFI）に変更しました。Tumbleweed時代はsystemd-bootを使っていましたが、NixOSに乗り換えるにあたりLimineの世代管理のしやすさを評価して選んでいます。Tailscaleも有効化していて、これは以前から使っていたものそのままです。

**デスクトップ（desktop.nix）**: ディスプレイマネージャーはSDDM（Wayland）で、KDE Plasma 6は継続です。日本語入力は引き続きFcitx5 + mozcですが、Tumbleweedで苦労した「パッケージが古い問題」はなくなりました。sessionVariablesでGTK_IM_MODULEやQT_IM_MODULEをまとめて設定するノウハウは、Tumbleweed時代に培ったものが活きています。

**ストレージ管理（nix-storage.nix）**: NixOS特有の課題である `/nix/store` の肥大化対策として、週次GC（14日より前の世代を削除）、空き容量しきい値5GB以下で自動GC起動などを設定しています。

### 移行前後での構成比較

変わったところと変わらなかったところをまとめます。

| 項目 | 移行前（openSUSE Tumbleweed） | 移行後（NixOS） |
|------|------|------|
| デスクトップ環境 | KDE Plasma 6 | KDE Plasma 6（変わらず） |
| シェル | Zsh + Starship | Zsh + Starship（変わらず） |
| ターミナル | Konsole | **Ghostty**（変更） |
| エディタ | VSCode | **VSCode + Neovim**（Neovim導入） |
| ブラウザ | Microsoft Edge | **Firefox + Microsoft Edge**（Firefox追加） |
| 開発ツール管理 | mise | **Nix profile**（変更） |
| 日本語入力 | Fcitx5 + mozc | Fcitx5 + mozc（変わらず） |
| フォント | Hack Nerd Font | Hack Nerd Font（変わらず） |
| 言語ランタイム | mise管理 | Nix管理（Node.js, Elixir, Rust等） |
| AI agent | Codex + Copilot | Codex + Copilot + OpenCode + Herdr（拡充） |

KDE Plasma 6やFcitx5 + mozcなど、気に入っている部分はそのまま移行しています。一方で、KonsoleからGhosttyに変えたり、VSCodeに加えてNeovimの設定を本格的に始めたりと、NixOSへの移行を機に思い切って変えたものもあります。

### 一番大きかった変化：miseからNix profileへ

以前はmiseで言語ランタイムを一元管理していました。mise自体は悪くなかったんですが、「Neovimのプラグイン管理はMason」「システムツールはHomebrew」という風に管理が分散してしまうのが気になっていました。

今回の移行で、言語ランタイムもLSPもフォーマッターも、**全部Nix式で統一**することにしました。Node.js（pnpm）、Elixir/Erlang、Rust/Cargo、GCC、typescript-language-server、elixir-ls、rust-analyzer...これらは全て `profiles/development/` のflakeで管理しています。

更新は次のコマンド一つで完了します。

```sh
nix flake update --flake ./profiles/development
nix profile upgrade development
```

以前miseを使っていた頃は `mise upgrade` していましたが、それとあまり変わらない手間で、しかもロックファイルでバージョンが固定される安心感があります。

### 新しく導入したもの

- **Ghostty**: Konsoleから乗り換え。透過/Breezeテーマで設定はNix管理下に。
- **Neovim**: 以前は「カスタマイズが面倒」と避けていましたが、設定をNixで管理できるならやってみようと導入。lazy.nvim + lazy-lock.json構成。
- **Firefox**: Edgeに加えてFirefoxも導入。NixOSでは設定も宣言的に管理できます。
- **AI agent周りの充実**: Codexに加えてOpenCode、HerdrなどもNix管理下に。

### 移行には至らなかったもの

- **VSCode**: やっぱり快適なので引き続きメインエディタです。Neovimはサブとして育てていく予定。
- **Microsoft Edge**: メインブラウザはEdgeのまま。Firefoxは検証用。

## 新規環境への導入

このdotfilesを使って新規NixOSマシンをセットアップする手順も用意しています。

```sh
git clone git@github.com:SuperSandyman/dotfiles.git ~/develop/dotfiles
cd ~/develop/dotfiles

# 開発環境プロファイルを先にインストール
nix profile add path:$PWD/profiles/development#default

# NixOS + Home Manager を適用
sudo nixos-rebuild test --flake path:$PWD#nixos
sudo nixos-rebuild switch --flake path:$PWD#nixos
```

以前のopenSUSE Tumbleweed時代には、OSのクリーンインストール後に「あれ、このツール入れてたっけ」と確認する手間が必ず発生していました。NixOSならflakeをcloneしてbuildするだけなので、そういうストレスはなくなりそうです。

## 移行してみての感想

### 変わらなかったこと、変わったこと

半年ほど前の記事で「Nixは面白そうではあるけど、安定した環境を構築するまでが難しそう」と書いていました。実際、最初の壁はやはり高かったです。Nix言語の学習、ドキュメントの読み解き方、エラーメッセージの意味を理解するまでにそれなりに時間がかかりました。

ただ、一度構成を作ってしまえば、その再現性と一貫性は想像以上でした。「あの時の環境、再現できる？」がflake.lock一つで完結するのは気持ちがいいです。

再現性以外だと、**設定が一箇所に集まる**のが地味に大きいです。Tumbleweed時代はKonsoleの設定はKonsoleのGUIで、シェルのaliasは.zshrcで、フォントの設定は各アプリごとに...と分散していましたが、今はNix式で全部を一箇所で見渡せます。

### まだ改善したいところ

- **Neovimの設定**: まだ入門したばかりなので、もう少し育てていきたい。
- **Ghosttyの設定**: 乗り換えたばかりでまだ試行錯誤中。
- **CIでのflakeチェック**: まだ整備できていないので、push時にflake checkが走るようにしたい。

## まとめ

ということで、[開発環境現状確認 2026](/posts/2026-dev-env/)で紹介したopenSUSE Tumbleweed環境からNixOSに移行した話でした。

まだ完成形とは言えず、これからもちょこちょこ改善していくつもりです。何か面白い知見があればまた書きます。
