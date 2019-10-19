import random
i = 1
m = 0
x = []
y = []
for i in range(1000):
    x = random.random()
    y = random.random()
    if x * x + y * y > 0.25 and x * x + (y - 1) * (y - 1) > 0.25 and (x - 1) * (x - 1) + y * y > 0.25\
            and (x - 1) * (x - 1) + (y - 1) * (y - 1) > 0.25:
        m = m+1
s = m/1000
print("面积是", float(s))

