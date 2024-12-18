import os
import subprocess
import datetime

def run_command(command):
    """Run a shell command and return the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {result.stderr.strip()}")
    return result.stdout.strip()

def create_github_repo(repo_name, description):
    """Create a new GitHub repository using GitHub CLI."""
    print(f"Creating GitHub repository '{repo_name}'...")
    # Corrected the gh command to use the right format
    run_command(f'gh repo create "{repo_name}" --public --description "{description}"')
    print("Repository created successfully!")


def initialize_git():
    """Initialize Git and commit changes."""
    print("Initializing Git repository...")
    if not os.path.exists(".git"):
        run_command("git init")
    run_command("git add .")
    commit_message = f"Initial commit on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    run_command(f'git commit -m "{commit_message}"')
    print("Git repository initialized and changes committed.")

def push_to_github():
    """Push the local repository to GitHub."""
    print("Pushing code to GitHub...")
    run_command("git branch -M main")
    run_command("git push -u origin main")
    print("Code pushed to GitHub successfully!")

def generate_summary():
    """Generate a summary of the Git log and save it to a file."""
    print("Generating work summary...")
    log = run_command("git log --oneline")
    with open("work-summary.txt", "w") as summary_file:
        summary_file.write(log)
    print("Work summary saved in 'work-summary.txt'.")

def main():
    repo_name = input("Enter the name for your GitHub repository: ").strip()
    description = input("Enter a description for your repository: ").strip()

    try:
        # Step 1: Create a new GitHub repository
        create_github_repo(repo_name, description)

        # Step 2: Initialize Git and commit changes
        initialize_git()

        # Step 3: Push code to GitHub
        push_to_github()

        # Step 4: Generate a summary of work
        generate_summary()

        print("\n✅ Automation complete! Repository created, code pushed, and summary generated.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
