from text_tokenize import tokenize_sentences

with open("texts/pride_and_prejudice", "r") as f:
    pride = f.read()

tokenised = tokenize_sentences(pride)
for line in tokenised:
    print(line)
