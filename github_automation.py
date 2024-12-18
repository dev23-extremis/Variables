# import os
# import subprocess
# import datetime

# def run_command(command):
#     """Run a shell command and return the output."""
#     result = subprocess.run(command, shell=True, capture_output=True, text=True)
#     if result.returncode != 0:
#         raise Exception(f"Command failed: {result.stderr.strip()}")
#     return result.stdout.strip()

# def create_github_repo(repo_name, description):
#     """Create a new GitHub repository using GitHub CLI."""
#     print(f"Creating GitHub repository '{repo_name}'...")
#     # Corrected the gh command to use the right format
#     run_command(f'gh repo create "{repo_name}" --public --description "{description}"')
#     print("Repository created successfully!")


# def initialize_git():
#     """Initialize Git and commit changes."""
#     print("Initializing Git repository...")
#     if not os.path.exists(".git"):
#         run_command("git init")
#     run_command("git add .")
#     commit_message = f"Initial commit on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
#     run_command(f'git commit -m "{commit_message}"')
#     print("Git repository initialized and changes committed.")

# def push_to_github(repo_name):
#     """Push the local repository to GitHub."""
#     print("Setting remote repository URL...")
#     # Set the remote repository URL
#     run_command(f"git remote add origin https://github.com/dev23-extremis/{repo_name}.git")
#     print("Pushing code to GitHub...")
#     run_command("git branch -M main")
#     run_command("git push -u origin main")
#     print("Code pushed to GitHub successfully!")


# def generate_summary():
#     """Generate a summary of the Git log and save it to a file."""
#     print("Generating work summary...")
#     log = run_command("git log --oneline")
#     with open("work-summary.txt", "w") as summary_file:
#         summary_file.write(log)
#     print("Work summary saved in 'work-summary.txt'.")

# def main():
#     repo_name = input("Enter the name for your GitHub repository: ").strip()
#     description = input("Enter a description for your repository: ").strip()

#     try:
#         # Step 1: Create a new GitHub repository
#         create_github_repo(repo_name, description)

#         # Step 2: Initialize Git and commit changes
#         initialize_git()

#         # Step 3: Push code to GitHub
#         push_to_github(repo_name)

#         # Step 4: Generate a summary of work
#         generate_summary()

#         print("\n✅ Automation complete! Repository created, code pushed, and summary generated.")
#     except Exception as e:
#         print(f"❌ Error: {e}")

# if __name__ == "__main__":
#     main()

# import os
# import subprocess
# import datetime

# def run_command(command):
#     """Run a shell command and return the output."""
#     result = subprocess.run(command, shell=True, capture_output=True, text=True)
#     if result.returncode != 0:
#         raise Exception(f"Command failed: {result.stderr.strip()}")
#     return result.stdout.strip()

# def sanitize_repo_name(repo_name):
#     """Replace spaces with dashes to make the repository name valid."""
#     return repo_name.strip().replace(" ", "-")

# def create_github_repo(repo_name):
#     """Create a new GitHub repository using GitHub CLI."""
#     print(f"Creating GitHub repository '{repo_name}'...")
    
#     sanitized_name = sanitize_repo_name(repo_name)  # Sanitize the repository name
    
#     # Create the repository on GitHub without the description
#     command = f'gh repo create {sanitized_name} --public'
#     run_command(command)
#     print("Repository created successfully!")
#     return sanitized_name

# def create_readme(repo_name, description):
#     """Create a README.md file with repository details."""
#     print("Creating README.md file...")
#     with open("README.md", "w") as readme_file:
#         readme_file.write(f"# {repo_name}\n\n{description}\n")
#     print("README.md file created successfully!")

# def initialize_git():
#     """Initialize Git and commit changes."""
#     print("Initializing Git repository...")
#     if not os.path.exists(".git"):
#         run_command("git init")
#     run_command("git add .")
#     commit_message = f"Initial commit on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
#     run_command(f'git commit -m "{commit_message}"')
#     print("Git repository initialized and changes committed.")

# def push_to_github(repo_name):
#     """Push the local repository to GitHub."""
#     print("Setting remote repository URL...")

#     # Check if remote 'origin' already exists and remove it
#     try:
#         run_command("git remote remove origin")
#         print("Removed existing 'origin' remote.")
#     except Exception as e:
#         print(f"No 'origin' remote found: {e}")

#     # Set the remote repository URL
#     run_command(f"git remote add origin https://github.com/dev23-extremis/{repo_name}.git")
#     print("Pushing code to GitHub...")
#     run_command("git branch -M main")
#     run_command("git push -u origin main")
#     print("Code pushed to GitHub successfully!")

# def generate_summary():
#     """Generate a summary of the Git log and save it to a file."""
#     print("Generating work summary...")
#     log = run_command("git log --oneline")
#     with open("work-summary.txt", "w") as summary_file:
#         summary_file.write(log)
#     print("Work summary saved in 'work-summary.txt'.")

# def main():
#     repo_name = input("Enter the name for your GitHub repository: ").strip()
#     description = input("Enter a description for your repository: ").strip()

#     try:
#         # Step 1: Create a new GitHub repository
#         sanitized_name = create_github_repo(repo_name)

#         # Step 2: Create a README.md file with description
#         create_readme(sanitized_name, description)

#         # Step 3: Initialize Git and commit changes
#         initialize_git()

#         # Step 4: Push code to GitHub
#         push_to_github(sanitized_name)

#         # Step 5: Generate a summary of work
#         generate_summary()

#         print("\n✅ Automation complete! Repository created, code pushed, and summary generated.")
#     except Exception as e:
#         print(f"❌ Error: {e}")

# if __name__ == "__main__":
#     main()

import os
import subprocess
import datetime

def run_command(command):
    """Run a shell command and return the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {result.stderr.strip()}")
    return result.stdout.strip()

def sanitize_repo_name(repo_name):
    """Replace spaces with dashes to make the repository name valid."""
    return repo_name.strip().replace(" ", "-")

def create_github_repo(repo_name):
    """Create a new GitHub repository using GitHub CLI."""
    print(f"Creating GitHub repository '{repo_name}'...")
    
    sanitized_name = sanitize_repo_name(repo_name)  # Sanitize the repository name
    
    # Create the repository on GitHub without the description
    command = f'gh repo create {sanitized_name} --public'
    run_command(command)
    print("Repository created successfully!")
    return sanitized_name

def create_readme(repo_name, description):
    """Create a README.md file with repository details."""
    print("Creating README.md file...")
    with open("README.md", "w") as readme_file:
        readme_file.write(f"# {repo_name}\n\n{description}\n")
    print("README.md file created successfully!")

def initialize_git():
    """Initialize Git and commit changes."""
    print("Initializing Git repository...")

    # Add github_automation.py to .gitignore to avoid pushing it to GitHub
    with open(".gitignore", "a") as gitignore_file:
        gitignore_file.write("github_automation.py\n")
    print("github_automation.py added to .gitignore.")

    if not os.path.exists(".git"):
        run_command("git init")
    run_command("git add .")
    commit_message = f"Initial commit on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    run_command(f'git commit -m "{commit_message}"')
    print("Git repository initialized and changes committed.")

def push_to_github(repo_name):
    """Push the local repository to GitHub."""
    print("Setting remote repository URL...")

    # Check if remote 'origin' already exists and remove it
    try:
        run_command("git remote remove origin")
        print("Removed existing 'origin' remote.")
    except Exception as e:
        print(f"No 'origin' remote found: {e}")

    # Set the remote repository URL
    run_command(f"git remote add origin https://github.com/dev23-extremis/{repo_name}.git")
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
        sanitized_name = create_github_repo(repo_name)

        # Step 2: Create a README.md file with description
        create_readme(sanitized_name, description)

        # Step 3: Initialize Git and commit changes
        initialize_git()

        # Step 4: Push code to GitHub
        push_to_github(sanitized_name)

        # Step 5: Generate a summary of work
        generate_summary()

        print("\n✅ Automation complete! Repository created, code pushed, and summary generated.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()





