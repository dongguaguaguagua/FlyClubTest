# 项目三进阶版

## 1. 爬取1000个python项目

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

## 2. dependency
