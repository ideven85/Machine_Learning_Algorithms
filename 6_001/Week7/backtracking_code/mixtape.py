def mixtape(songs, target_duration):
    """
    Given a dictionary of songs (mapping titles to durations), as well as a
    total target duration, return a set of song titles such that the sum of
    those songs' durations equals the target_duration.

    If no such set exists, return None instead.
    >>> mixtape(
    {
        "Chariots of Fire": 907,
        "Fire": 137,
        "3 AM": 362,
        "Blurry": 965,
        "Thank You": 874,
        "Always Straight Ahead": 290,
        "It's Still Rock and Roll To Me": 345,
        "Set Fire to the Rain": 371,
        "Footloose": 888,
        "Work": 3,
        "Love Song": 78,
        "Mambo No. 5": 859,
        "Swamp Thing": 131,
        "Der Kommissar": 471,
        "Walk Like an Egyptian": 822,
        "Lisztomania": 44,
        "Can You Feel the Love Tonight": 528,
        "Lady": 902,
        "We Can Work It Out": 903,
        "I Got You, Babe": 565,
        "Karma Chameleon": 4,
        "Blue (Da Ba Dee)": 886,
        "Heaven is a Place on Earth": 369,
        "Watch Me (Whip, Nae Nae)": 647,
        "Complicated": 155,
        "Changes": 229,
        "Kryptonite": 607,
        "Achy Breaky Heart": 437,
        "Raindrops Keep Fallin' on My Head": 825,
        "Nothing Compares 2 U": 405,
        "This Love": 878,
        "Toxic": 232,
        "Electric Youth": 143,
        "Magic": 338,
        "I Will Survive": 298,
        "Fallin'": 462,
        "Hey Jude": 586,
        "I Miss You": 609,
        "Last Train to Clarksville": 52,
        "Bennie and the Jets": 449,
        "Dancing Machine": 509,
        "What Do You Mean?": 466,
        "Money for Nothing": 572,
        "Hooked on a Feeling": 717,
        "Mmm Mmm Mmm Mmm": 441,
        "What's Love Got to Do With It": 413,
        "Waterloo": 386,
        "All Around the World (La La La La La)": 376,
        "Jack & Diane": 900,
        "Spider Snakes": 895,
        "San Francisco": 732,
        "Problem": 814,
        "Policy of Truth": 785,
        "Miss Independent": 48,
        "Mockingbird": 246,
        "The Locomotion": 171,
        "Every Rose Has Its Thorn": 66,
        "Never Gonna Give You Up": 273,
        "Hips Don't Lie": 334,
        "Whoomp! (There It Is)": 126,
        "Jump Around": 248,
        "Firework": 602,
        "Call Me": 726,
        "Sweet Caroline": 657,
        "Save Tonight": 252,
        "Broken Wings": 359,
        "It's the Same Old Song": 966,
        "Surfin' USA": 813,
        "I Want it That Way": 730,
        "Mony Mony": 123,
        "(I Wear My) Sunglasses at Night": 956,
        "Dancing Queen": 237,
        "September": 610,
        "Sugar": 312,
        "Always Be My Baby": 188,
        "Jeopardy": 18,
        "Safety Dance": 87,
        "Bring Me To Life": 962,
        "Particle Man": 934,
        "Umbrella": 214,
        "Jump": 33,
        "Can't Stop the Feeling": 889,
        "Paint It, Black": 516,
        "Boom Boom Pow": 11,
        "I Love Rock 'n Roll": 256,
        "One Step at a Time": 254,
        "Upside Down": 391,
        "Fergalicious": 91,
        "Cheap Thrills": 5,
        "Faith": 672,
        "The Twist": 721,
        "Celebration": 724,
        "The Way": 754,
        "Stay": 395,
        "I Want to Hold Your Hand": 320,
        "Sweet Child o' Mine": 349,
        "Funkytown": 69,
        "Beat It": 739,
        "The Great Divide": 890,
        "Barracuda": 319,
        "A Fifth of Beethoven": 709,
        "Reunited": 623,
        "Against All Odds (Take a Look At Me Now)": 731,
        "Royals": 740,
        "Cold as Ice": 410,
        "Fancy": 725,
        "(Sittin' On) The Dock of the Bay": 727,
        "Macarena": 110,
        "Sugar, Sugar": 84,
        "In My Head": 249,
        "At the End of August": 827,
        "Shake It Off": 242,
        "Slide": 409,
        "I Feel the Earth Move": 847,
        "I Try": 824,
        "Picture": 746,
        "Dance to the Music": 982,
        "Respect": 287,
        "Express Yourself": 894,
        "Waterfalls": 678,
        "Hero": 980,
        "Uptown Funk": 632,
        "Tell Her ABout It": 851,
        "Lights": 763,
        "That Don't Impress Me Much": 690,
        "Hit 'Em Up Style": 486,
        "U Can't Touch This": 803,
        "Parallel Universe": 294,
        "American Pie": 972,
        "Hide and Seek": 527,
        "The Hustle": 684,
        "I Knew You Were Trouble": 975,
        "The Wanderer": 796,
        "Boogie Oogie Oogie": 355,
        "You've Got a Friend": 797,
        "Hello": 81,
        "Life Is a Highway": 841,
        "Hang on Sloopy": 465,
        "Heart of Gold": 204,
        "Unwritten": 408,
        "My Heart Will Go On": 308,
        "She Blinded Me With Science": 392,
        "Glamorous": 830,
        "Let It Be": 216,
        "Nyan Cat": 680,
        "Crazy on You": 479,
        "Gettin' Jiggy Wit It": 552,
        "Dancing in the Street": 57,
        "The Distance": 770,
        "...Baby One More Time": 559,
        "Hollaback Girl": 454,
        "Take Me Home, Country Roads": 622,
        "Smooth": 642,
        "Love Story": 869,
        "The Ballroom Blitz": 532,
        "Behind These Hazel Eyes": 267,
        "Electric Avenue": 380,
        "Another Brick in the Wall": 370,
        "Fame": 301,
        "Lean on Me": 778,
        "Blank Space": 238,
        "Single Ladies (Put a Ring On It)": 530,
        "Sunshine of Your Love": 470,
        "Maps": 745,
        "Straight Up": 562,
        "No Scrubs": 519,
        "Hanging by a Moment": 845,
        "99 Luftballons": 800,
        "Mrs. Brown, You've Got a Lovely Daughter": 525,
        "Mrs. Robinson": 150,
        "Do Wah Diddy Diddy": 432,
        "Drops of Jupiter": 90,
        "London Bridge": 379,
        "Ghostbusters": 95,
        "Time in a Bottle": 716,
        "Louie Louie": 245,
        "The Sign": 144,
        "My Sharona": 862,
        "I'll Be There": 184,
        "Call Me Maybe": 251,
        "Burning Heart": 72,
        "All for You": 263,
        "I Don't Want to Wait": 435,
        "Livin' on a Prayer": 366,
        "Let's Dance": 112,
        "We're an American Band": 114,
        "Cat's in the Cradle": 158,
        "Genie in a Bottle": 538,
        "Word Up!": 974,
        "Eye of the Tiger": 802,
        "Pipeline": 51,
        "Starships": 329,
        "Livin' la Vida Loca": 478,
        "Wrecking Ball": 29,
        "Wind Beneath My Wings": 545,
        "Ain't No Mountain High Enough": 250,
        "22": 594,
    },




   """
    # Recursive Approach

    if target_duration == 0:
        return set()
    if target_duration<0 or not songs:
         return None

    song = list(songs.keys())[0]
    duration = songs[song]
    #print(song,duration)
    songs_rest = {key:value for key,value in songs.items() if key!=song}
    #print(songs_rest)
    case1 = mixtape(songs_rest,target_duration-duration)
    case2 = mixtape(songs_rest, target_duration)
    #print(case1)
    if   case1 is not None :
        #print("Hi")
        #print([song]+case1)
        return {song}|case1

    if case2 is not None :
        #print("Hello")
        #print(case2)
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
    import doctest
    print(doctest.testmod())
    songs = {'A': 5, 'B': 10, 'C': 6, 'D': 1}
    print(mixtape(songs, 11))

