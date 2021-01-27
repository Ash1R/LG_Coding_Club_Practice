recurseSum = lambda x,y: x if x == y else x + recurseSum(x+1, y)
print(recurseSum(5,10))
