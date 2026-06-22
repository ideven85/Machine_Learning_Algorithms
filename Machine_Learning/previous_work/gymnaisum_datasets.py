import gymnasium

envs = gymnasium.envs
print(len(envs.registry))
for key, value in envs.registry.items():
    print(key, value.name, value.to_json(), sep=":")

# with open('gymnasium_available_envs.txt','w+') as f:
#      for key,value in envs.registry.items():
#          f.write(key+':'+str(value.version)+'\n')
