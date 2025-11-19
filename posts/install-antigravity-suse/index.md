---
slug: install-antigravity-suse
title: openSUSEでAntigravityを使う
tags:
  - Linux
  - openSUSE
categories: []
date: '2025-11-19'
---
Google謹製のAIエディタ、[Antigravity](https://antigravity.google/)をopenSUSEにインストールする方法です。

## 手順
### リポジトリを /etc/zypp/repos.d に追加
```bash
sudo tee /etc/zypp/repos.d/antigravity.repo << 'EOL'
[antigravity-rpm]
name=Antigravity RPM Repository
enabled=1
autorefresh=1
baseurl=https://us-central1-yum.pkg.dev/projects/antigravity-auto-updater-dev/antigravity-rpm
gpgcheck=0
EOL
```

### パッケージキャッシュを更新
```bash
sudo zypper refresh
```

### パッケージをインストール
```bash
sudo zypper install antigravity
```

## まとめ
これでAntigravityが使えるよ！以上！！！
