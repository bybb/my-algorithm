# https://www.acmicpc.net/problem/2845

l, p = map(int, input().split())

a, b, c, d, e = map(int, input().split())
base = l * p

print(a-base, b-base, c-base, d-base, e-base)