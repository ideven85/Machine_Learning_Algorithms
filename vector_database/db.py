"""
Let’s represent the vector database using a 2D grid
 where one axis represents the color of the animal (brown, black, white)
 and the other axis represents the size (small, medium, large).
"""
import pandas as pd
from collections import namedtuple
animals_normal=namedtuple('Animals',('color','size'))
animals_normal1 = [{'color':['brown','black','white']},{'size': ['small','medium','large']}]
#animals = pd.DataFrame()

for animal in animals_normal1:
    print(animal)