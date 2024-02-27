a = [i for i in range(4)]
height = 2
width = 2
#result = [[a[i] for i in range(height)]  for a[height] in range(width)]
# for i in range(width):
#     k = width+1
#     for j in range(height):
#         result[i][j] =a[j:k]
listA = [i for i in range(6)]

# Length of 2D lists needed
len_2d = [ 2, 4]

#Declare empty new list
res = []
def convert(listA, len_2d):
   idx = 0
   for var_len in len_2d:
      res.append(listA[idx: idx + var_len])
      idx += var_len
convert(listA, len_2d)
print("The new 2D lis is: \n",res)