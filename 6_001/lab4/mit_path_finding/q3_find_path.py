"""
Question 3: Implement find_path below.
(hint: you may want to start by taking the code from can_reach
and modifying it as described in the maze path finding section
at the bottom of the Flood Fill readings)

You can test this function by running `pytest q3_find_path.py -v`
in the terminal. After you pass the small test cases, try commenting
out the large test cases at the bottom.
"""

from q2_can_reach import can_reach

def find_path(map, start_building, goal_building):
    """
    same arguments as can_reach()

    returns a tuple of directly-connected buildings from start_building
    to goal_building or None if no possible path in map
    """




# from http://whereis.mit.edu/?zoom=18&lat=42.36162996081668&lng=-71.09057574701308&maptype=mit&open=-1
# (and not using tunnels)
small_map = {
    '26': {'36'}, # 26 connects to 36
    '32': {'36'}, # 32 connects to 36
    '36': {'26', '32'}, # 36 connects to both of the others
    '76': set()   # Koch building is by itself
}


def test_can_reach_small():
    assert can_reach(small_map, '26', '32')
    assert can_reach(small_map, '36', '36')
    assert not can_reach(small_map, '76', '32')

def test_find_path_small():
    assert find_path(small_map, '26', '32') == ('26', '36', '32')
    assert find_path(small_map, '36', '36') == ('36',)
    assert find_path(small_map, '76', '32') == None

# from http://whereis.mit.edu/?zoom=17&lat=42.35983737457077&lng=-71.09177737665175&maptype=mit&open=-1
large_map = {
 '1': {'5', '3'},
 '10': {'4', '3'},
 '11': {'3'},
 '12': {'16', '13', '26'},
 '13': {'9', '12'},
 '14': {'18', '2'},
 '16': {'56', '8', '12'},
 '17': {'33'},
 '18': {'56', '14'},
 '2': {'14', '6', '4'},
 '24': {'34'},
 '26': {'32', '12', '36'},
 '3': {'7', '11', '1', '10'},
 '31': {'37'},
 '32': {'26', '57', '36'},
 '33': {'9', '17', '35'},
 '34': {'36', '24', '38'},
 '35': {'37', '33'},
 '36': {'32', '26', '34'},
 '37': {'39', '31', '35'},
 '38': {'39', '34'},
 '39': {'37', '38'},
 '4': {'2', '8', '10'},
 '41': {'42'},
 '42': {'43', '41'},
 '43': {'42'},
 '45': {'46'},
 '46': {'45'},
 '48': set(),
 '5': {'7', '1'},
 '50': set(),
 '54': set(),
 '56': {'16', '66', '18'},
 '57': {'32'},
 '6': {'2', '8', '6C'},
 '62': {'64'},
 '64': {'62'},
 '66': {'56', '68', 'E17'},
 '68': {'66'},
 '6C': {'6', '8'},
 '7': {'5', '9', '3', '7A'},
 '76': set(),
 '7A': {'7'},
 '8': {'6', '4', '6C', '16'},
 '9': {'7', '13', '33'},
 'E1': set(),
 'E14': {'E15'},
 'E15': {'E14'},
 'E17': {'E18', '66'},
 'E18': {'E25', 'E19', 'E17'},
 'E19': {'E18'},
 'E2': set(),
 'E23': {'E25'},
 'E25': {'E18', 'E23'},
 'E28': set()
}

# print(f"{find_path(large_map, '1', '2')=}")
# print(f"{find_path(large_map, '1', '32')=}")
# print(f"{find_path(large_map, '7', '62')=}")


"""
Question 4:
What are the similarities between can_reach and find_path?
Rewrite can_reach() in terms of the find_path() function.

Question 5: Consider the following questions:
How does this week's flood fill reading relate to this week's Bacon Number lab?
How does finding paths through a maze relate to finding Bacon paths?
How does finding paths at MIT relate to finding Bacon paths?
What is a Bacon number in analogy to a MIT building path?
"""