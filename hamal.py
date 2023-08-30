def is_valid(graph, path, v, pos):
    if graph[path[pos - 1]][v] == 0:
        return False
    if v in path:
        return False
    return True

def hamiltonian_cycle_util(graph, path, pos):
    if pos == len(graph):
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    for v in range(1, len(graph)):
        if is_valid(graph, path, v, pos):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True
            path[pos] = -1

    return False

def hamiltonian_cycle(graph):
    path = [-1] * len(graph)
    path[0] = 0

    if hamiltonian_cycle_util(graph, path, 1):
        return path
    else:
        return None

# Taking user input for the number of vertices
n = int(input("Enter the number of vertices: "))
graph = [[0] * n for _ in range(n)]

# Taking user input for the graph's adjacency matrix
print("Enter the adjacency matrix (space-separated values):")
for i in range(n):
    row = input().split()
    for j in range(n):
        graph[i][j] = int(row[j])

cycle = hamiltonian_cycle(graph)
if cycle:
    print("Hamiltonian cycle:", cycle)
else:
    print("No Hamiltonian cycle exists")
