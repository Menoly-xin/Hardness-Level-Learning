import os
import shutil
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Delete a file')
    parser.add_argument('path', help='Path to the file')
    parser.add_argument('save_path', help='Path to the file')
    return parser.parse_args()
if __name__ == '__main__':
    args = parse_args()
    dirs = os.listdir(args.path)
    for dir in dirs:
        full_dir = os.path.join(args.path, dir)
        if not os.path.isdir(full_dir):
            continue
        save_full_path = os.path.join(args.save_path, dir)
        if not os.path.exists(save_full_path):
            os.makedirs(save_full_path)
        files = os.listdir(full_dir)
        for file in files:
            if file.endswith('.json') or file.endswith('.py') or file.endswith('.log'):
                shutil.copy(os.path.join(full_dir, file), save_full_path)



