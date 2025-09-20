#!/usr/bin/env python3
"""
Script to upload FukuiNet to Hugging Face Hub
"""

import os
import sys
from pathlib import Path

try:
    from huggingface_hub import HfApi, login
except ImportError:
    print("Error: huggingface_hub not installed. Run: uv add huggingface_hub")
    sys.exit(1)


def main():
    # Check for token
    token = os.getenv("HUGGINGFACE_HUB_TOKEN")
    if not token:
        print("Error: HUGGINGFACE_HUB_TOKEN environment variable not set")
        print("Get your token from: https://huggingface.co/settings/tokens")
        print("Then run: export HUGGINGFACE_HUB_TOKEN='your_token_here'")
        sys.exit(1)

    # Login
    try:
        login(token=token)
        print("✓ Successfully logged in to Hugging Face")
    except Exception as e:
        print(f"Error logging in: {e}")
        sys.exit(1)

    # Initialize API
    api = HfApi()

    # Repository details
    repo_id = "Nikolenko-Sergei/FukuiNet"
    
    # Create repository if it doesn't exist
    try:
        api.create_repo(repo_id=repo_id, exist_ok=True)
        print(f"✓ Repository {repo_id} is ready")
    except Exception as e:
        print(f"Error creating repository: {e}")
        sys.exit(1)

    # Files to upload
    files_to_upload = [
        "README.md",
        "model_card.md", 
        "pyproject.toml",
        ".gitattributes",
        "fukui_net/",
        "tests/",
        "models/final_model.ckpt"
    ]

    # Upload files
    print("\n📤 Uploading files...")
    for file_path in files_to_upload:
        if os.path.exists(file_path):
            try:
                if os.path.isfile(file_path):
                    api.upload_file(
                        path_or_fileobj=file_path,
                        path_in_repo=file_path,
                        repo_id=repo_id,
                        commit_message=f"Add {file_path}"
                    )
                    print(f"✓ Uploaded {file_path}")
                elif os.path.isdir(file_path):
                    api.upload_folder(
                        folder_path=file_path,
                        path_in_repo=file_path,
                        repo_id=repo_id,
                        commit_message=f"Add {file_path}/"
                    )
                    print(f"✓ Uploaded {file_path}/")
            except Exception as e:
                print(f"❌ Error uploading {file_path}: {e}")
        else:
            print(f"⚠️  File not found: {file_path}")

    print(f"\n🎉 Upload complete!")
    print(f"View your model at: https://huggingface.co/{repo_id}")


if __name__ == "__main__":
    main()
