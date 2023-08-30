def optimal_bst(keys, freq):
    n = len(keys)
    cost = [[0] * n for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')
            freq_sum = sum(freq[i:j+1])

            for r in range(i, j + 1):
                left_cost = 0 if r == i else cost[i][r - 1]
                right_cost = 0 if r == j else cost[r + 1][j]
                subtree_cost = left_cost + right_cost + freq_sum
                cost[i][j] = min(cost[i][j], subtree_cost)

    return cost[0][n - 1]

# Taking user input for keys and frequencies
n = int(input("Enter the number of keys: "))
keys = []
freq = []

for i in range(n):
    key = int(input(f"Enter key {i+1}: "))
    frequency = int(input(f"Enter frequency for key {i+1}: "))
    keys.append(key)
    freq.append(frequency)

print("Optimal BST cost:", optimal_bst(keys, freq))
