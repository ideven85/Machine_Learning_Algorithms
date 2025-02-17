def looping():
    snacks = [("chilli",90),("bacon",120),("vanilla",12)]
    for rank,(item,price) in enumerate(snacks,1):
        print(f"Number {rank} item={item} costs {price}")
    for rank in range(1,len(snacks)):
        print(rank,snacks[rank][0],snacks[rank][1])
looping()