# Fix GitHub 403 by switching repository to SSH authentication

# 1. Check if an SSH key already exists
ls ~/.ssh

# 2. If id_ed25519 does NOT exist, generate a new SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# 3. Start the SSH agent
eval "$(ssh-agent -s)"

# 4. Add the key to the agent
ssh-add ~/.ssh/id_ed25519

# 5. Print the public key (copy this output)
cat ~/.ssh/id_ed25519.pub

# 6. Manually add the copied key to GitHub:
# https://github.com/settings/keys

# 7. Check current git remote
git remote -v

# 8. Change remote to SSH
git remote set-url origin git@github.com:USER/REPO.git

# 9. Test SSH authentication
ssh -T git@github.com

# 10. Push again
git push -u origin main
