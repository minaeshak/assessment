import random
output=[]
for i in range(0,10):
    x = random.randint(1, 10)
    while (True):
        if (x not in output):
            output.append(x)
            break
        else:
            x = random.randint(1, 10)

print(output)  

