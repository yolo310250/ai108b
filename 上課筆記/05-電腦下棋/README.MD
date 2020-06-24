# 極小極大演算法

Minimax is a decision-making algorithm, typically used in a turn-based, two player games. The goal of the algorithm is to find the optimal next move.

In the algorithm, one player is called the maximizer, and the other player is a minimizer. If we assign an evaluation score to the game board, one player tries to choose a game state with the maximum score, while the other chooses a state with the minimum score.

Minimax演算法常用於棋類等由兩方較量的遊戲和程式。即一方要在可選的選項中選擇將其優勢最大化的選擇，另一方則選擇令對手優勢最小化的方法。

![MINIMAX](minimax.png)

## 參考資料
[minimax](https://www.baeldung.com/java-minimax-algorithm) \
[Min-Max 對局搜尋法](https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/05-%E9%9B%BB%E8%85%A6%E4%B8%8B%E6%A3%8B/C-Min-Max%E5%B0%8D%E5%B1%80%E6%90%9C%E5%B0%8B%E6%B3%95)