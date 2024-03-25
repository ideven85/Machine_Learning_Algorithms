import pickle
from collections import defaultdict

bacon_numbers = defaultdict()

with open('resources/names.pickle','rb') as f:
    names = pickle.load(f)

for name,bacon_number in names.items():
    bacon_numbers[bacon_number] = name

with open('resources/small.pickle','rb') as f:
    acted_together_ids = pickle.load(f)

with open('resources/movies.pickle','rb') as f:
    movies = pickle.load(f)

movie_names = defaultdict()
for movie,bacon_number in movies.items():
    movie_names[bacon_number] =movie
acted_together_names = defaultdict(list)
file_name = 'acted_together_names.txt'
with open(file_name,'w') as f:
    for actor1,actor2,movie in acted_together_ids:
        f.write(str(bacon_numbers[actor1]) + ',' + str(bacon_numbers[actor2]) + ',' + str(movie_names[movie]) +'\n')
        acted_together_names[bacon_numbers[actor1]].append([bacon_numbers[actor2],movie_names[movie]])
        acted_together_names[bacon_numbers[actor2]].append([bacon_numbers[actor1], movie_names[movie]])
