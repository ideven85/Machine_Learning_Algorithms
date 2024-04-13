def mixtape(songs, target_duration):
    """
    Given a dictionary of songs (mapping titles to durations), as well as a
    total target duration, return a set of song titles such that the sum of
    those songs' durations equals the target_duration.

    If no such set exists, return None instead.

    """
    # Recursive Approach

    if target_duration == 0:
        return set()
    if target_duration < 0 or not songs:
        return None

    song = list(songs.keys())[0]
    duration = songs[song]
    # print(song,duration)
    songs_rest = {key: value for key, value in songs.items() if key != song}
    # print(songs_rest)
    case1 = mixtape(songs_rest, target_duration - duration)
    case2 = mixtape(songs_rest, target_duration)
    # print(case1)
    if case1 is not None:
        # print("Hi")
        # print([song]+case1)
        case1.add(song)
        return case1

    if case2 is not None:
        # print("Hello")
        # print(case2)
        return case2

    # for song, duration in songs.items():
    #     rest = {key: value for (key, value) in songs.items() if key != song}
    #     recursive_sequence_first = mixtape(rest, target_duration - duration)
    #     if recursive_sequence_first:
    #         return {song} | recursive_sequence_first
    #     recursive_sequence_second = mixtape(
    #         rest, target_duration
    #     )  # If the current song is not included
    #     if recursive_sequence_second:
    #         return {song}
    else:
        return None


if __name__ == "__main__":
    # import doctest
    # print(doctest.testmod())
    songs = {"A": 5, "B": 10, "C": 6, "D": 1}
    print(mixtape(songs, 11))
