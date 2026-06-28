import os
import hashlib
import time

# Folder to monitor (change if needed)
FOLDER = "."

# Store hashes in memory
file_hashes = {}

# Function to calculate file hash
def get_hash(filepath):
    try:
        with open(filepath, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except:
        return None

# Initial scan
def scan_files():
    hashes = {}
    for file in os.listdir(FOLDER):
        if os.path.isfile(file):
            hashes[file] = get_hash(file)
    return hashes

print("🔍 Starting File Integrity Monitor...")
file_hashes = scan_files()

# Continuous monitoring
while True:
    time.sleep(5)  # check every 5 seconds
    new_hashes = scan_files()

    # Check modified & deleted files
    for file in file_hashes:
        if file not in new_hashes:
            print(f"❌ Deleted: {file}")
        elif file_hashes[file] != new_hashes[file]:
            print(f"⚠️ Modified: {file}")

    # Check new files
    for file in new_hashes:
        if file not in file_hashes:
            print(f"🆕 New File: {file}")

    file_hashes = new_hashes