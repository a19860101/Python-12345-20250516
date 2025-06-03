# Python 資訊視覺化 - 使用Matplotlib
## 基本使用
### 安裝
```commandline
pip install matplotlib
```
### 引用
```python
import matplotlib.pyplot as plt

```
## 折線圖
### 基本
```python
# 引入
import matplotlib.pyplot as plt

# 定義資料
data1 = [20, 24, 32, 18, 26]

# 設定折線圖
plt.plot(data1, color='red', linewidth=1, linestyle=':')
# plt.plot([20, 24, 32, 18, 26])

# 顯示折線圖
plt.show()
```


### 設定樣式
* linewidth or lw
* linestyle or ls
* color
* marker
* markersize or ms

#### linewidth or lw
折線寬度。預設為1
#### linestyle or ls
折線樣式

| 樣式 |  說明  |
|:----:|:------:|
|  -   |  實線  |
|  --  |  虛線  |
|  -.  | 虛點線 |
|  :   | 點狀線 |
