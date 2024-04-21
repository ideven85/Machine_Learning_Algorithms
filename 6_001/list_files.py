import os

LOCATION = os.path.realpath(os.path.dirname(__file__))

def disk_usage(path):
    total=os.path.getsize(path)
    #print(total)
    if os.path.isdir(path):
        for file in os.listdir(path):
            files=os.path.join(path,file)
            total+=disk_usage(files)
    print('{0:< 7}'.format(total), path)
    return total


def disk_usage2(path):
    if not os.access(path,700):
        return 0


    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):

            childpath = os.path.join(path, filename)
            if not childpath:
                continue
            total += disk_usage2(childpath)
    print('{0:<7}'.format(total), path)
    return total
print(disk_usage2('../../'))
