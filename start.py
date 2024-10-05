from pathlib import Path
import shutil
import subprocess
import os

repo_path = Path('repo')
apk_path = repo_path / 'apk'
icon_path = repo_path / 'icon'

# Cleaning
shutil.rmtree(apk_path, ignore_errors=True)
shutil.rmtree(icon_path, ignore_errors=True)
apk_path.mkdir(parents=True)

# Move apk to repo/apk/
for apk in Path().glob('*.apk'):
    new_name = apk.name.replace("-release.apk", ".apk")
    apk.rename(apk_path / new_name)
    
# Copy repo.json
shutil.copy('repo.json', repo_path / 'repo.json')

# Use inspector to generate output.json
subprocess.call(["java", "-jar", "Inspector.jar", "repo/apk", "output.json", "tmp"])

# Create repo
subprocess.call(["python3", "create-repo.py"])
