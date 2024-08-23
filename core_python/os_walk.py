import os

lst = []
for dirName, x, fileNames in os.walk(".."):
    # print(x,fileNames)
    for filename in fileNames:
        if filename.split(".")[-1] == "pyc":
            print(filename)

        lst.append(str(os.path.join(dirName, filename)))

print(len(lst))
