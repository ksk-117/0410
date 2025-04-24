import matplotlib.pyplot as plt
import numpy as np

# ナップサック問題の動的計画法
def knapsack(weights, values, W):
    n = len(weights)
    dp = np.zeros((n+1, W+1))

    # 動的計画法で計算
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
                
    # 結果の表示
    return dp[n][W], dp

# ナップサックの重さと価値
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
W = 7

# 可視化のために動的計画法を実行
max_value, dp_table = knapsack(weights, values, W)

# 結果の表示
print(f"Maximum value in Knapsack: {max_value}")

# 動的計画法のテーブルを可視化
plt.imshow(dp_table, cmap='Blues', interpolation='nearest')
plt.title('Dynamic Programming Table')
plt.xlabel('Capacity (W)')
plt.ylabel('Items (n)')
plt.colorbar()
plt.show()