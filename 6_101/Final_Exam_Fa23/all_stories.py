def all_n_length_stories(n,vocabulary):


    for word in vocabulary:
        if len(word)==n:
            yield word



def round(number,n_digits=0):
    pass



def main():
    vocabulary = 'I am Hamlet the prin of Denmark'.split()
    goal = 'the prince am I'.split()
    print(vocabulary)
    print(len(goal))
    print([s for s in all_n_length_stories(len(goal),vocabulary)])

if __name__ == '__main__':
    main()
