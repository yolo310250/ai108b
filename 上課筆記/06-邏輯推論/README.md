# 邏輯推論

## 肯定前項
```
前提 1: -p | q
前提 2: p
-------------------
結論： q
```
p|q|-p\|q
----|---|---
0   |0  |1
0   |1  |1
1   |0  |0
1   |1  |1

在上述表格中，前兩條的 p 為 0，因此不滿足前提 2，而第三條的 -p|q 為 0，不滿足前提 1，因此符合前提的項目就只剩下了一個如下。
p|q|-p\|q
----|---|---
1   |1  |1
## 參考網站

[布林邏輯與公理系統](https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/06-%E9%82%8F%E8%BC%AF%E6%8E%A8%E8%AB%96/A-%E9%82%8F%E8%BC%AF%E6%8E%A8%E8%AB%96%E7%B0%A1%E4%BB%8B?fbclid=IwAR3TcO1VnRARYMOkGXZxIxCYZJiQexcYUGqx53T6CZIlPuEgNZLnZjcbkBo)