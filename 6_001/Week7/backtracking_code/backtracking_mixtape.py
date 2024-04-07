def mixtape(songs, target_duration):
    #count=0
    if target_duration==0:
        return set()
    if not songs :
        return None
    for song,duration in songs.items():
        #count+=1
        remaining={k:v for k,v in songs.items() if k!=song}
        rest_songs1 = mixtape(remaining,target_duration-duration)
        if rest_songs1 is not None:
            # print("C1",count+1)
            return {song}|rest_songs1
        rest_songs2 = mixtape(remaining,target_duration)
        if rest_songs2 is not None:
            # print("C2", count + 1)
            return rest_songs2

        return None
#
# if __name__ == '__main__':
#     songs = {'A': 5, 'B': 10, 'C': 6, 'D': 1}
#     print(mixtape(songs, 11))
