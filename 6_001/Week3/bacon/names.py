import pickle

db = "./resources/small.pickle"
acted_together_large = pickle.load(open(db, "rb"))
# print(acted_together_tiny)
with open("acted_together_small.txt", "w") as file:
    for actor1, actor2, movie in acted_together_large:
        file.write(str(actor1) + " " + str(actor2) + " " + str(movie) + "\n")

#
# with open('acted_together1.txt', 'w') as file:
#     for key, value in names.items():
#         if value == '200015':
#             print(key)
#         file.write('"'+str(key) + '":' + str(value) + '\n')
