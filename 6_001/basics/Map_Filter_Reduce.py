class Person:
    def __init__(self,name:str,age:int,gender:str) -> None:
        self.name=name
        self.age = age
        self.gender=gender


    def __str__(self) -> str:
        return f'{self.name} who is a {self.gender} is {self.age} years old'

#persons =[Person("John",21,'Male'),Person('Deven',21,'Male')]
# for person in persons:
#     print(person)
names = ['John','Deven','Joe']
ages = [21,22,23]
genders = ['Male','Female','Unknown']
persons = [Person for _ in range(len(names))]

"""
Working Code
"""
for i in range(len(names)):
    persons[i]=persons[i](names[i],ages[i],genders[i])


for p in persons:
    print(p)

"""
Dictionary Revision
"""

person_dict ={'name':'John','age':21,'gender':'Male'}
for key,value in person_dict.items():
    print(key,value)

persons = [
    ('John',(21,'Male')),
    ('Deven',(22,'Male')),
    ('Pooja',(23,'Female')),

]
pairs = zip(*persons)
print("Pairs: ",*pairs)
persons_dictionary = {name:(age,sex) for name,(age,sex) in persons}
print(persons_dictionary)

Dict = dict({1:'Geeks',2:'Idiot auto complete',3: 'New method to create dictionary',4:'New method to create dictionary'})
print(Dict)
a = [1,2,3,4,5,6,7,8,9]
x = [element for element in a if element%2==0]
print(x)


def dump(**kwargs):
    return kwargs

print(dump(**persons_dictionary))