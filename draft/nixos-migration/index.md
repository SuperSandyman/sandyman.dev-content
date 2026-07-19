---
title: "NixOSに開発環境を移行した"
tags: 
  - "NixOS"
  - "dotfiles"
  - "Nix"
categories: 
  - "tech"
date: "2026-07-19"
draft: true
---

今年に入ってから少しずつ準備していたんですが、とうとう開発環境をNixOSに移行しました。dotfilesを整理するついでに、構成を一から組み直したのでその話を書きます。

## 動機

前々から「設定ファイルを宣言的に管理したい」「環境再現性を高めたい」と思っていました。Homebrew + mise + 各種dotfilesスクリプトでもそれなりに回せてはいたんですが、新マシンをセットアップするたびに「あれ、これ入れたっけ」になったり、バージョン差異でハマったりするのが地味にストレスでした。

NixOSはOSの構成からユーザーシェルの設定、開発ツールまで**全部Nix式で書ける**ところが魅力です。思い切って移行することにしました。

## 全体構成

今回のdotfilesは、更新目的の異なる2つのflakeで構成しています。

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

ハードウェア構成としては、Intel CPU + KDE Plasma 6 + Waylandの組み合わせです。GPUは特にゲーム用途ではないので、シンプルにIntel内蔵グラフィクスで運用しています。

## NixOSの設定

### ベース（base.nix）

ベース設定では、以下のような基本的なシステム構成を定義しています。

- **ブートローダー**: Limine (EFI)
- **カーネル**: Linux latest
- **ネットワーク**: NetworkManager
- **タイムゾーン**: Asia/Tokyo、ロケールは ja_JP.UTF-8
- **Nix機能**: flakes + nix-command の実験的機能を有効化
- **ユーザー**: sandyman（zsh、networkmanager/wheel groups）
- **Tailscale**: 有効化

Nixの設定ではflakeのlockファイルから常に再現可能になるよう、`keep-derivations`や`keep-outputs`はfalseにしています。代わりに週次GCで14日より古い世代を削除する運用です。

### デスクトップ（desktop.nix）

デスクトップは以下のような構成です。

- **ディスプレイマネージャー**: SDDM (Wayland)
- **デスクトップ環境**: KDE Plasma 6
- **サウンド**: PipeWire（ALSA, PulseAudio互換）
- **日本語入力**: fcitx5 + mozc
- **ロックスクリーン**: qylock（テーマは pixel-night-city）
- **ブラウザ**: Firefox + Microsoft Edge

日本語入力周りはfcitx5の環境変数をあちこちに設定しないと一部アプリで効かないので、`sessionVariables`でGTK_IM_MODULE、QT_IM_MODULE、XMODIFIERSなどをまとめて設定しています。これは試行錯誤の末にたどり着いた形ですね。

### ストレージ管理（nix-storage.nix）

NixOSを使っていると避けて通れないのが `/nix/store` の肥大化問題です。以下の対策を入れています。

- **自動GC**: 週次で14日より前の世代を削除
- **store最適化**: auto-optimise-store で重複ファイルを自動でハードリンク
- **空き容量しきい値**: 5GB以下でGCを起動、15GB超で停止
- **ブート世代制限**: systemd-bootの最大世代を10に制限

ちなみにLimineの方は `maxGenerations = 5` とさらに厳しめにしています。

## Home Managerの設定

NixOSのmoduleとしてHome Managerを統合しており、ユーザーランドの設定は `home.nix` に集約しています。

### シェル環境

普段使いはzsh、緊急用にbashも有効にしています。Aliasは全部モダンな置き換えに変えました。

```nix
ls = "eza --icons --group-directories-first";
ll = "eza --icons -la --group-directories-first";
grep = "rg";
cat = "bat --paging=never";
vi = "nvim";
```

プロンプトは Starship でカスタマイズして、カラフルなセグメント区切りに加えて、言語ランタイムのバージョン表示やDockerコンテキストがパッと見えるようにしています。

### インストールするツール

Home Manager側で入れるのは、あくまでシステムに密接に関わるものだけに絞っています。

- **ターミナル**: Ghostty (透過/Breezeテーマ、Hack Nerd Font)
- **フォント**: Hack Nerd Font、Inconsolata
- **ファイラ代替**: eza（テーマカスタム）+ zoxide（cd置き換え）
- **エディタ設定**: Neovimの設定ファイル群

Neovimの設定やGhosttyの設定は `xdg.configFile` で各ディレクトリに配置しています。init.luaはlazy.nvimでプラグインを管理していて、`lazy-lock.json`はNeovim側から書き変わるので、初回だけbootstrapで配置して以降は触らないようにしています。

### Codexの設定ファイル

AI agent周りもNix管理下に置いています。Codexのカスタムスキルはhome.fileで各スキルディレクトリを展開。ただしCodexの認証情報や履歴、セッションキャッシュは管理対象外です。

設定ファイル（config.toml）は**初回だけbootstrap**で配置するようにしていて、Codex Desktopから後で書き換えられても上書きしない仕組みです。このへんはHome Managerの `backupFileExtension` を設定して、既存ファイルを守るようにしています。

```nix
home.activation.bootstrapCodexConfig = lib.hm.dag.entryAfter [ "writeBoundary" ] ''
  if [[ ! -e "$HOME/.codex/config.toml" ]]; then
    run mkdir -p "$HOME/.codex"
    run install -m 0600 \
      ${./dot_codex/private_config.toml} \
      "$HOME/.codex/config.toml"
  fi
'';
```

## 開発環境プロファイル

### なぜNixOSとは別のflakeにしたか

OSの設定と開発ツールの更新頻度が違うからです。Node.jsやRustのマイナーアップデート、新しいLSPの追加などをいちいち `nixos-rebuild switch` したくないですよね。開発環境は独立したflakeとして、**nix profile** で管理しています。

### 中身

主な中身は以下のような感じです。

- **エディタ**: Neovim、VSCode
- **言語ランタイム**: Node.js（pnpm）、Elixir/Erlang、Rust/Cargo、GCC
- **LSP/フォーマッター**: typescript-language-server、elixir-ls、nil（Nix）、rust-analyzer、lua-language-server、nixfmt、prettier、stylua など
- **開発CLI**: ripgrep、fd、gh（GitHub CLI）、tree-sitter、wl-clipboard
- **AI agent**: Codex、GitHub Copilot CLI、OpenCode、Pi、Herdr
- **自作パッケージ**: hunkdiff、portless

注目ポイントは **miseとMasonを使わない** ことにした点です。ランタイムやLSPのインストール管理をNixに一本化することで、バージョンの管理場所が散らばらないようにしています。

### 更新方法

開発環境の更新は以下のコマンドだけです。

```sh
nix flake update --flake ./profiles/development
nix profile upgrade development
```

flake.lockを更新して `nix profile upgrade` するだけ。システム再起動も不要です。

逆にシステム側を更新したいときは、

```sh
nix flake update
sudo nixos-rebuild switch --flake path:$PWD#nixos
```

両方まとめて更新したいときはユーティリティも用意していて、

```sh
nix run path:.#update-all
```

これで両方のflake.lockを更新 + 開発環境プロファイルのupgradeまでやってくれます。

## 新規環境への導入

このdotfilesを使って新規NixOSマシンをセットアップする場合は3ステップです。

```sh
git clone git@github.com:SuperSandyman/dotfiles.git ~/develop/dotfiles
cd ~/develop/dotfiles

# 開発環境プロファイルを先にインストール
nix profile add path:$PWD/profiles/development#default

# NixOS + Home Manager を適用
sudo nixos-rebuild test --flake path:$PWD#nixos   # まず試す
sudo nixos-rebuild switch --flake path:$PWD#nixos  # 確定
```

最初に `test` でデスクトップやネットワークが問題なく動くか確認してから `switch` するのが安心です。Home ManagerもNixOS moduleとして統合されているので、`switch` 一発でホーム設定まで反映されます。

## 移行してみての感想

### よかったところ

**再現性が高い** のは想像通りでした。flake.lockで全てのバージョンが固定されるので、「この前動いたのに...」が激減しました。

**設定が一箇所に集まる** のも地味に大きいです。ターミナルの設定、シェルのalias、フォント、IMEの設定が全部Nix式で書かれていて、バラバラに管理していた頃と比べると見通しが格段に良くなりました。

**GCの自動化** は `/nix/store` の肥大化に対する精神衛生上とても良いです。昔Arch Linuxでpacmanのキャッシュを手動で掃除していた頃を思い出すと隔世の感があります。

### ハマったところ

**日本語入力の設定** はやはり面倒でした。fcitx5自体の設定は簡単なんですが、GTK/QtアプリごとにIM moduleの環境変数を適切に設定しないと一部で効かない現象がありました。特にElectronアプリ（VSCode、Edge）周りは地味に試行錯誤しています。

**Limine vs systemd-boot** の選択も少し迷いました。結局Limineをメインにしつつ、systemd-bootも世代管理用に併用する形に落ち着いています。

**開発環境の分離** は正解だったんですが、依存関係のトレースが少し面倒です。例えば `profiles/development/flake.nix` から参照している自作パッケージ（hunkdiff、portless）を変更した場合、開発環境プロファイルをre-buildし直す必要があります。これはまあ仕方ないですね。

## まとめ

NixOSへの移行は、正直なところ最初の壁は高いです。Nix言語の学習コスト、ドキュメントの豊富さ（nixpkgsは膨大ですが取っ掛かりが難しい）、エラーメッセージの読みにくさ、など乗り越えるべきものはいくつかあります。

ただ、一度構成を作ってしまえば、その再現性と一貫性は破壊的に便利です。「再インストール」が「flakeをcloneしてbuild」に変わるのは、体験としてかなり大きな差があります。

今回の構成はまだ完全に枯れたとは言えないので、これからもちょこちょこ改善していくつもりです。何か面白い知見があればまた書きます。
