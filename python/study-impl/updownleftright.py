n = int(input())
move = list(map(str, input().split()))
x = 1
y = 1

for m in range(len(move)):
    if(move[m]=='L' and x!=1):
        x -= 1
    if(move[m]=='R' and x!=n):
        x += 1
    if(move[m]=='U' and y!=1):
        y -= 1
    if(move[m]=='D' and y!=n):
        y += 1
    
print(y, x)