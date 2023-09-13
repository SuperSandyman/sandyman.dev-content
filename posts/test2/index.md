---
date: "2023-05-07"
title: "Vue×TypeScriptの基本についてまとめたかった！！！"
tags: ["React", "TypeScript", "JavaScript"]
categories: ["ブログ"]
archives: ["2023/05"]
toc: true
---

皆さんこんにちは。Sandyマンです。今回は、「React×TypeScriptの基本」ということでやっていこうと思います。それではやっていきます！

## なぜTypeScriptを使うのか？
JavaScript使えばいいじゃん、わざわざ記述量増やしてどうするの？って思うかもですが、TypeScriptの使用には結構メリットがあります。以下がそのメリットです。
- 型によるバグの事前検知
- IntelliSense（補完機能）による開発効率の向上
- 大規模プロジェクトの開発がしやすい

型があることによって実際に動かす前にエラーが検知できるので、バグを見つけやすくなります。また、JavaScriptに比べて補完もいい感じなので開発効率が結構上がります。

## どうやってReactで使うの？
プロジェクトを作るときに、TypeScriptを使うほうを選択すれば勝手にやってくれます。こんな感じで。
```shell
npx create-next-app --typescript myapp
```
これだけでTypeScriptのプロジェクトが完成します。簡単ですね！

## Reactで使うときの例
### Propsの型定義
Reactでは、Propsを利用して親コンポーネントから子コンポーネントへデータを渡します。TypeScriptを利用する場合は、Propsに対して型を指定する必要があります。こんな感じです。
```typescript
interface Props {
  text: string;
}

const MyComponent = (props: Props) => {
  return <div>{props.text}</div>;
};
```

### useStateの型定義
状態管理に使うuseStateの際の型定義をしてみます。こんな感じです。
```typescript
import React, { useState } from 'react';

interface MyComponentProps {
  text: string;
}

const MyComponent: React.FC<MyComponentProps> = ({ text }) => {
  const [count, setCount] = useState<number>(0);

  const handleClick = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <p>{text}</p>
      <p>{count}</p>
      <button onClick={handleClick}>Increment</button>
    </div>
  );
};
```

上の例は、useStateに対して型指定を行っています。useStateは、ジェネリクスによって型を受け取ります。このため、`useState<number>`と指定することで、状態の初期値として数値型を設定しています。

また、useStateから返される値の型は、常にタプル型です。最初の要素は状態の値であり、2番目の要素は状態を更新するための関数です。これらの要素に対して、それぞれ型定義を行うことができます。

### JSXの型定義
JSXの型定義はこんな感じです。
```typescript
import React from 'react'

const MyComponent: React.FC = () => {
  return <div>Hello, TypeScript!</div>;
};
```

上記の例では、React.FC型を利用して、関数コンポーネントを実装しています。React.FC型は、関数コンポーネントを定義するための型であり、Propsの型を受け取ることができます。Propsの型をジェネリクスとして指定することで、コンポーネントに渡されるPropsの型を正確に定義することができます。もし、Propsの型を受け取らない場合には、ジェネリクスを指定せずに利用することができます。

## まとめ
ということで今回は、ReactとTypeScriptの基本についてやってみました！皆さんも、ReactにTypeScriptを導入して最高の開発体験を手に入れてみてください！**コード量以上に効率が上がります！** それではさようならーーーーーーーー！

（記事に誤字や間違いがあったら教えてください）