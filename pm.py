import os
from datetime import datetime
from pathlib import Path
from shutil import move

def get_current_date():
    return datetime.now().date().isoformat()

def create_article(slug, directory):
    # フロントマターを設定
    if directory == "posts":
        frontmatter = (
            f"---\n"
            f"title: \"\"\n"
            f"date: \"{get_current_date()}\"\n"
            f"tags: [\"\"]\n"
            f"categories: [\"\"]\n"
            f"draft: true\n"
            f"---\n\n"
            f"# {slug}\n\n"
            f"内容をここに書いてください。\n"
        )
    else:  # 'scraps'用
        frontmatter = (
            f"---\n"
            f"date: \"{get_current_date()}\"\n"
            f"title: \"\"\n"
            f"---\n\n"
            f"# {slug}\n\n"
            f"内容をここに書いてください。\n"
        )

    draft_path = Path(f"draft/{slug}/index.md")
    draft_path.parent.mkdir(parents=True, exist_ok=True)
    draft_path.write_text(frontmatter, encoding="utf-8")
    print(f"記事 '{slug}' が作成されました。パス: {draft_path}")

def publish_article(slug, directory):
    draft_path = Path(f"draft/{slug}")
    draft_index_path = draft_path / "index.md"
    
    if not draft_index_path.exists():
        print(f"記事 '{slug}' は見つかりませんでした。")
        return

    # コンテンツを読み込み、公開状態に設定
    content = draft_index_path.read_text(encoding="utf-8")
    if directory == "posts":
        content = content.replace("draft: true", "draft: false")
    draft_index_path.write_text(content, encoding="utf-8")

    # ディレクトリを公開フォルダに移動
    publish_path = Path(directory) / slug

    # 既存のディレクトリのチェック
    if publish_path.exists():
        print(f"公開パス '{publish_path}' ですでに存在しています。名前を変更するか削除してください。")
        return

    publish_path.parent.mkdir(parents=True, exist_ok=True)
    move(str(draft_path), str(publish_path))

    commit_message = input("コミットメッセージを入力してください: ")
    os.system(f"git add {publish_path}")
    os.system(f'git commit -m "{commit_message}"')
    os.system("git push")

    print(f"記事 '{slug}' が公開されました。パス: {publish_path}")

def main():
    action = input("行いたいアクションを入力してください ('create' or 'publish')： ").lower()
    slug = input("記事のslugを入力してください：").lower()
    article_type = input("記事の種類を選択してください ('posts' or 'scraps')： ").lower()

    if article_type not in ["posts", "scraps"]:
        print("無効な記事の種類です。'posts' または 'scraps' を選択してください。")
        return

    if action == "create":
        create_article(slug, article_type)
    elif action == "publish":
        publish_article(slug, article_type)
    else:
        print("無効なアクションです。'create' または 'publish' を入力してください。")

if __name__ == "__main__":
    main()