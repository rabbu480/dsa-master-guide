import os, sys, shutil, subprocess

sys.stdout.reconfigure(encoding='utf-8')

f_root = r"F:\\"
dsa_dir = r"F:\dsa"
deepseek_dup = os.path.join(dsa_dir, "deepseek")
ds_dup = os.path.join(dsa_dir, "ds")

print("1. Removing duplicated copies inside F:\\dsa...")
if os.path.exists(deepseek_dup):
    shutil.rmtree(deepseek_dup)
    print("   - Removed F:\\dsa\\deepseek")

if os.path.exists(ds_dup):
    shutil.rmtree(ds_dup)
    print("   - Removed F:\\dsa\\ds")

print("2. Configuring git safe.directory for F:/...")
subprocess.run(["git", "config", "--global", "--add", "safe.directory", "F:/"], capture_output=True)

print("3. Setting up clean root Git repo in F:\\...")
git_dsa = os.path.join(dsa_dir, ".git")
if os.path.exists(git_dsa):
    shutil.rmtree(git_dsa, ignore_errors=True)
    print("   - Removed nested F:\\dsa\\.git")

subprocess.run(["git", "init"], cwd=f_root, check=True)

remote_url = "https://github.com/rabbu480/dsa-master-guide.git"
subprocess.run(["git", "remote", "remove", "origin"], cwd=f_root, capture_output=True)
subprocess.run(["git", "remote", "add", "origin", remote_url], cwd=f_root, check=True)

branch_name = "backup-deepseek-ds-dsa"
subprocess.run(["git", "checkout", "-B", branch_name], cwd=f_root, check=True)

print("4. Staging original folders deepseek, ds, and dsa directly (NO DUPLICATION)...")
subprocess.run(["git", "add", "deepseek", "ds", "dsa"], cwd=f_root, check=True)

commit_msg = "Clean Backup: Track deepseek, ds, and dsa directly without duplication"
print(f"5. Committing to branch '{branch_name}'...")
subprocess.run(["git", "commit", "-m", commit_msg], cwd=f_root, check=True)

print(f"6. Force pushing branch '{branch_name}' to GitHub origin...")
subprocess.run(["git", "push", "-u", "origin", branch_name, "--force"], cwd=f_root, check=True)

print("============================================================")
print("CLEAN NO-DUPLICATION GIT SETUP COMPLETE & PUSHED TO GITHUB!")
print("============================================================")
