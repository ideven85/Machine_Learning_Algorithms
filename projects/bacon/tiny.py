import pickle

with open("resources/tiny.pickle", "rb") as f:
    data = pickle.load(f)
with open("tiny.txt", "w") as f:
    for line in data:
        f.write(str(line) + "\n")
