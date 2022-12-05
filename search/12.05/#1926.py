import sys
n,m = map(int,input().split())
graph = list(list(map(int,input().split())) for _ in range(n))
visited = [[False]*m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    global cnt
    cnt += 1
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if visited[nx][ny] == False and graph[nx][ny] == 1:
                dfs(nx,ny)
area = 0
ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            cnt = 0
            dfs(i,j)
            area += 1
            ans = max(ans,cnt)
print(area)
print(ans)