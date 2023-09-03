def groupAnagrams( strs):
    d = {}  # maps s to list of words with signature s
    for word in strs:  # group words according to the signature
        s = ''.join(sorted(word))  # calculate the signature
        if s in d:
            d[s].append(word)  # append a word to an existing signature
        else:
            d[s] = [word]  # add a new signature and its first word
    # -- extract anagrams, ingoring anagram groups of size 1
    #print(d)
    return [d[s] for s in d if len(d[s]) >= 1]

if __name__ == '__main__':
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    print(groupAnagrams(words))