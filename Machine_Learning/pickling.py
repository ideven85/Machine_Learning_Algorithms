import pickle
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int

def save_model():
    dave = Person("Deven",12)
    ser = pickle.dumps(dave)
    with open('dave.pkl','wb') as f:
        f.write(ser)
    return ser

def load_model(model):
    dave = pickle.loads(model)
    print(dave.name) # Side Effect not pure functional programming
    print(dave.age)

def main():
    model = save_model()
    load_model(model)


if __name__ == '__main__':
    main()