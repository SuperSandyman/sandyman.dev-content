import os
from datetime import date
from pathlib import Path
from shutil import move

# Get the current date in YYYY-MM-DD format
def get_current_date():
    return date.today().isoformat()

# Function to create a new draft article
def create_article(slug):
    # Frontmatter for the article
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

    # Path for the draft article
    draft_path = Path(f"draft/{slug}/index.md")
    draft_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write the content to the file
    draft_path.write_text(frontmatter, encoding="utf-8")
    print(f"記事 '{slug}' が作成されました！ パス: {draft_path}")

# Function to publish an article
def publish_article(slug):
    # Path for the draft and published article
    draft_path = Path(f"draft/{slug}")
    publish_path = Path(f"posts/{slug}/index.md")

    # Check if the draft exists
    if not draft_path.exists():
        print(f"記事 '{slug}' は見つかりませんでした...。")
        return

    # Move the draft article to the posts directory
    publish_path.parent.mkdir(parents=True, exist_ok=True)
    move(str(draft_path), str(publish_path))

    # Get commit message from the user
    commit_message = input("コミットメッセージを入力してください: ")

    # Git commands to add, commit, and push the article
    os.system(f"git add {publish_path}")
    os.system(f'git commit -m "{commit_message}"')
    os.system("git push")

    print(f"記事 '{slug}' が公開されました！")

# Main function to handle user input
def main():
    action = input("行いたいアクションを入力してください ('create' or 'publish')： ").lower()
    slug = input("記事のslugを入力してください：").lower()

    if action == "create":
        create_article(slug)
    elif action == "publish":
        publish_article(slug)
    else:
        print("無効なアクションです。'create' または 'publish' を入力してください。")

if __name__ == "__main__":
    main()
