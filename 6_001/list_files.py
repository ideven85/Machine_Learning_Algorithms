import os

LOCATION = os.path.realpath(os.path.dirname(__file__))


def disk_usage(path):
    total = os.path.getsize(path)
    # print(total)
    if os.path.isdir(path):
        for file in os.listdir(path):
            files = os.path.join(path, file)
            total += disk_usage(files)
    print("{0:< 7}".format(total), path)
    return total


def disk_usage2(path):
    if not os.access(path, 700):
        return 0

    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):

            childpath = os.path.join(path, filename)
            if not childpath:
                continue
            total += disk_usage2(childpath)
    print("{0:<7}".format(total), path)
    return total


folder = os.path.expanduser("~/Developer")


def ends_with_suffix(suffix):
    return lambda x: x.endswith(suffix)


def list_files(path):
    files = []
    if not path:
        return
    if not os.access(path, 700):
        return
    if os.path.isfile(path):
        # files.append(path)
        yield path
    elif os.path.isdir(path):
        for f in os.listdir(path):
            children = os.path.join(path, f)
            if os.path.isdir(children):
                yield from list_files(children)
            else:
                yield children


# words=[list_files(y) for y in folder ]
# print(words)


# print(disk_usage2(folder))
for val in list_files(folder):
    print(val)
