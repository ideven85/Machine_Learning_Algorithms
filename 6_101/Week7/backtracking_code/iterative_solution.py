def mixtape(songs, target, s=frozenset()):
    sum_so_far = sum(songs[x] for x in s)
    if sum_so_far == target:
        return set(s)

    if sum_so_far > target:
        print(s)
        return None

    for song, duration in songs.items():
        if song in s:
            continue
        backtrack = mixtape(songs, target, s | {song})
        if backtrack is not None:
            return backtrack

        return None


songs = {"A": 5, "B": 10, "C": 6, "D": 2}
print(mixtape(songs, 17))
