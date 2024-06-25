def mixtape(songs, target_duration):
    agenda = [set()]
    while agenda:
        this_path = agenda.pop()
        duration = sum(songs[s] for s in this_path)
        if duration == target_duration:
            return this_path
        if duration > target_duration:
            continue
        for song, duration in songs.items():
            if song not in this_path:
                agenda.append(this_path | {song})
    return None
