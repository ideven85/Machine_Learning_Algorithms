from typing import List


def commonCharacters(strings: List[str]) -> List[str]:
    # Write your code here.
    if len(strings) == 0:
        return []
    output = []
    mapping = set()
    for i in range(len(strings[0])):
        mapping.add(strings[0][i])
    print(mapping)
    for j in range(1, len(strings)):
        for i in range(len(strings[j])):
            c = strings[j][i]

        print(mapping)

    return list(mapping)


def commonCharactersV2(strings):
    # Write your code here.
    mapping = {}
    for string in strings:
        setString = set(string)
        for char in setString:
            if char not in mapping:
                mapping[char] = 0
            mapping[char] += 1
    output = []
    print(mapping)
    for character, count in mapping.items():
        if count == len(strings):
            output.append(character)
    return output


if __name__ == "__main__":
    s = ["abc", "bcd", "cbad"]
    print(commonCharactersV2(s))
