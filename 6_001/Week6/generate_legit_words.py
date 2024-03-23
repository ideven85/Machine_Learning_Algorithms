import time


with open('all_words.txt','r') as f:
    ALL_WORDS={i.strip() for i in f}
#print(all_words[:20])
print('sex' in ALL_WORDS)
def generate_subsequences_slow(word):
    return {w for w in generate_subsequences_slow_helper(word) if w in ALL_WORDS}
def generate_subsequences_fast(word):
    for w in generate_subsequences_fast_helper(word) :
        if w in ALL_WORDS :
            print(w,end=' ')
    #return {w for w in generate_subsequences_fast_helper(word) if w in ALL_WORDS}

def generate_subsequences_fast_helper(word):
    if not word:
        yield ''
        return

    first=word[0]
    rest=word[1:]

    for w in generate_subsequences_fast_helper(rest):
        yield w
        for index in range(len(w)+1):
            yield w[:index]+first+w[index:]

def generate_subsequences_slow_helper(word):
    if not word:
        return {''}
    first=word[0]
    rest=word[1:]
    out = set()
    for w in generate_subsequences_slow_helper(rest):
        out.add(w)
        for index in range(len(w)+1):
            out.add(w[:index]+first+w[index:])
    return out

start = time.time()
print(generate_subsequences_slow('artichokes'))
end = time.time()
print(end - start)

"""
Using Generators
"""
start = time.time()

generate_subsequences_fast('artichokes')
print()
end = time.time()
print(end - start)