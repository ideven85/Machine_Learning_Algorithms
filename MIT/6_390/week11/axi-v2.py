# %% [markdown]
# ## Solving OpenAI Gym Environment - (Taxi-v2)
#
# In this Python demo, we'll try solving the classic cab-driver problem. The purpose of this notebook is to show how to solve OpenAI Gym environments. We'll demonstrate Q-learning & SARSA on the Taxi environment.
#
# Let's now look at the problem statement
#
# Here, the objective is to pick up the passenger from one position and drop them off at another in minimum possible time. For this problem, we'll consider our environment to be a 5x5 grid.
#
# <img src="cab_problem.png" style="width: 300px;">
# Image source: https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/
#
# There are 4 locations (R, G, Y, B) marked in the image. And the task is to pick up the passenger from one of the four locations and drop him off at other. There is a reward of +20 for a successful dropoff, and -1 for every timestep it takes and -10 for illegal pick-up and drop-off actions.
# %%
# Import routines
import numpy as np
import random
import time
import gymnasium as gym

# %% [markdown]
# ### Calling the environment
# %%
env = gym.make("Taxi-v2")  # Create environment

state = env.reset()
env.render()  # helps in visualizing the environment

print("current state is :", state)
# %% [markdown]
# #### Rendering:
#     - yellow: taxi is unoccupied
#     - green: taxi is occupied by a passenger
#     - blue: passenger
#     - magenta: destination
#     - other grids: locations
#
# That means, for now, I'm at yellow box and need to pick the passenger from 'G' and drop him off at 'B'
# %% [markdown]
# ### State Space
#
# The state vector for this problem is (col_index, row_index, destination_locations, passenger_position)
# There are 5 rows, 5 columns and 4 destination locations. What about the passenger locations? 4 or 5?
#
# If the passenger is not in cab that means he could be only at one of the four locations. But we also need to account for 1 addition state if the passenger is inside the cab. So, passenger could be at any 4+1 possible locations.
#
# Therefore, the state space = 5x5x4x5 = 500
# %%
# Number of possible states
state_size = env.observation_space.n
print("State space : ", state_size)
# print("Current state : " ,env.env.s)
# %% [markdown]
# ### Action Space
#
# At any state, the cab driver can either move in any of the four directions or it can pickup/ drop (legally or illegally)
#
#     - 0: south
#     - 1: north
#     - 2: east
#     - 3: west
#     - 4: pickup
#     - 5: drop
#
# %%
# Number of possible actions
action_size = env.action_space.n
print("Action space : ", action_size)
# %% [markdown]
# ### Training
#
# Let's know solve the given MDP using Q-learning & SARSA.
#
# ### Q-Learning
# Q-Learning is an off-policy optimal control algorithm. It learns the Q-values by taking the next action based on the greedy policy
# %%
# Initialise q-table with zeros
Q_table = np.zeros((state_size, action_size))
print(Q_table)
# %%
episodes = 100000  # Total episodes

# hyperparameters
learning_rate = 0.1  # Learning rate
gamma = 0.8  # discount factor
epsilon = 0.1  # exploration -exploitation tradeoff


# %%
# Keeping the policy epsilon-greedy
def epsilon_greedy(state, table):
    z = np.random.random()  # Randomizes a number to select whether or not to expolit

    if z > epsilon:
        action = np.argmax(
            table[state]
        )  # Exploitation: this gets the action corresponding to max q-value of current state
    else:
        action = env.action_space.sample()  # Exploration: randomly choosing and action

    return action


# %%
start = time.time()  # tracking time
deltas = []
for episode in range(1, episodes + 1):
    state = env.reset()  # Reset the environment
    done = False  # 'done' defines successfully dropping the passenger off;
    # resulting in an end of episode
    step = 0
    biggest_change = 0  # to keep a track of difference in the Q-values

    if episode % 5000 == 0:
        print("Episode: {}".format(episode))

    while not done:
        action = epsilon_greedy(state, Q_table)

        # Take the action and observe the new state and reward
        new_state, reward, done, info = env.step(action)

        oldQ_table = Q_table[state, action]

        # UPDATE RULE
        Q_table[state, action] += learning_rate * (
            reward + gamma * np.max(Q_table[new_state, :]) - Q_table[state, action]
        )

        biggest_change = max(
            biggest_change, np.abs(Q_table[state][action] - oldQ_table)
        )

        state = new_state

    deltas.append(biggest_change)

    if deltas[-1] < 0.00000001:
        break

    episode += 1


end = time.time()
training_time = end - start
print("Time taken in seconds: ", training_time)
print("maximum difference: ", deltas[-1])
# %%
Q_table[454]
# %% [markdown]
# #### Testing the Q-Table
#
# Let's know test our Q-learning agent on a different environment
# %%
# Let's change the environment
state = env.reset()  # reset will set the environment to a new and random state
env.render()
# %%
from IPython.display import clear_output

done = False
cumulative_reward = 0

while done == False:
    best_action = np.argmax(
        Q_table[state, :]
    )  # selecting the best action basis Q-table

    # Take the best action and observe the new state and reward
    state, reward, done, info = env.step(best_action)
    cumulative_reward += reward

    time.sleep(0.5)
    clear_output(wait=True)
    env.render()
    print("Episode Reward = ", cumulative_reward)
# %% [markdown]
# ### SARSA
#
# SARSA is on-policy learning algorithm. Unlinke Q-learning, it learns the Q-values by taking the next action based on the current policy rather than a greedy policy
# %%
state = env.reset()
env.render()  # helps in visualizing the environment

print("current state is :", state)
# %%
# Initialise sarsa-table with zeros
Sarsa_table = np.zeros((state_size, action_size))
print(Sarsa_table)
# %%
episodes = 800000
start = time.time()  # tracking time
deltas = []
for episode in range(1, episodes + 1):
    state = env.reset()  # Reset the environment
    done = False  # 'done' defines successfully dropping the passenger off;
    # resulting in an end of episode
    step = 0
    biggest_change = 0  # to keep track of difference in Q-values

    if episode % 10000 == 0:
        print("Episode: {}".format(episode))

    while not done:
        action = epsilon_greedy(state, Sarsa_table)

        # Take the action and observe the new state and reward
        next_state, reward, done, info = env.step(action)
        # Get the action basis epsilon greedy policy
        next_action = epsilon_greedy(next_state, Sarsa_table)

        oldSarsa_table = Sarsa_table[state, action]

        # UPDATE RULE
        Sarsa_table[state, action] += learning_rate * (
            reward
            + gamma * Sarsa_table[next_state, next_action]
            - Sarsa_table[state, action]
        )

        biggest_change = max(
            biggest_change, np.abs(Sarsa_table[state][action] - oldSarsa_table)
        )

        state = new_state

    deltas.append(biggest_change)

    if deltas[-1] < 0.00000001:
        break

    episode += 1


end = time.time()
training_time = end - start
print("Time taken in seconds: ", training_time)
print("maximum difference: ", deltas[-1])
# %%
Sarsa_table
# %%
Sarsa_table[263]
# %% [markdown]
# #### Testing the SARSA table
#
# Let's know test our SARSA agent on a different environment
# %%
# Let's change the environment
state = env.reset()  # reset will set the environment to a new and random state
env.render()
# %%
from IPython.display import clear_output

done = False
cumulative_reward = 0

while done == False:
    best_action = np.argmax(
        Sarsa_table[state, :]
    )  # selecting the best action basis Sarsa-table

    # Take the best action and observe the new state and reward
    state, reward, done, info = env.step(best_action)
    cumulative_reward += reward

    time.sleep(0.5)
    clear_output(wait=True)
    env.render()
    print("Episode Reward = ", cumulative_reward)
# %%
