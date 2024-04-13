#todo Date: 14th April,2024
def feed(preferences:dict, quantities:dict)->dict:
    """
    >>> out1 = {'alex': 'pickles', 'billie': 'ketchup'}
    >>> feed({'alex': ['pickles'], 'billie': ['ketchup']},
    ...      {'pickles': 1, 'ketchup': 1}) == out1
    True

    >>> feed({'alex': ['pickles'], 'billie': ['pickles']},
    ...      {'pickles': 1, 'ketchup': 1}) is  None
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

