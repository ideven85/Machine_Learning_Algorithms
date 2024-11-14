import gymnasium.envs

with open('envs.txt', 'w') as f:
    for env in gymnasium.envs.registry:
        f.write(f"{env}\n")

