# 🚀 GitHub Setup Guide (with SSH, Git Bash, and Python Projects)

````markdown
# 🚀 Git + GitHub Setup with SSH (Complete Workflow)

This guide walks you through how to fully configure Git, generate and use SSH keys, initialize a local project, and push it to GitHub — all with step-by-step terminal commands and explanations. Ideal for developers managing Python or C++ projects.

---
### 🔧 Step 1: Install Git

- Download Git: [https://git-scm.com/download/win](https://git-scm.com/download/win)
- During installation:
  - ✅ Choose **Git Bash** as default terminal
  - ✅ Allow Git from Command Prompt
  - ✅ (Optional) Add Git profile to Windows Terminal
  - Keep other settings as default

---

### 🔐 Step 2: Generate SSH Key

> SSH (Secure Shell) uses a key pair (public + private) to let your computer securely talk to GitHub without passwords.

In Git Bash, run:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
````

* Press Enter to accept the default file path: `~/.ssh/id_ed25519`
* You can set a passphrase or leave it blank (press Enter)

Then start the SSH agent and add your key:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

---

### 📋 Step 3: Add Public SSH Key to GitHub

Get your public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

1. Copy the whole output
2. Go to **GitHub → Settings → SSH and GPG Keys**
3. Click **New SSH key**
4. Paste the public key and give it a name (e.g., "My Laptop")

---

### ✅ Step 4: Test SSH Connection to GitHub

```bash
ssh -T git@github.com
```

* The first time, you'll be asked:
  *"Are you sure you want to continue connecting?"* → type `yes`

If everything works, you’ll see:

```
Hi your_username! You've successfully authenticated, but GitHub does not provide shell access.
```

---

### ⚙️ Step 5: Set Your Git Identity

Tell Git who you are (one-time):

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Verify with:

```bash
git config --global --list
```

---

### 📁 Step 6: Initialize Git in Your Local Project

Navigate to your project folder:

```bash
cd path/to/your/project
```

Then run:

```bash
git init
git add .
git commit -m "Initial commit"
```

This creates a local Git repository and saves the first snapshot of your code.

---

### 🌍 Step 7: Create a GitHub Repository

In your GitHub account:

1. Click the **+ New repository**
2. Set a name like `signal-lab`
3. Do **NOT** check “Initialize with README”
4. Click **Create repository**

---

### 🔗 Step 8: Connect Local Repo to GitHub via SSH

Run the following (replace with your GitHub username and repo name):

```bash
git remote add origin git@github.com:your_username/signal-lab.git
git branch -M main
git push -u origin main
```

This links your local repo to GitHub and pushes your first commit.

---

### 🔁 Step 9: Push Changes (Daily Workflow)

After making edits, repeat this process to save and upload changes:

```bash
git add .
git commit -m "Meaningful commit message"
git push
```

Optional tools:

```bash
git status   # See what's changed
git log      # View commit history
```

---

### 🚫 Step 10: Add .gitignore (Optional but Recommended)

Create a `.gitignore` file to exclude clutter:

```gitignore
# Python
__pycache__/
*.pyc

# Virtual environments
venv/

# Editor config
.vscode/
```

Then commit it:

```bash
git add .gitignore
git commit -m "Add .gitignore"
git push
```

---

✅ You're now fully set up with Git, SSH, and GitHub for coding projects!

```

---

Would you like me to generate a matching `README.md` that introduces your `signal-lab` project with a project goal, tech stack, learning roadmap, and weekly logs section too?
```
