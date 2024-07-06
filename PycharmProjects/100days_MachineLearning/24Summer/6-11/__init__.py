n, m = map(int, input().split())

g = []
for i in range(n):
    g.append(list(map(int, input().split())))

dis = [[-1] * m for i in range(n)]
q = []

for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            dis[i][j] = 0
            q.append((i, j))

while q:
    x, y = q.pop(0)
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] != -1 and dis[nx][ny] == -1:
            dis[nx][ny] = dis[x][y] + 1
            q.append((nx, ny))

ans = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 1 and dis[i][j] != -1:
            ans += dis[i][j]

print(ans)