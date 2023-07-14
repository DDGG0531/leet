from collections import defaultdict


def test(equations, values, queries):
    graph = defaultdict(dict)

    for equation, value in zip(equations, values):
        a, b = equation
        graph[a][b] = value
        graph[b][a] = 1 / value

    def dfs(start, end, seen):
        if start == end and start in graph:
            return 1

        if start not in graph:
            return -1

        for neighbor in graph[start]:
            val = graph[start][neighbor]
            if neighbor not in seen:
                seen.add(neighbor)
                times = dfs(neighbor, end, seen)
                if times > 0:
                    return times * val
        return -1

    return [dfs(pair[0], pair[1], set({pair[0]})) for pair in queries]


print(
    test(
        equations=[["x1", "x2"]],
        values=[3.0],
        queries=[["x9", "x1"], ["x9", "x9"]],  # [-1.00000,-1.00000]
    )
)

# print(
#     test(
#         equations=[["a", "b"], ["b", "c"]],
#         values=[2.0, 3.0],
#         queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
#     )
# )

# print(
#     test(
#         equations=[["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]],
#         values=[3.0, 4.0, 5.0, 6.0],
#         queries=[
#             ["x1", "x5"],
#             ["x5", "x2"],
#             ["x2", "x4"],
#             ["x2", "x2"],
#             ["x2", "x9"],
#             ["x9", "x9"],
#         ],
#     )
# )
