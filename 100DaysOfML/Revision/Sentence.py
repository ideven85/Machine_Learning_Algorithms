import re
import reprlib

"""
Shows a Sentence class that extracts words from a text by index.
"""
RE_WORD = re.compile(r'\w+')
class Sentence:
    def __init__(self,text):
        self.text =text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence {}'.format(reprlib.repr(self.text))

s= Sentence("Hi My name is Deven () {} %s, 234")
for word in s:
    print(word)
print(list(s))
print(len(s))
