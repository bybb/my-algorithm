# 거스름돈

# 내가 생각해서 풀어논 거 날아갔다...
# 그래서 기억나는 대로 풀었다.

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)