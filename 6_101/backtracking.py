# 6.101 recitation: potluck

# You are organizing a potluck for your friends, and you want to make sure that
# everybody who comes to your party has something that they can eat!
#
# Given a dictionary containing food preferences (mapping person => list of
# foods they will eat), and a dictionary containing the food you have available
# (mapping food name => quantity), we want to give everybody one food in their
# preferences, but we can't give out more of a particular food than we have
# available at the start.
#
# When a solution is found, return a dictionary mapping each person to the food
# they are eating. If there is no solution, return None.


def feed(preferences, quantities):
    """
    >>> out1 = {'alex': 'pickles', 'billie': 'ketchup'}
    >>> feed({'alex': ['ketchup', 'pickles'], 'billie': ['ketchup']},
    ...      {'pickles': 1, 'ketchup': 1}) == out1
    True

    >>> feed({'alex': ['pickles'], 'billie': ['pickles']},
    ...      {'pickles': 1, 'ketchup': 1}) == None
    True

    >>> out2 = {'alex': 'pickles', 'billie': 'pickles'}
    >>> feed({'alex': ['pickles'], 'billie': ['pickles']},
    ...      {'pickles': 2, 'ketchup': 1}) == out2
    True

    >>> preferences = {'alex': ['pickles', 'ketchup'], 'billie': ['chips', 'onions'],
    ...           'cameron': ['pie', 'broccoli'],  'devin': ['pickles'],
    ...           'emery': ['onions'], 'frankie': ['pie']}
    >>> foods = {'pickles': 1, 'ketchup': 1, 'chips': 1, 'onions': 1,
    ...          'pie': 1, 'broccoli': 1}
    >>> expected = {'alex': 'ketchup', 'billie': 'chips', 'cameron': 'broccoli',
    ...             'devin': 'pickles', 'emery': 'onions', 'frankie': 'pie'}
    >>> feed(preferences, foods) == expected
    True

    >>> preferences = {'alex': ['cake', 'cheese', 'pie', 'sandwiches'],
    ...           'billie': ['cake', 'cheese', 'pie'],
    ...           'cameron': ['cake', 'cheese'],
    ...           'devin': ['cake', 'cheese'],
    ...           'emery': ['cake', 'cheese']}
    >>> foods = {'cake': 2, 'cheese': 1, 'pie': 1, 'sandwiches': 1}
    >>> res = feed(preferences, foods)
    >>> res['alex'], res['billie']
    ('sandwiches', 'pie')
    >>> sorted((res['cameron'], res['devin'], res['emery']))
    ['cake', 'cake', 'cheese']
    """
    pass


import doctest

if __name__ == "__main__":
    doctest.testmod()
