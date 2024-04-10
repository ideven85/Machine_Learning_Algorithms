movies = ["Alien", "Barbie", "Clue", "Frozen", "Inception"]
ratings = [8.5, 7.3, 7.2, 7.4, 8.8, 3.3, 1.5]

def exampleA():
    print(i**2 for i in [0,1,2,3,4,5])

exampleA()
print(eval('1+1'))
def exampleB():
    i = 0
    for movie in movies:
        print(movie)
exampleB()

def exampleC():
   reverse=movies[::-1]
   for x in reverse:
       print(x)
exampleC()

def exampleD():
    for index,element in enumerate(movies):
        print(index, element)
exampleD()

def exampleE():
   for (x,y) in zip(movies,ratings):
       print(x,y)
exampleE()