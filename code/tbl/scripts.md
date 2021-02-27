# Scripts for Week 2

http://bit.ly/bangkit-s-form
Trisna Gelar ML - 0209

## List of Git Scripts

### basic config
```bash
    git config --global user.name ...
    git config --global user.email ....
```
### basic workflow
```bash
    git init 
    *git clone # from github
    git status

    git add ...
    git commit ...
    git commit -a -m "message"
    git log

    git push origin main
    *git pull 
```
### branch workflow
```bash
    git branch second-solution
    git checkout second-solution
    git add ..
    git commit ...
    git log
    git merge
```

### advance workflow
```bash
    git revert
    git head
```

### git shortcut
Add to .bashrc / .profile
```bash
alias ga='git add'
alias gaa='git add .'
alias gaaa='git add --all'
alias gau='git add --update'
alias gb='git branch'
alias gbd='git branch --delete '
alias gc='git commit'
alias gcm='git commit --message'
alias gcf='git commit --fixup'
alias gco='git checkout'
alias gcob='git checkout -b'
alias gcom='git checkout main'
alias gcos='git checkout staging'
alias gcod='git checkout develop'
alias gd='git diff'
alias gda='git diff HEAD'
alias gi='git init'
alias glg='git log --graph --oneline --decorate --all'
alias gld='git log --pretty=format:"%h %ad %s" --date=short --all'
alias gm='git merge --no-ff'
alias gma='git merge --abort'
alias gmc='git merge --continue'
alias gp='git pull'
alias gpr='git pull --rebase'
alias gr='git rebase'
alias gs='git status'
alias gss='git status --short'
alias gst='git stash'
alias gsta='git stash apply'
alias gstd='git stash drop'
alias gstl='git stash list'
alias gstp='git stash pop'
alias gsts='git stash save'

# ----------------------
# Git Functions
# ----------------------
# Git log find by commit message
function glf() { git log --all --grep="$1"; }
```
#### Reference
[Git Command-Line Shortcuts](https://jonsuh.com/blog/git-command-line-shortcuts/)

### FizzBuzz

README

#### Solution 1
```python fb01.py


```
#### Solution 2
```python fb02.py


```
#### Solution 3
```python fb03.py


```
## List of Troubleshoot & Debug Tools on Ubuntu

git, top, iotop, ionice, iftop, nice
bisect, ab, nice, renice, kill/killall, pprofile, kcachegrind, strace, netstat, valgrind, pdb3

```bash
sudo apt-get install --no-install-recommends -y git iotop iftop apache2-utils python3-pprofile kcachegrind net-tools valgrind 
```
