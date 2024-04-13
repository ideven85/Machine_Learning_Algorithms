"""
/etc/ssh/ssh_config
https://py.mit.edu/spring24/ssh_keys/key-add
https://py.mit.edu/spring24/ssh_keys/key-add?loginaction=login
Use sorted and string builtins to make these functions one line!
"""


def color_str(colors):
    """Takes a list of colors, sorts them alphabetically
    and places them in a string separated by spaces"""
    # how can we write this in one line?
    return " ".join(sorted(colors[:])).strip()


def word_lst(word_str):
    """Take a string of words separated by spaces and
    make a list of individual word strings"""
    # how can we write this in one line?
    return word_str[:].split(" ")


def sort_word_len(word_lst):
    """Given a list of words, create a new list where the
    words are sorted from longest to shortest"""
    return sorted(word_lst[:], reverse=True, key=len)


def sort_movies(movies, ratings):
    """
    Return a new list of movies sorted by the rating from
    lowest to highest
    """
    return [movie for movie, rating in sorted(zip(movies, ratings), key=lambda y: y[1])]


def check(result, expected):
    if isinstance(expected, float):
        assert abs(result - expected) <= 1e-6, f"got {result=} but {expected=}"
    else:
        assert result == expected, f"got {result=} but {expected=}"


if __name__ == "__main__":
    movies = ["Alien", "Barbie", "Clue", "Frozen", "Inception"]
    ratings = [7.3, 8.4, 7.2, 7.4, 8.5]
    colors = ["red", "green", "blue", "yellow", "chartreuse", "periwinkle"]

    exp_str = "blue chartreuse green periwinkle red yellow"
    check(color_str(colors), exp_str)
    exp_lst = ["blue", "chartreuse", "green", "periwinkle", "red", "yellow"]
    check(word_lst(exp_str), exp_lst)
    len_lst = ["chartreuse", "periwinkle", "yellow", "green", "blue", "red"]
    check(sort_word_len(colors), len_lst)
    exp_movies = ["Clue", "Alien", "Frozen", "Barbie", "Inception"]
    check(sort_movies(movies, ratings), exp_movies)

    print("all correct!")
