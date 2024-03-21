import pickle

db = './resources/movies.pickle'
names = pickle.load(open(db, 'rb'))
print(names)
#
# with open('acted_together1.txt', 'w') as file:
#     for key, value in names.items():
#         if value == '200015':
#             print(key)
#         file.write('"'+str(key) + '":' + str(value) + '\n')