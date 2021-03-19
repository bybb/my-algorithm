import time
n = int(input())
result = 0
start_time = time.time()
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if h%10 == 3 or m%10 == 3 or 30 <= m < 40 or s%10 == 3 or 30 <= s < 40:
            #if s%10 == 3 or 30 <= s < 40 or m%10 == 3 or 30 <= m < 40 or h%10 == 3:
            #설마하고 해봤는데 둘은 별차이없음
                result += 1
end_time = time.time()
print(end_time-start_time)
print(result)


result = 0
start_time = time.time()
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                result += 1

end_time = time.time()
print(end_time-start_time)
print(result)
