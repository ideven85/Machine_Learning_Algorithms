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
    """
    if target_duration==0:
        return set()
    first = list(songs.keys())[0]
    duration = songs[first]
    return {first}|mixtape({key:value for key,value in songs.items() if key!=first}, target_duration-duration)




if __name__ == '__main__':
    import doctest
    doctest.testmod()
    songs = {'A': 5, 'B': 10, 'C': 6, 'D': 2}
    print(mixtape(songs,21))
