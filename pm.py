import os
from datetime import datetime
from pathlib import Path
from shutil import move, rmtree

# Function to get the current date in YYYY-MM-DD format
def get_current_date():
    return datetime.now().date().isoformat()

# Function to create a new draft article
def create_article(slug, directory):
    # Set frontmatter based on the article type
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
            f"Your content here...\n"
        )
    else:  # For 'scraps'
        frontmatter = (
            f"---\n"
            f"date: \"{get_current_date()}\"\n"
            f"title: \"\"\n"
            f"---\n\n"
            f"# {slug}\n\n"
            f"Your content here...\n"
        )

    # Path for the draft article
    draft_path = Path(f"draft/{slug}/index.md")
    draft_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write the content to the file
    draft_path.write_text(frontmatter, encoding="utf-8")
    print(f"記事 '{slug}' が作成されました！ パス: {draft_path}")

# Function to publish an article
def publish_article(slug, directory):
    # Path for the draft and published article
    draft_path = Path(f"draft/{slug}/index.md")

    # Check if the draft exists
    if not draft_path.exists():
        print(f"記事 '{slug}' は見つかりませんでした...")
        return
    
    # Update draft to false and get the modified content (if posts)
    if directory == "posts":
        content = draft_path.read_text(encoding="utf-8").replace("draft: true", "draft: false")
    else:
        content = draft_path.read_text(encoding="utf-8")
    
    # Path for the published article
    publish_path = Path(f"{directory}/{slug}/index.md")
    publish_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write the updated content to the new location
    publish_path.write_text(content, encoding="utf-8")

    # Delete the draft
    rmtree(draft_path.parent)

    # Get commit message from the user
    commit_message = input("コミットメッセージを入力してください: ")

    # Git commands to add, commit, and push the article
    os.system(f"git add {publish_path}")
    os.system(f'git commit -m "{commit_message}"')
    os.system("git push")

    print(f"記事 '{slug}' が公開されました！ パス: {publish_path}")

# Main function to handle user input
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
