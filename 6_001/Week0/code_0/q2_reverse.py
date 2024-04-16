def reverse_all(inp):
    """
    Given a list of lists, return a new list of lists
    but with all of the inner lists reversed, without
    modifying the input list
    """
    # some hidden code below...
    output = []
    for el in inp:
        if isinstance(el, list):
            el.reverse()
            output.append(el)
        else:
            output.append(el)
    return output


def test_reverse_all():
    x = [[1, 2], [3, 4]]
    result = reverse_all(x)
    expected = [[2, 1], [4, 3]]
    assert result == expected


if __name__ == "__main__":
    test_reverse_all()
    print("done!")
