




if __name__ == '__main__':
    N = int(input())
    while N>0:
        scores = list(map(int, input().strip().split()))
        #scores = [3,2,5,6,1,1]
        alice = sorted(scores[:3],reverse=True)
        #print(a)
        #print(scores[:3])
        #print(scores[3:])
        #a.sort(reverse=True)
        #alice=a
        #print(alice)
        ALICE = sum(alice[:2])
        bob = sorted(scores[3:],reverse=True)
        BOB = sum(bob[:2])
        if ALICE>BOB:
            print("Alice")
        elif ALICE<BOB:
            print("Bob")
        else:
            print("Tie")
        N-=1
