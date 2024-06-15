from lab9.debug_recursion import show_recursive_structure


@show_recursive_structure
def mixtape(songs, target_duration):
    """
    Given a dictionary of songs (mapping titles to durations), as well as a
    total target duration, return a set of song titles such that the sum of
    those songs' durations equals the target
    _
    duration.
    If no such set exists, return None instead.
    >>> songs = {'A': 5, 'B': 10, 'C': 6, 'D': 2}
    >>> mixtape(songs, 21) == {'A', 'B', 'C'}
    True
    >>> mixtape(songs, 1000) is None
    True
    >>> mixtape(songs, 10)
    {'B'}

    """

    if target_duration == 0:
        return set()
    if not songs:
        return None
    new_song = list(songs.keys())[0]
    songs_rest={key:value for key,value in songs.items() if key!=new_song}
    case1=mixtape(songs_rest,target_duration-songs[new_song])
    if case1 is not None:
        return {new_song}|case1
    case2 = mixtape(songs_rest,target_duration)
    if case2 is not None:
        return case2
    return None

