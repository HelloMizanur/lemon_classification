import os
from pathlib import Path

# 1. Define the base path relative to this script
base_dir = Path(__file__).parent / "data"

# 2. Define the sub-directories
train_dir = base_dir / "train"
val_dir = base_dir / "validation"

def check_folders(directory, set_name):
    print(f"--- Checking {set_name} Set ---")
    categories = ['fresh', 'affected']
    
    for cat in categories:
        path = directory / cat
        if path.exists():
            # Count the number of images in the folder
            file_count = len([f for f in os.listdir(path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
            print(f"Found {file_count} images in: {set_name}/{cat}")
        else:
            print(f"Warning: Path {path} does not exist!")
    print("\n")

if __name__ == "__main__":
    # Check if the 'data' folder exists
    if base_dir.exists():
        check_folders(train_dir, "Train")
        check_folders(val_dir, "Validation")
    else:
        print("Error: The 'data' folder was not found in the script directory.")

  
