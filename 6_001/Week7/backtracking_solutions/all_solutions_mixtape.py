from functools import lru_cache


def mixtape(songs: dict, target_duration: int):
    """
    Given a dictionary of songs (mapping titles to durations), as well as a
    total target duration, return a set of song titles such that the sum of
    those songs' durations equals the target_duration.

    If no such set exists, return None instead.

    """

    # @lru_cache(maxsize=None)
    def mixtape_helper(current, duration, start, n, visited):

        if duration == 0:
            # print(current)
            output.append(current[:])

        for i in range(start, n):

            first_song = list(songs.keys())[i]

            current_duration = songs[first_song]

            # if duration<0:
            #     mixtape_helper(current,target_duration,i+1,n)
            current.append(first_song)
            visited[0] += 1
            mixtape_helper(current, duration - current_duration, i + 1, n, visited)
            current.remove(first_song)

    visited = [0]
    number_of_songs = len(songs)
    output = list()
    current1 = list()

    mixtape_helper(current1, target_duration, 0, number_of_songs, visited)
    print(visited)
    return output


if __name__ == "__main__":
    song = {"A": 5, "B": 10, "C": 6, "D": 1}
    print(mixtape(song, 1000))
