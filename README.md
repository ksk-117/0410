# アルゴリズムとデータ構造1 - 実装とユニットテスト

## 実装したアルゴリズム
このプロジェクトでは以下のアルゴリズムを実装しました：

- 線形探索法 (Linear Search)
- 二分探索法 (Binary Search)
- 挿入ソート (Insertion Sort)
- マージソート (Merge Sort)
- クイックソート (Quick Sort)
- ヒープソート (Heap Sort)

## テストについて
すべてのアルゴリズムについて、Pythonの `unittest` を用いてテストを実施しました。

### テスト観点
- 正常系: ソートや探索が正しく行われるかどうか
- 異常系: 存在しない要素の探索に対して正しく `-1` を返すか（探索法）
- ソート結果が標準ライブラリの `sorted()` 関数と一致しているか（ソート法）

## 実行方法
```bash
python -m unittest test_algorithms.py
```