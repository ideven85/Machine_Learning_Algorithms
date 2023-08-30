import os


def get_usage(given_path):
    total = 0
    if not given_path:
        total = 0
        return FileNotFoundError("File not Found")

    else:
        total = os.path.getsize(given_path)


    if os.path.isdir(given_path):
        for file in os.listdir(given_path):
            children = os.path.join(given_path,file)
            if not children:
                total += 0
                return FileNotFoundError("File not Found")

            else:
                total += get_usage(children)


    print(total,given_path)
    return total

print(get_usage("/Users/deven/Developer"))