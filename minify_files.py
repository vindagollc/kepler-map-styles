import os
import json
from pathlib import Path

def minify_json_files(folder_path):
    """Discover all JSON files in a folder and minify their content."""
    json_files = Path(folder_path).glob("**/*.json")
    
    for json_file in json_files:
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            
            with open(json_file, 'w') as f:
                json.dump(data, f, separators=(',', ':'))
            
            print(f"Minified: {json_file}")
        except Exception as e:
            print(f"Error processing {json_file}: {e}")

if __name__ == "__main__":
    folder = input("Enter the folder path: ")
    minify_json_files(folder)