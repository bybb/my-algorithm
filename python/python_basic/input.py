# 기본 입출력
# 모든 프로그램은 적절한(약속된) 입출력 양식을 가지고 있다.
# 프로그램 동작의 첫 번째 단계는 데이터를 입력 받거나 생성하는 것이다.

# 자주 사용되는 표준 입력 방법
# input() 함수는 한줄의 문자열을 입력 받는 함수이다.
# map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용한다.
# 예시) 공백을 기준으로 구분된 데이터를 입력 받을 때는 다음과 같이 사용한다.
# list(map(int, input().split()))
# 예시) 공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 단순히 다음과 같이 사용한다.
# a, b, c = map(int, input().split())

# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# n, m, k를 공백을 기준으로 구분하여 입력
n, m, k = map(int, input().split())

print(n, m, k)

# 빠르게 입력받기
# 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우가 있다.
# 파이썬의 경우 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메서드를 이용한다.
# 단, 입력 후 엔터(Enter)가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용한다.

import sys

# 문자열 입력받기
data = sys.stdin.readline().rstrip()
print(data)


