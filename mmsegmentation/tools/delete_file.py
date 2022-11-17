import os
import shutil
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Delete a file')
    parser.add_argument('path', help='Path to the file')
    return parser.parse_args()
if __name__ == '__main__':
    args = parse_args()
    dirs = os.listdir(args.path)
    for dir in dirs:
        names = dir.split('_')
        if '40k' in names:
            filename = ['iter_'+str(iter)+'.pth' for iter in range(4000,32001,4000)]
        if '80k' in names:
            filename = ['iter_'+str(iter)+'.pth' for iter in range(8000,64001,8000)]
        if '160k' in names:
            filename = ['iter_'+str(iter)+'.pth' for iter in range(16000,128001,16000)]

        filenames = [os.path.join(args.path, dir, name) for name in filename]
        detete = []
        for item in filenames:
            if os.path.exists(item):
                detete.append(item)
        if len(detete) == 0:
            continue
        print(*detete,sep='\n')
        yes_or_no = input('Delete? [y/n] ')
        if yes_or_no == 'y':
            for file in detete:
                os.remove(file)
        else:
            print('Aborted')


