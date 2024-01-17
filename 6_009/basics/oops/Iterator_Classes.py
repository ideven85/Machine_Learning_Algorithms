class Is_Subsequence:
    def __init__(self,word1:str,word2:str):
        self.word1 = word1
        self.word2 = word2
        self.n = len(self.word1)

    def __bool__(self):
        j = 0
        for i in range(len(self.word2)):
            if self.word2[i] == self.word1[j]:
                j+=1
        print(j)
        return j==len(self.word2)
    def __getitem__(self,index:int):
        """
        :param index: given index of word2 in word1
        """

        for i in range(self.n):
            if self.word1[i]==self.word2[index]:
                index=i
                break
        return self.word1[index]

if __name__ == '__main__':
    word1 = "ace"
    word2 = "bacdef"
    sub1 = Is_Subsequence(word1,word2)
    print(bool(sub1))