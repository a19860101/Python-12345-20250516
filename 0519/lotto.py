# 大樂透 1-49 7

import random

result = []

while len(result) < 7:
    n = random.randint(1,49)
    if n not in result:
        result.append(n)

print(result)
print(f'大樂透號碼為{result[:6]}特別號為{result[-1]}')
print(f'大樂透號碼為{result[1:]}特別號為{result[0]}')