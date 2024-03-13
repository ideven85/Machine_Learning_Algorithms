"""
Extra path finding questions below!
"""

"""
Question 8:
How would you initialize the visited set and agenda for the function below?
"""
def general_actor_path(transformed_data, start_actors, goal_test_function):
    # start actors is a set of actor ids representing valid start of path
    actor_map, _ = transformed_data
    visited =  None # your code
    agenda = None # your code







"""
Question 9:
How would you initialize the visited set and agenda for the function below?
"""
def super_general_actor_path(transformed_data,
                             start_test_function,
                            goal_test_function):
    '''
    start_test_function(actor_id) returns true if actor_id
    is a valid actor to start path from, false otherwise
    '''
    actor_map, _ = transformed_data
    visited = None
    agenda =  None


