# VENV的安裝
## Installing virtualenv
```
py -m pip install --user virtualenv
```
## 啟動venv
```
C:\Users\EASON\Desktop\class\AI\ai2\env> cd ..
PS C:\Users\EASON\Desktop\class\AI\ai2> .\env\Scripts\activate
(env) PS C:\Users\EASON\Desktop\class\AI\ai2>
```
## install pytorch
```
pip install torch
```
遇到報錯 ModuleNotFoundError: No module named 'tools.nnwrap'
`解決方法 https://pytorch.org/get-started/locally/ 到官網選擇自己電腦的版本，複製指令即可`
## 執行main.py
```
(env) PS C:\Users\EASON\Desktop\class\AI\ai2\python\11-deepLearning\01-pytorch\tutorial> python
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> import torch
>>> import torchvision
>>> import torch.nn as nn
>>> import numpy as np
>>> import torchvision.transforms as transforms
>>> x = torch.tensor(1., requires_grad=True)
>>> w = torch.tensor(2., requires_grad=True)
>>> b = torch.tensor(3., requires_grad=True)
>>> y = w * x + b
>>> y.backward()
>>> print(x.grad) x的梯度
tensor(2.)
>>> print(w.grad) w的梯度
tensor(1.)
>>> print(b.grad) b的梯度
tensor(1.)
>>> 
```