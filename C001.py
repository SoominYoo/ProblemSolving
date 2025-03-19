#N 크기 입력 받기
n = int(input())

#자물쇠가 있는 그리드 입력하기
grid = [list(map(int, input().split())) for _ in range(n)]

# 해당 범위를 벗어나지 않도록 하기(3<=N<=20)
if(n<3 or n>20):
    print("Invalid Input")

# nxn 격자 내에 있는지 체크
def in_range(x, y):
    return 0 <= x+2 < n and 0<= y+2 < n

ans = 0
for x in range(n):
    for y in range(n):
        if in_range(x, y):
            cnt = 0
            for i in range(3):
                for j in range(3):
                    cnt += grid[x+i][y+j]
            ans = max(ans, cnt)

print(ans) 
