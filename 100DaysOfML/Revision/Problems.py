from array import array
from collections import defaultdict
import heapq
from typing import List


class Solution:
    def frequencySort(self, s: str) -> str:
        if len(s)==0:
            return ""
        mapping = defaultdict(int)
        for e in s:
            mapping[e] += 1
        mapping = sorted(mapping.items(), key=lambda x: x[1],reverse=True)
        output = str()
        for key, value in mapping:
            output += key*value
        return output


    """


class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> hm = new HashMap<>();
        
        for (char c : s.toCharArray()) {
            hm.put(c, hm.getOrDefault(c, 0) + 1);
        }
        
        PriorityQueue<Map.Entry<Character, Integer>> pq = new PriorityQueue<>(
            (a, b) -> b.getValue() - a.getValue()
        );
        
        pq.addAll(hm.entrySet());
        
        StringBuilder result = new StringBuilder();
        while (!pq.isEmpty()) {
            Map.Entry<Character, Integer> entry = pq.poll();
            result.append(String.valueOf(entry.getKey()).repeat(entry.getValue()));
        }
        
        return result.toString();
    }
}


    """
    def frequencySortMemoised(self, s: str) -> str:
        #Map<Character,Integer> map = new HashMap<>();

        freq = defaultdict(int)

        for i in s:
            freq[i] += 1

        h = []
        # Queue<Integer> queue = new PriorityQueue<Integer>((a,b)->b-a);
        # for(var m:map.entrySet()){
        # queue.push(m.get}
        for i in freq:
            heapq.heappush(h, [-freq[i], i])
        ret = ""
        print(h)
        while h:
            f, ch = heapq.heappop(h)
            f = -f
            ret += ch * f
        return ret

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = str()
        s2 = str()
        for word in word1:
            s1 = s1 + word
        for word in word2:
            s2 = s2 + word
        return s1 == s2

    def countCharacters(self, words: List[str], chars: str) -> int:
        def frequency(s: str)->List[int]:
            dictionary = [0]*26
            for char in s:
                dictionary[ord(char)-97]+=1
            return dictionary

        def checkInside(a: List[int], b:List[int]) -> bool:
            for i in range(26):
                if a[i]>b[i]:
                    return False
            return True

        freq = frequency(chars)
        n = 0
        for word in words:
            if checkInside(frequency(word),freq):
                n+=len(word)


        return n



    def countCharactersLeetCode(self, words: List[str], chars: str) -> int:
        result = []
        for i in words:
            for j in i:
                if chars.count(j) < i.count(j):
                    break
            else:
                result.append(len(i))
        return sum(result)


a = Solution()
print(a.frequencySort("tree"))
print(a.frequencySortMemoised("i love java"))
word1 = ["a", "bc"]
word2 = ["ab", "c"]
print(a.arrayStringsAreEqual(word1, word2))
words = ["cat","bt","hat","tree"]
chars = "atach"
print(a.countCharacters(words, chars))
# print(sorted(list("cat")))
# print(sorted(list(chars)))
# print(sorted(['c','a','t']) in sorted(list(chars)))
words1 = ["hello","world","leetcode"]
char1 = "welldonehoneyr"
print(a.countCharacters(words1, char1))
