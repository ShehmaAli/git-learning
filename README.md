# 🚀 Git Commit Commands – Notes & Cheat Sheet

A handy reference for all the **Git commit-related commands**. Ideal for beginners and experienced developers working with Git regularly.

---

## 🔧 Git Setup (One-Time)

Before committing, make sure to set your Git identity:
now these are the basic things I've learned till now

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"


git add <filename>        # Stage a specific file
git add .                 # Stage all files in the current directory (new + modified)
git add -A                # Stage all changes (including deletions)

git commit -m "Your commit message"      # Commit with a message
git commit -a -m "Quick commit"          # Automatically stage modified files and commit

git commit --amend                      # Modify last commit (interactive)
git commit --amend -m "New message"     # Change last commit message directly

git status         # Show status of working directory and staging area
git diff           # View unstaged changes
git diff --staged  # View staged changes ready to commit

git log                            # Full commit log
git log --oneline                  # One-line summaries of commits
git log --graph                    # Visualize commit tree
git log -p                         # Show changes introduced by each commit
git log --stat                     # Show stats (files changed, insertions/deletions)

git push                           # Push to default remote (usually origin)
git push origin main               # Push to a specific branch

git reset --soft HEAD~1            # Undo last commit, keep staged changes
git reset --mixed HEAD~1           # Undo last commit, keep changes in working directory
git reset --hard HEAD~1            # Undo last commit, discard changes
