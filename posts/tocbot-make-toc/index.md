---
date: "2023-09-23"
title: "Tocbotを使ってマークダウンブログに目次を実装"
tags: ["Tocbot", "Next.js", "ブログ"]
categories: ["Next.js"]
emoji: "🖨️"
---

## 概要
[Tocbot](https://github.com/tscanlin/tocbot)という目次を作成できるライブラリを使って、Next.js製マークダウンブログに目次機能を実装します。

## 実施環境
- Next.js 13.4
- App Router
- Tailwind CSS（JITモード使用）

## 導入
以下のコマンドを実行してTocbotをインストールします。Headingタグにidを付与するために、`rehype-slug`もインストールしておきます。（インストールしないと目次をクリックしても飛ばない）
```
npm install tocbot rehype-slug
```

## 実装
今回はこのブログを例に実装します。目次用のコンポーネント`Toc.tsx`を作成し以下のようにします。
```ts
"use client";

import { useEffect } from "react";
import tocbot from "tocbot";

export const Toc = () => {
    useEffect(() => {
        tocbot.init({
            // 目次を表示させたいところのクラス名
            tocSelector: ".toc",
            // どこから目次を作成するか
            contentSelector: ".prose",
            // どの見出しを目次にするか
            headingSelector: "h2, h3",
        });
        return () => tocbot.destroy();
    }, []);

    return (
        // tocSelectorの対象
        <div className="toc"></div>
    );
};
```

`useEffect`を使っているので、App Routerでは`"use client"`を先頭に書く必要があります。

目次の装飾は`tocSelector`で指定した要素にCSSを書いたりすればOKです。参考にこのブログのCSSを載せておきます。
```css
.toc {
    @apply px-2;
}

.toc-list-item {
    @apply py-1 text-gray-500;
}

.toc-list-item .toc-list {
    @apply pt-1 pl-3;
}

.is-active-link {
    @apply text-gray-950 font-bold;
}
```

## まとめ
こんな感じで目次を実装してみました。Tocbotを使うとかなり簡単に目次を実装することができるので、ぜひ導入してみてください。それでは！

