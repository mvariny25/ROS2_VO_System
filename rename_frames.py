import os
import re

# path to your image folder
print('Input folder name')
fn = str(input())
folder = f"datasets/{fn}/data"

for filename in os.listdir(folder):
    if filename.endswith(".png"):
        # extract the number between 'frame_' and '_diff'
        match = re.search(r'frame_(\d+)_diff', filename)
        if match:
            new_name = f"{match.group(1)}.png"
            old_path = os.path.join(folder, filename)
            new_path = os.path.join(folder, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")
