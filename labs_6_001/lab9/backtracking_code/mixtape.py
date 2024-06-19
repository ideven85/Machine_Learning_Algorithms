from debug_recursion import show_recursive_structure


@show_recursive_structure
def mixtape(songs, target_duration):
    """
    Given a dictionary of songs (mapping titles to durations), as well as a
    total target duration, return a set of song titles such that the sum of
    those songs' durations equals the target_duration.

    If no such set exists, return None instead.

    >>> songs = {'A': 5, 'B': 10, 'C': 6, 'D': 2}
    >>> mixtape(songs, 21) == {'A', 'B', 'C'}
    True
    >>> mixtape(songs, 1000) is None
    True
    >>> mixtape(songs, 10)
    {'B'}
    """
    #raise NotImplementedError
    if target_duration == 0:
        return set()
    if not songs:
        return None
    for song,duration in songs.items():
        backtrack=mixtape({k:v for k,v in songs.items() if k!=song},target_duration-duration)
        if backtrack is not None:
            return {song}|backtrack
    return None


if __name__ == '__main__':
    import doctest
    doctest.testmod()
