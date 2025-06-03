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
如果只有一份資料，這份資料會是y座標，x座標則是索引直
```python
# 引入
import matplotlib.pyplot as plt

# 定義資料
data1 = [20, 24, 32, 18, 26]
# (0,20)(1,24)(2,32)(3,18)(4,26)

# 設定折線圖
plt.plot(data1, 
         color='red', 
         linewidth=1, 
         linestyle=':')
# plt.plot([20, 24, 32, 18, 26])

# 顯示折線圖
plt.show()
```
通常都會有兩份資料，水平座標與垂直座標
```python
import matplotlib.pyplot as plt

dataX = [1, 3, 5, 7, 9]
dataY = [20, 24, 32, 18, 26]

# (1,20)(3,24)(5,32)(7,18)(9,26)
plt.plot(dataX,dataY,
         color='red',
         linewidth=1.5,
         linestyle='-',
         marker=".",
         markersize=15)

# marker:標記、markersize:標記大小

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

#### marker 

標記樣式

|  樣式   |  說明  |
|:-------:|:------:| 
|    o    |   圓   |
|    .    |   點   |
|    *    |   星   |
|    +    |  十字  |
|    x    |  叉叉  |
|    _    |  橫線  |
|    \|   | 直線 |
|   ^,v   | 三角形 |
|    s    |  矩形  |
|    p    | 五邊形 |
|   h,H   | 六邊形 |
|   d,D   |  鑽型  |
| 1,2,3,4 | 人字形 |
