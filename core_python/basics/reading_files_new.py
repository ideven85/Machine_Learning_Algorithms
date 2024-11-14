import os.path

import gymnasium.envs
from pathlib import Path

def read_file(file):


    if not os.path.exists(file):
        raise FileNotFoundError("File Not Found")
    f = Path(file)
    print(f)
    contents = f.read_text().split('\n')
    print(contents)




def main():
    f = 'envs.txt'
    read_file(f)

if __name__ == '__main__':
    main()

