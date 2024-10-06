# def mixtape(songs, target_duration):
#     """
#     Given a dictionary of songs (mapping titles to durations), as well as a
#     total target duration, return a set of song titles such that the sum of
#     those songs' durations equals the target_duration.
#
#     If no such set exists, return None instead.
#
#     """
#     # Recursive Approach
#
#     if target_duration == 0:
#         return set()
#     if target_duration < 0 or not songs:
#         return None
#
#     song = list(songs.keys())[0]
#     duration = songs[song]
#     # print(song,duration)
#     songs_rest = {key: value for key, value in songs.items() if key != song}
#     # print(songs_rest)
#     case1 = mixtape(songs_rest, target_duration - duration)
#     case2 = mixtape(songs_rest, target_duration)
#     # print(case1)
#     if case1 is not None:
#         # print("Hi")
#         # print([song]+case1)
#         case1.add(song)
#         return case1
#
#     if case2 is not None:
#         # print("Hello")
#         # print(case2)
#         return case2
#
#     # for song, duration in songs.items():
#     #     rest = {key: value for (key, value) in songs.items() if key != song}
#     #     recursive_sequence_first = mixtape(rest, target_duration - duration)
#     #     if recursive_sequence_first:
#     #         return {song} | recursive_sequence_first
#     #     recursive_sequence_second = mixtape(
#     #         rest, target_duration
#     #     )  # If the current song is not included
#     #     if recursive_sequence_second:
#     #         return {song}
#     else:
#         return None
def mixtape(songs, target_duration):

    agenda = {()}
    total_paths = set()
    visited = set()
    count = 0
    while agenda:

        this_path = agenda.pop()

        # this_path=tuple(sorted(this_path))

        count += 1

        # print(type(this_path))

        duration = sum(songs[s] for s in this_path)
        if duration == target_duration:
            return this_path
        if duration > target_duration:
            continue
        for song, duration in songs.items():
            if song not in this_path:
                new_path = tuple(sorted(this_path + (song,)))
                if new_path in visited:
                    continue
                visited.add(new_path)
                agenda.add(new_path)
    print(count)
    # print(visited)
    return None


if __name__ == "__main__":
    # import doctest
    # print(doctest.testmod())
    songs = {"A": 5, "B": 10, "C": 6, "D": 1}
    print(mixtape(songs, 11))
    songs2 = {
        "California Dreamin'": 303,
        "Achy Breaky Heart": 481,
        "Set Fire to the Rain": 513,
        "Heat Wave": 60,
        "Fame": 325,
        "(Sittin' On) The Dock of the Bay": 380,
        "Cheap Thrills": 932,
        "American Pie": 370,
        "I Miss You": 454,
        "Someday": 864,
        "Lean on Me": 527,
        "San Francisco": 617,
        "Heart of Gold": 371,
        "Thank You": 221,
        "Bug A Boo": 19,
        "Heaven is a Place on Earth": 201,
        "Firework": 138,
        "Never Gonna Give You Up": 452,
        "I Want it That Way": 799,
        "...Baby One More Time": 686,
        "Call Me Maybe": 101,
        "Parallel Universe": 397,
        "Mmm Mmm Mmm Mmm": 740,
        "Dance to the Music": 426,
        "Eye of the Tiger": 433,
        "Happy Together": 115,
        "Der Kommissar": 880,
        "I Believe I Can Fly": 82,
        "Fancy": 117,
        "Different Summers": 555,
        "The Ballroom Blitz": 917,
        "Since U Been Gone": 794,
        "Complicated": 413,
        "No Scrubs": 400,
        "Total Eclipse of the Heart": 668,
        "Roar": 230,
        "We're an American Band": 783,
        "Sk8r Boi": 69,
        "It's All Right": 742,
        "Beautiful": 418,
        "Hang on Sloopy": 156,
        "Mr. Roboto": 523,
        "Watch Me (Whip, Nae Nae)": 865,
        "Magic": 463,
        "Build Me Up Buttercup": 485,
    }
    duration2 = 5105
    print(mixtape(songs2, duration2))
