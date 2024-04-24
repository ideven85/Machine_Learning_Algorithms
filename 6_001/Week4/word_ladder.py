# ALL_WORDS is a set containing all strings that should be considered valid
# words (all in lower-case)
with open("words.txt") as f:
    ALL_WORDS = {i.strip() for i in f}

# replace the following with the starting state
start_state = ":)"


def find_path(graph, start, goal_test):
    if goal_test(start):
        return (start,)
    agenda = [(start,)]
    visited = {start}
    while visited:
        this_path = agenda.pop(0)
        terminal_state = this_path[-1]  # Means?

        for neighbour in graph.get(terminal_state, []):
            if neighbour not in visited:
                new_path = this_path + (neighbour,)

                if goal_test(neighbour):
                    return this_path
                agenda.append(new_path)
                visited.add(neighbour)

    return None


# replace this neighbors function:
def word_ladder_neighbors(state):
    """
    takes a state as input
    returns all neighboring states (valid words that differ in one letter)
    """
    return []


# replace this goal test function:
def goal_test_function(state):
    """
    takes a state as input
    returns True if and only if state matches the goal (the target word)
    """
    return False


# ultimately, these variables will be passed as arguments to the find_path
# function to solve for the path between "patties" and "foaming"
#
output = find_path(word_ladder_neighbors, start_state, goal_test_function)
