import os, sys, shutil, subprocess

sys.stdout.reconfigure(encoding='utf-8')

dsa_dir = r"F:\dsa"
deepseek_src = r"F:\deepseek"
ds_src = r"F:\ds"

deepseek_dst = os.path.join(dsa_dir, "deepseek")
ds_dst = os.path.join(dsa_dir, "ds")

print("1. Copying F:\\deepseek to F:\\dsa\\deepseek...")
if os.path.exists(deepseek_dst):
    shutil.rmtree(deepseek_dst)
shutil.copytree(deepseek_src, deepseek_dst)

print("2. Copying F:\\ds to F:\\dsa\\ds...")
if os.path.exists(ds_dst):
    shutil.rmtree(ds_dst)
shutil.copytree(ds_src, ds_dst)

branch_name = "backup-deepseek-ds-dsa"

print(f"3. Creating and switching to git branch '{branch_name}'...")
subprocess.run(["git", "checkout", "-b", branch_name], cwd=dsa_dir, check=True)

print("4. Staging all files with git add . ...")
subprocess.run(["git", "add", "."], cwd=dsa_dir, check=True)

commit_msg = "Backup: Include deepseek, ds, and dsa folders"
print(f"5. Committing with message: '{commit_msg}'...")
subprocess.run(["git", "commit", "-m", commit_msg], cwd=dsa_dir, check=True)

print(f"6. Pushing branch '{branch_name}' to origin GitHub repository...")
subprocess.run(["git", "push", "-u", "origin", branch_name], cwd=dsa_dir, check=True)

print("============================================================")
print("SUCCESSFULLY COMMITTED & PUSHED ALL 3 FOLDERS (deepseek, ds, dsa)!")
print("============================================================")
