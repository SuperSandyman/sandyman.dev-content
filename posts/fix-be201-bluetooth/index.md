---
slug: fix-be201-bluetooth
title: openSUSE TumbleweedでBluetoothが動作せず、スリープもできない問題の対処法
tags:
  - Linux
  - openSUSE
categories: []
date: '2026-01-05'
draft: false
---
8割くらいChatGPTに生成させました。内容は確認済みです。

## 症状
- スリープを実行しても数秒で画面が復帰する（サスペンドが失敗している）
- Bluetooth を有効化できない（`bluetoothctl` で `No default controller available`）

## 環境
- OS: openSUSE Tumbleweed 20260101（Windows 11とデュアルブート）
- Kernel: Linux 6.18.2-1-default
- PC: ThinkPad T14 Gen6 (Intel Lunar Lake)
- Wi-Fi, Bluetooth: Intel BE201

## 原因
- Intel Bluetooth（`btintel_pcie` / `0000:00:14.7`）が必要とするファームウェア `intel/ibt-0190-0291-iml.sfi` を読み込めず初期化失敗
- `.xz` の圧縮ファイルは存在するが、カーネルが読む非圧縮 `.sfi` が存在せず `Failed to load … (-2)` になっていた
- サスペンド時に Bluetooth が D3 へ移行できず `Timeout … for D3 entry` → `btintel_pcie_suspend returns -16` となり、サスペンド処理が中断された

## 解決方法
1. Intel BT firmware（`.xz`）を展開して非圧縮の `.sfi/.ddc` を作る
    ```bash
    cd /usr/lib/firmware/intel

    sudo xz -dk ibt-0190-0291-iml.sfi.xz
    sudo xz -dk ibt-0190-0291-pci.sfi.xz
    sudo xz -dk ibt-0190-0291-pci.ddc.xz
    sudo xz -dk ibt-0190-0291-usb.sfi.xz
    sudo xz -dk ibt-0190-0291-usb.ddc.xz
    sudo xz -dk ibt-0190-0291.sfi.xz
    sudo xz -dk ibt-0190-0291.ddc.xz
    ```

2. Bluetooth を再初期化して controller を復活させる
    ```bash
    sudo systemctl stop bluetooth.service

    sudo modprobe -r btintel_pcie btintel bluetooth 2>/dev/null || true
    sudo modprobe btintel_pcie

    sudo systemctl start bluetooth.service

    # controllerを確認（No default controller... が消える）
    bluetoothctl list
    bluetoothctl show
    ```

## まとめ
Bluetoothとスリープ関係で困っている人は試してみてください。それでは！
