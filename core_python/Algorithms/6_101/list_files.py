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


folder = os.path.expanduser("~/Developer/")


def ends_with_suffix(suffix):
    return lambda x: x.endswith(suffix)


def list_files(path, ends_with_suffix):

    if not path:
        yield []
        return
    if not os.access(path, 700):
        yield []
        return

    elif os.path.isdir(path):
        for f in os.listdir(path):
            children = os.path.join(path, f)
            if os.path.isdir(children):
                yield from list_files(children, ends_with_suffix)
            elif children.split(".")[-1] == ends_with_suffix:
                yield children

    elif path.split(".")[-1] == ends_with_suffix:
        yield path


# words = list_files(folder)
# for val in words:
#     print(val)

# print(disk_usage2(folder))
# for val in list_files(folder):
#     print(val)

# print(disk_usage2(folder))


def ls(params: dict):
    path = os.path.join(folder, params.get("path", "."))
    return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]


params = {"paths": folder}
# print(ls(params))
count = 0
for f in list_files(folder, "java"):
    count += 1
    print(f)
print(count)
"https://www.youtube.com/watch?v=0xaLT4Svzgo&list=PLxC_ffO4q_rW0bqQB80_vcQB09HOA3ClV&index=1&t=1498s"
