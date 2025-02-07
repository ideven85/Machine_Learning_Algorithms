import pickle
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int

#@dataclass
class Student(Person): # Not a data class unless decorated with it
    grade: int



def save_model():
    dave = Person("Deven",12)
    ser = pickle.dumps(dave)
    file = 'dave.pkl'
    with open(file,'wb') as f:
        f.write(ser)
    return file



def load_model(file):
    with open(file,'rb') as f:
        model = f.read()
    dave = pickle.loads(model)
    print(dave.name) # Side Effect not pure functional programming
    print(dave.age)

def main():
    #file=save_model()
    #load_model(file)
    stu = Student('Deven',12)
    print(stu)


if __name__ == '__main__':
    main()