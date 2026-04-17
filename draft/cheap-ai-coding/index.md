---
slug: cheap-ai-coding
title: 月100ドルも払えない貧民のAIコーディング
tags:
  - AI
categories:
  - AI
date: '2026-04-24'
draft: true
---
Xをぼんやり眺めていると、Claude CodeやCodexに月200ドルを平気な顔してぶち込んでるやつをよく目にしますよね。なんか「海外はもう進んでる。AIにかける費用で\*\*大きな差\*\*が出る。(ｷﾘｯ)」とか言ってる~~クソみたいな驚き屋の~~投稿もよく見ます。

うっせえボケ！！！！！！！一般庶民が月200ドル、いや100ドルもAIに払えるわけねえだろ！！！！！！！！~~殺すぞ~~

ということで、今から月30ドル程度でなんとかコーディングエージェントを使う方法をまとめていきます。

## 契約するプラン
- Codex Plus 20ドル
- GitHub Copilot 10ドル

## Codexには計画作成だけさせる
Codexは計画の作成に使いましょう。GPT-5.4 High（もしくはMedium）あたりを使うのがおすすめです。

## 話したいならChatGPTを使う
計画を立てるときに話し合って考えていく場面もあると思いますが、そこでCodexを使うのはもったいないです。ChatGPTとCodexのリミットは別枠なので、ChatGPTのGPT-5.4 Thinkingとお話しましょう。そこでできたある程度のやつをCodexに持っていくと良いでしょう。

## 実装にはGitHub CopilotとCodexを併用
GitHub CopilotはGPT-5.4かGPT-5.4-miniがおすすめです。推論レベルは選択肢の中で最も高いやつにしましょう。GitHub Copilotはプレミアムリクエストという謎な制度を取っていて、一回のプロンプトでどんな重い処理をさせても値段が変わりません。10ドルのプランの場合、5.4だと月300回、miniだと月900回使えます。

CodexだとなんでもGPT-5.4に投げるのではなく、5.3-Codexや5.4-miniに投げることをおすすめします。5.4と5.3-Codexはコーディング性能にそこまで大きな違いはないですが、5.3-Codexのほうが使用可能な量が多いためおすすめです。

参考：[Pricing – Codex | OpenAI Developers](https://developers.openai.com/codex/pricing)

