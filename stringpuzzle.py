from collections import defaultdict, deque


def calculate_value(N, edges, words):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    all_words = set()

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
        all_words.add(u)
        all_words.add(v)

    queue = deque([word for word in all_words if in_degree[word] == 0])
    level = {}

    while queue:
        node = queue.popleft()
        if node not in level:
            level[node] = 1

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
            if neighbor not in level:
                level[neighbor] = level[node] + 1

    total_value = 0
    for word in words:
        total_value += level.get(word, -1)

    return total_value


N = int(input())
edges = [input().split() for _ in range(N)]
words = input().split()

print(calculate_value(N, edges, words))