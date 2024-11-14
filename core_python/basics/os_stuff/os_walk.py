import os
from list_files import list_files


def walk_os():
    lst = []
    for dirName, x, fileNames in os.walk("../../.."):
        # print(x,fileNames)
        for filename in fileNames:
            if filename.split(".")[-1] == "pyc":
                print(filename)

            lst.append(os.path.join(dirName, filename))
    return lst


def main():
    l = walk_os()
    print(len(l))
    for e in l[:20]:
        print(e)
    print(list(list_files(os.path.expanduser("~/Developer"), "py")))


if __name__ == "__main__":
    main()
