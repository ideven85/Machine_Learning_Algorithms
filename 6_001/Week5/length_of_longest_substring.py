def length_of_longest_substring(s):
    """
    @param s: str String s
    @returns: int Length of longest substring of s without repeating characters
    """

    # Hashing Approach
    # Think Recursive... Too basic same thing as a for loop
    def longest_substring_helper(l, index, longest_so_far, visited, max_longest):
        if index >= len(l):
            # visited.add(l[index])
            longest_so_far = len(visited)
            return max(longest_so_far, max_longest)
        if l[index] not in visited:
            visited.add(l[index])
            return longest_substring_helper(
                l, index + 1, longest_so_far, visited, max_longest
            )
        else:
            longest_so_far = len(visited)
            max_longest = max(longest_so_far, max_longest)
            longest_so_far = 1
            visited.add(l[index])
            return longest_substring_helper(
                l, index + 1, longest_so_far, visited, max_longest
            )

    if not s:
        return 0
    mapping = dict()
    visited = set()

    current_longest = 0
    max_longest = 0
    left = 0

    for char in s:
        if char not in visited:
            visited.add(char)
        else:
            # print(visited)
            current_longest = len(visited)
            max_longest = max(current_longest, max_longest)

            visited.clear()
            visited.add(char)
    current_longest = len(visited)
    # print(visited)
    max_longest = max(current_longest, max_longest)
    print(longest_substring_helper(s, 0, 0, set(), 0))
    return max_longest


s = "abcdeabcabcdefgh"
print(length_of_longest_substring(s))
