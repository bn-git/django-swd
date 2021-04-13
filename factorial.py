inp = int(input('Pls enter your Factorial Number! : '))
fact = 1
for ind in range(inp + 1):
    if ind > 0:
        fact = fact*ind
index = []
for ind in str(fact):
    index.append(ind)

indexs = list(reversed(index))

count = 0
for ind in indexs:
    if int(ind) == 0:
        count += 1
    else:
        break

print("Total last sticking zero from factorial number : %s Values is : %s"%(count,fact))
