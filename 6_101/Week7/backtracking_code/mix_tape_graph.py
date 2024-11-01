import time


def mixtape(songs: dict, target_duration: int):

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
    songs = {"A": 5, "B": 10, "C": 6, "D": 1}
    s1 = time.process_time_ns()
    print(mixtape(songs, 11))
    s2 = time.process_time_ns()
    print(s2 - s1)
    # 4^2=16 )
