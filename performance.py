import time
import random
from quick_sort import quick_sort

# ランダムなリストを生成して実行時間を計測
arr = random.sample(range(1, 10001), 1000)  # リストサイズ1000のランダムな整数リスト

start_time = time.time()
quick_sort(arr)  # quick_sort関数を実行
end_time = time.time()

execution_time = end_time - start_time  # 実行時間を計算
print(f"Execution Time: {execution_time} seconds")

# 実行結果:
# Execution Time: 0.4854164123535156 seconds