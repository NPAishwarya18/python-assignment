import numpy as np

def calculate_lower_bound(cost_matrix, assignment):
    n = cost_matrix.shape[0]
    lower_bound = 0

    for row, col in assignment:
        lower_bound += cost_matrix[row, col]

    for row in range(n):
        if all(col != assignment[row][1] for _, col in assignment):
            min_cost = np.min(cost_matrix[row])
            lower_bound += min_cost

    return lower_bound

def branch_and_bound_assignment(cost_matrix):
    n = cost_matrix.shape[0]
    best_assignment = None
    best_cost = float('inf')

    def backtrack(assignment, row):
        nonlocal best_assignment, best_cost
        if row == n:
            current_cost = sum(cost_matrix[row, col] for row, col in assignment)
            if current_cost < best_cost:
                best_cost = current_cost
                best_assignment = assignment.copy()
            return

        for col in range(n):
            if all(col != assignment[row][1] for row, _ in assignment):
                new_assignment = assignment.copy()
                new_assignment[row] = (row, col)
                lower_bound = calculate_lower_bound(cost_matrix, new_assignment)
                if lower_bound <= best_cost:
                    backtrack(new_assignment, row + 1)

    backtrack(np.empty((n, 2), dtype=int), 0)

    return best_assignment, best_cost

# Example cost matrix
cost_matrix = np.array([
    [8, 5, 9],
    [6, 7, 12],
    [10, 8, 5]
])

assignment, cost = branch_and_bound_assignment(cost_matrix)
print("Assignment:")
for i, j in assignment:
    print(f"Task {i+1} assigned to Agent {j+1}")
print("Total Cost:", cost)
