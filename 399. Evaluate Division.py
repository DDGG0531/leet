from collections import defaultdict


def test(equations, values, queries):
    graph = defaultdict(list)
    path_map = defaultdict(dict)

    for index, (a, b) in enumerate(equations):
        graph[a].append(b)
        graph[b].append(a)
        path_map[a][b] = values[index]
        path_map[b][a] = 1 / values[index]
    print(graph)
    print(path_map)

    def dfs(start, end, value, seen):
        # hack
        if start == end:
            return value if start in graph else -1
        if end not in graph:
            return -1

        for neighbor in graph[start]:
            print("neighbor", neighbor)
            if neighbor not in seen:
                seen.add(neighbor)
                if neighbor == end:
                    return value * path_map[start][neighbor]
                else:
                    return dfs(neighbor, end, value * path_map[start][neighbor], seen)

    return [dfs(pair[0], pair[1], 1, set({pair[0]})) for pair in queries]


# print(
#     test(
#         equations=[["a", "b"], ["b", "c"]],
#         values=[2.0, 3.0],
#         queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
#     )
# )

print(
    test(
        equations=[["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]],
        values=[3.0, 4.0, 5.0, 6.0],
        queries=[
            # ["x1", "x5"],
            # ["x5", "x2"],
            # ["x2", "x4"],
            # ["x2", "x2"],
            # ["x2", "x9"],
            # ["x9", "x9"],
            ["x2", "x4"],
        ],
    )
)
