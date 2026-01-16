import os


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


# def ends_with_suffix(suffix):
#     return lambda x: x.endswith(suffix)


def list_files(path, ends_with_suffix=None):

    if not path:
        # yield []
        return

    if not os.path.exists(path):
        # yield []
        return

    elif os.path.isdir(path):
        for f in os.listdir(path):
            children = os.path.join(path, f)
            if os.path.isdir(children):
                yield from list_files(children, ends_with_suffix)
            elif not ends_with_suffix:
                yield children
            elif children.split(".")[-1].find(ends_with_suffix):
                yield children
    elif not ends_with_suffix:
        yield path
    elif path.split(".")[-1].find(ends_with_suffix):
        yield path


def ls(params: dict, folder):
    path = os.path.join(folder, params.get("path", "../.."))
    return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]


def main():
    location = os.path.realpath(os.path.dirname(__file__))
    folder = os.path.expanduser("~/Developer/")

    # words = list_files(folder)
    # for val in words:
    #     print(val)

    l = disk_usage2(folder)
    print(f"\nTotal disk usage of {folder} : {l/1024/1024/1024}GB")
    # for val in list_files(folder):
    #     print(val)

    # print(disk_usage2(folder))

    # params = {"paths": folder}
    # print(ls(params, folder))
    # count = 0
    # for f in list_files(folder, "ipynb"):
    #     count += 1
    #     print(f)
    # print(count)


if __name__ == "__main__":
    main()
