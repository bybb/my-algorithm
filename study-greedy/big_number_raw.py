# '큰 수의 법칙'은 일반적으로 통계 분야에서 다루어지는 내용이지만 동빈이는 본인만의 방식으로 다르게 사용하고 있다.
# 동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
# 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.
# 예를 들어 순서대로 2, 4, 5, 4, 6으로 이루어진 배열이 있을 때 M이 8이고, K가 3이라고 가정하자.
# 이 경우 특정한 인덱스의 수가 연속으로 세 번까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과는 6+6+6+5+6+6+6+5인 46이 된다.
# 단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다. 
# 예를 들어 순서대로 3, 4, 3, 4, 3으로 이루어진 배열이 있을 때 M이 7이고, K가 2라고 가정하자. 이 경우 두 번째 원소에 해당하는
# 4와 네 번째 원소에 해당하는 4를 번갈아 두 번씩 더하는 것이 가능하다. 결과적으로 4+4+4+4+4+4인 28이 도출된다.
# 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 떄 동빈의 큰 수의 법칙에 따른 결과를 출력하시오.

# 내 생각 - big_number_raw_memo.png 참조

# N, M, K를 공백으로 구분하여 입력받기
import time
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

start_time = time.time()
answer = 0
count = m

data.sort(reverse=True)

while m > 0:
    if m > k:
        answer += (data[0] * k) + data[1]  
        m -= k + 1
    else:
        answer += data[0] * m
        break

print(answer)
end_time = time.time()
a = end_time-start_time

# 단순하게 푸는 답안 예시

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

start_time = time.time()

data.sort() # 입력받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 떄 마다 1씩 빼기
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한번 더하기
    m -= 1 # 더할 때 마다 1씩 뺴기

print(result)
end_time = time.time()
b = end_time-start_time

# 답안 예시

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

start_time = time.time()
data.sort() # 입력받은 수 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)
end_time = time.time()
c = end_time-start_time

if(a>b and a>c):
    if(b>c):
        print("c가 제일 빠르고 그 다음 b 그 다음 a")
    else:
        print("b가 제일 빠르고 그 다음 c 그 다음 a")
elif(b>a and b>c):
    if(a>c):
        print("c가 제일 빠르고 그 다음 a 그 다음 b")
    else:
        print("a가 제일 빠르고 그 다음 c 그 다음 b")
else:
    if(a>b):
        print("b가 제일 빠르고 그 다음 a 그 다음 c")
    else:
        print("a가 제일 빠르고 그 다음 b 그 다음 c")
