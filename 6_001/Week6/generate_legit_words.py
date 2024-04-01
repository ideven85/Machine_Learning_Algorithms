import time
from multiprocessing.pool import ThreadPool
from threading import Thread

with open("all_words.txt", "r") as f:
    ALL_WORDS = {i.strip() for i in f}
# print(all_words[:20])
#print("" in ALL_WORDS)


def generate_subsequences_slow(word):
    return {w for w in generate_subsequences_slow_helper(word) if w in ALL_WORDS}


def generate_subsequences_fast(word):
    return [w for w in generate_subsequences_fast_helper(word)]
    # return {w for w in generate_subsequences_fast_helper(word) if w in ALL_WORDS}


def generate_subsequences_fast_helper(word):
    if not word:
        yield ""
        return

    first = word[0]
    rest = word[1:]

    for w in generate_subsequences_fast_helper(rest):
        yield w
        for index in range(len(w) + 1):
            yield w[:index] + first + w[index:]


def generate_subsequences_slow_helper(word):
    if not word:
        return {""}
    first = word[0]
    rest = word[1:]
    out = set()
    for w in generate_subsequences_slow_helper(rest):
        out.add(w)
        for index in range(len(w) + 1):
            out.add(w[:index] + first + w[index:])
    return out



if __name__ == '__main__':
    words = ['fib','fie','fig','fin','fir','fit','fix','artichokeshelperfigure','cheer']
    #[generate_subsequences_fast(w) for w in words]
    start = time.time_ns()
    with ThreadPool() as pool:
        for result in pool.map(generate_subsequences_fast,[w for w in words]):
            print(f'Got Result {result}')
    end = time.time_ns()
    print('\n\n\nDone', end - start)
    # threads = [Thread(target=generate_subsequences_fast,args=(x,)) for x in words]
    # start = time.time_ns()
    # for t in threads:
    #     t.start()
    # for t in threads:
    #     t.join()
    # end = time.time_ns()
    # print('\nDone',end-start)

    #
    # start = time.time()
    # print(generate_subsequences_slow("artichokes"))
    # end = time.time()
    # print(end - start)
    #
    # """
    # Using Generators
    # """
    # start = time.time()
    #
    # print(generate_subsequences_fast("artichokes"))
    # print()
    # end = time.time()
    # print(end - start)
