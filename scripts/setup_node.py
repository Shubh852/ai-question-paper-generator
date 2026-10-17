"""
Setup portable Node.js for Windows if node is not found on PATH.
Downloads Node LTS zip and extracts into tools/nodejs.
"""
import os
import sys
import shutil
import zipfile
import urllib.request
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent.parent / "tools"
NODE_DIR = TOOLS_DIR / "nodejs"
NODE_ZIP_URL = "https://nodejs.org/dist/v20.18.0/node-v20.18.0-win-x64.zip"

def setup_node():
    if shutil.which("node") and shutil.which("npm"):
        print("Node.js and npm already available on PATH.")
        return

    node_exe = NODE_DIR / "node.exe"
    if node_exe.exists():
        print(f"Node.js already exists in {NODE_DIR}")
        return

    TOOLS_DIR.mkdir(parents=True, exist_ok=True)
    zip_path = TOOLS_DIR / "node.zip"

    print(f"Downloading Node.js from {NODE_ZIP_URL}...")
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(NODE_ZIP_URL, zip_path)
    print("Download complete. Extracting...")

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(TOOLS_DIR)
    
    extracted_folder = TOOLS_DIR / "node-v20.18.0-win-x64"
    if extracted_folder.exists():
        if NODE_DIR.exists():
            shutil.rmtree(NODE_DIR)
        extracted_folder.rename(NODE_DIR)
    
    zip_path.unlink(missing_ok=True)
    print(f"Node.js installed successfully to {NODE_DIR}")

if __name__ == "__main__":
    setup_node()
