import pandas
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", context="talk")

plt.rcParams['font.family'] = 'Arial Unicode MS'  # 解决中文字体无法显示问题
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）

csv = pandas.read_csv("./python_repository_list.csv", encoding="utf8")
# 取前50条数据
x = csv['名称'][:50]
y = csv['星标数(star)'][:50]
for i in range(len(x)):
    if len(x[i]) > 12:
        x[i] = x[i][:12] + "..."

ax = sns.barplot(x=y, y=x, palette="rocket")
plt.xticks(fontsize=15)
plt.yticks(fontsize=10)
plt.show()
