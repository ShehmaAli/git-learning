# 🚀 Git Commands – Notes & Cheat Sheet

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

git status         # Show status of working directory and staging area
git diff           # View unstaged changes
git diff --staged  # View staged changes ready to commit

git log                            # Full commit log
git log --oneline                  # One-line summaries of commits
git log --graph                    # Visualize commit tree
git log -p                         # Show changes introduced by each commit
git log --stat                     # Show stats (files changed, insertions/deletions)

git reset --soft HEAD~1            # Undo last commit, keep staged changes
git reset --mixed HEAD~1           # Undo last commit, keep changes in working directory
git reset --hard HEAD~1            # Undo last commit, discard changes

```

Git push
# 📦 Git Push Cheat Sheet

`git push` is used to upload local repository content (commits, branches, tags) to a remote repository like GitHub.

---

## 🚀 Basic Syntax

```bash
git push [remote] [branch]
```
## Git push commands🎀

```bash
git push                          #Pushes to the remote branch set as upstream.                                   |
git push origin main              #Push `main` branch to the remote `origin`.                                     |
git push -u origin main           #Push `main` branch and set it as upstream for future pushes.                   |
git push origin dev               #Push `dev` branch to `origin`.                                                 |
git push --all                    #Push all branches to remote.                                                   |
git push origin --tags            #Push all local tags to the remote.                                             |
git push origin :branch-name      #Delete the remote branch named `branch-name`.                                  |
git push --force or git push -f   #Force push the current branch (overwrite remote history).                      |
git push origin HEAD              #Push the current local HEAD (current branch) to the remote with the same name. |
```
# 🔄 Git Pull Cheat Sheet

`git pull` is used to fetch and download content from a remote repository and immediately merge it with your local branch.

It’s effectively the same as:
```bash
git fetch
git merge
```

but git pull is more effective with greater and more handling

## basic format ⬇️
```bash
git pull [remote] [branch]
```

## ✨ git pull commands ✨

```bash
Command	                                     Description
git pull	                  #Pulls from the tracked upstream branch and merges it.
git pull origin main	          #Pulls from the main branch of the origin remote.
git pull --rebase	          #Fetches and rebases instead of merging. Keeps history linear.
git pull origin main --rebase	  #Pulls from main and rebases changes.
git pull --all	                  #Fetch and merge all branches from all remotes.
git pull --no-commit	          #Merge but don’t automatically commit the result.
git pull --ff-only	          #Only fast-forward if possible; otherwise, abort.
git pull --no-rebase	          #Ensures regular merge (disables rebasing).
```

till now this is it more will be added later
