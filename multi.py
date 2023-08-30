def multistage_graph(graph, stages):
    n = len(graph)
    cost = [0] * n
    next_node = [0] * n

    for i in range(n - 2, -1, -1):
        min_cost = float('inf')
        for j in range(i + 1, n):
            if graph[i][j] != float('inf'):
                current_cost = graph[i][j] + cost[j]
                if current_cost < min_cost:
                    min_cost = current_cost
                    next_node[i] = j
        cost[i] = min_cost

    path = [0]
    current_node = 0
    while current_node != n - 1:
        current_node = next_node[current_node]
        path.append(current_node)

    return cost[0], path

# Taking user input for the number of nodes, cost matrix, and stages
n = int(input("Enter the number of nodes: "))
graph = []
for i in range(n):
    row = []
    for j in range(n):
        cost = float('inf')
        if i == j:
            cost = 0
        else:
            cost_input = input(f"Enter cost from node {i} to {j} (or 'inf' for no direct edge): ")
            if cost_input != 'inf':
                cost = int(cost_input)
        row.append(cost)
    graph.append(row)

stages = int(input("Enter the number of stages: "))
min_cost, optimal_path = multistage_graph(graph, stages)
print("Minimum cost:", min_cost)
print("Optimal path:", optimal_path)
