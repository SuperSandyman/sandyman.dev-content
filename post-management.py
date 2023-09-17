import os
import subprocess
from datetime import date

def create_post():
    slug = input("記事のslugを入力してください: ")
    today = date.today().strftime("%Y-%m-%d")
    content = f'''---
date: "{today}"
title: ""
tags: [""]
categories: [""]
emoji: ""
---

'''

    post_directory = os.path.join("draft", slug)
    os.makedirs(post_directory, exist_ok=True)
    with open(os.path.join(post_directory, "index.md"), "w") as file:
        file.write(content)

def publish_post():
    slug = input("公開したい記事のslugを入力してください: ")
    post_directory = os.path.join("draft", slug)
    if not os.path.exists(post_directory):
        print(f"記事 '{slug}' は存在しません。")
        return

    target_directory = os.path.join("posts", slug)
    os.rename(post_directory, target_directory)
    
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f'"{slug} add"'])
    subprocess.run(["git", "push", "-u", "origin", "main"])

def edit_post():
    commit_message = input("コミットメッセージを入力してください: ")
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "push", "-u", "origin", "main"])

def main():
    print("1. 記事の作成")
    print("2. 記事の投稿")
    print("3. 記事の修正")
    choice = input("実行したい操作を選択してください (1/2/3): ")

    if choice == "1":
        create_post()
    elif choice == "2":
        publish_post()
    elif choice == "3":
        edit_post()
    else:
        print("無効な選択です。")

if __name__ == "__main__":
    main()
