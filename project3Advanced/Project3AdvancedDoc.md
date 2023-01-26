# 项目三进阶版

## 1. 爬取1000个python项目

主要在`advancedMain.py`中实现

这里使用了[GitHub Topics](https://github.com/topics/python) 下面的数据。

虽然没有要求尽量爬star多的，但是由于**接下来是要对star进行分析的**，所以我按stars排序，从star最多的[system-design-primer](https://github.com/donnemartin/system-design-primer) 开始爬，一直爬完Top1000 star的python项目。

```python
def get_1000_github_repo() -> None:
```

该函数将前1000个项目路径保存在`./python_repository_list.txt`，方便接下来读取。

```python
def get_information(href: str):
```

这个函数会把题目要求的所有信息爬下来，并返回一个列表包括下面15个值：

- 名称
- 地址
- 星标数(star)
- 复刻数(fork)
- 简介(About)
- Readme
- 主题标(Topic，About 下面)
- 发布版本数量(Release)
- 贡献者数量(Contributors)
- 语言构成(Languages)
- 分支数(Branch)
- 开放议题数(Issues open)
- 关闭议题数(Issues closed)
- 开放拉取请求数(Pull Requests open)
- 关闭拉取请求数(Pull Requests closed)


```python
def save_to_csv():
```

这个函数负责把1000个项目的信息保存到`./python_repository_list.csv`，用numbers打开如图：

![](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project3Advanced/images/csv_image.png)

## 2. 可视化星标数项目排行榜

主要在`visualize_stars.py`中实现。

![代码截图](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project3Advanced/images/code.png)

使用seaborn库画的star前50的项目排行榜：

![](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project3Advanced/images/Figure.png)

## 3. 可视化项目依赖图

主要在`visualize_dependency.py`中实现。

```python
def get_dependency_data() -> int:
# 粗略获取项目依赖（只爬取根目录下的requirements.txt）

def get_complete_data() -> int:
# 获取项目所有的依赖（爬取insight -> dependency中的所有数据）

def draw_dependency_map() -> None:
# 绘制依赖关系图
```

其中`get_dependency_data()`只爬取**根目录下**的`requirements.txt`，爬取速度快。但是爬下来的内容不全，因为有些requirement放在某项目目录下，而且还有各种`setup.py`中也可以定义依赖关系。这个函数会将结果以json形式保存到data文件夹下。

爬取结果：`data/dependency_data.json` \[6684\]行

而`get_complete_data()`能够**获取项目所有的依赖**（爬取insight->dependency中的所有数据），爬取速度较慢。它也会将结果以json形式保存到data文件夹下。

爬取结果：`data/complete_dependency_data.json` \[31629\]行

`draw_dependency_map()`函数使用[networkx库](https://github.com/networkx/networkx)作为绘图引擎，将读入的json文件转化成依赖关系图。

```python
pos = nx.arf_layout(G)
nx.draw_networkx_edges(G, pos, edgelist=el, width=star_list[index] / 100000, alpha=0.5, edge_color='b')
nx.draw_networkx_nodes(G, pos, alpha=0.5, node_size=100, edgecolors="b", node_color="w", linewidths=0.5)
nx.draw_networkx_labels(G, pos, font_size=5, font_color="r", font_family=["Fira Code"], font_weight="bold")
```

这4行代码负责绘图，由于用下来arf_layout图最清晰，接下来的图像都用的是arf_layout。

有向边（出度入度）用的是**0.5透明度的蓝色线条**，根据项目星标数多少变化粗细。

节点用的是**0.5透明度的白底蓝框圆圈**，线条粗0.5，因为这样好看。

最后label用的是Fira Code等宽字体，并红色加粗便于辨认。

1. 用粗略获取的项目依赖数据绘制而成的图像：

（线条越粗说明star越多）

[Figure3](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project3Advanced/images/Figure3.png)

2. 用完整版的数据：

- Fira Code常规体 Top100

[Figure4](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project3Advanced/images/Figure4.png)

- Fira Code粗体 Top100

[Figure5](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project3Advanced/images/Figure5.png)

- Top200开开眼

[Figure6](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project3Advanced/images/Figure5.png)

但是好像两者的数据差异并非肉眼可见，那是因为我在代码里滤去了没有进入top100的项目，因此绝大部分依赖都没用上。
