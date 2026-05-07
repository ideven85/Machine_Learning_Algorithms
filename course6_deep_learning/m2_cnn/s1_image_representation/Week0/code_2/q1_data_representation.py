"""
Question 1:
There are many ways to represent sounds in Python.
Look at the different ways presented below and answer the following questions.
a)	How readable is each sound representation?
b)	How extensible is each representation?
(How hard would it to be to change it by adding more information / channels?)
c)	What are common mistakes someone might make trying to use the representation?

"""

# sound is a dictionary, with keys
#    rate: int, the sampling rate, in samples per second
#    samples: a list of floats, the samples
sound = {"rate": 8000, "samples": [1, 2, 3]}
sound["rate"]
sound["samples"]

# OR:
# sound is a list whose first element is the rate and second is a sublist
# containing the samples
sound = [8000, [1, 2, 3]]
sound[0]
sound[1]

# OR:
# sound is a list whose first element is the rate, and remaining elements the
# samples
sound = [8000, 1, 2, 3]
sound[0]
sound[1:]


# OR: (coming later in semester)
# class Sound:
#    ...
# sound = Sound(8000, [1,2,3])
# sound.rate
# sound.samples
# isinstance(sound, Sound) ==> True
