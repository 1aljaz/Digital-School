import os

def list_files(path="/Users/aljazmarn/Documents/github/Digital-School/10-11-2025/hell_maze"):
    for root, dir, files in os.walk(path):
        for file in files:
            if "target_REAL" in os.path.join(root, file):
                print(os.path.join(root, file)) 


list_files()