from collections import deque

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_valid(x, y, n, grid):
    return 0 <= x < n and 0 <= y < n and grid[x][y] != 'M'


def bfs(n, grid, start, end):
    water_cost = [[float('inf')] * n for _ in range(n)]
    water_cost[start[0]][start[1]] = 0
    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if is_valid(nx, ny, n, grid):
                cost = 0 if grid[x][y] == 'T' and grid[nx][ny] == 'T' else 1

                if water_cost[x][y] + cost < water_cost[nx][ny]:
                    water_cost[nx][ny] = water_cost[x][y] + cost
                    queue.append((nx, ny))

    return water_cost[end[0]][end[1]]


def main():
    n = int(input())
    grid = []
    start = end = None

    for i in range(n):
        row = input().split()
        grid.append(row)
        for j in range(n):
            if row[j] == 'S':
                start = (i, j)
            elif row[j] == 'E':
                end = (i, j)

    result = bfs(n, grid, start, end)

    print(result)


if __name__ == "__main__":
    main()
