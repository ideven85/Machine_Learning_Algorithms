def duplicate_characters(string):
    duplicates = []
    visited = set()
    for char in string:
        if char in visited:
            duplicates.append(char)
        else:
            visited.add(char)
    return " ".join(duplicates)


string = "DavidaD"
print(duplicate_characters(string))
