import random

area1 = random.sample(range(1,39),6)
area2 = random.sample(range(1,9),1)

area1 = ','.join(str(a1) for a1 in area1)

print(area1,area2)
print(f'第一區號碼為:{area1}\n第二區號碼為:{area2[0]}')

