# 人物社交网络分析
import networkx as nx
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

df_net = pd.read_csv("weight.csv")
df_net['weight'] = df_net.chapweight/120
df_net2 = df_net[df_net['weight'] > 0.45].reset_index(drop=True)
plt.figure(figsize=(12, 12))
plt.rcParams['font.family'] = 'Arial Unicode MS'  # 解决中文字体无法显示问题
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）
# 生成社交图
G = nx.Graph()
# 添加边
for i in df_net2.index:
    G.add_edge(df_net2.First[i], df_net2.Second[i], weight=df_net2.weight[i])
# 定义三种边，以便后续不同边设置不同的参数
elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.2]
emidle = [(u, v) for (u, v, d) in G.edges(data=True) if (d['weight'] > 0.1) & (d['weight'] <= 0.2)]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.1]
# 进行图布局
# 网络图的三种布局方式
pos = nx.spring_layout(G)
# pos=nx.circular_layout(G)
# pos=nx.random_layout(G)
# 计算中心度
Gdegree = nx.degree(G)
Gdegree = dict(Gdegree)
Gdegree = pd.DataFrame({'name': list(Gdegree.keys()), 'degree': list(Gdegree.values())})
# node
# nx.draw_networkx_nodes(G, pos, alpha=0.6, node_size=800)  # 指定结点大小
# 依据出度和入度进行节点大小的设置
nx.draw_networkx_nodes(G, pos, alpha=0.6, node_size=Gdegree.degree * 100)
# edge
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=0.5, alpha=0.6, edge_color='r')
nx.draw_networkx_edges(G, pos, edgelist=emidle, width=0.3, alpha=0.5, edge_color='b')
nx.draw_networkx_edges(G, pos, edgelist=esmall, width=0.1, alpha=0.1, edge_color='y', style='dashed')
# label
nx.draw_networkx_labels(G, pos, font_size=10)
plt.axis('off')
plt.title('红楼梦社交网络')
plt.show()
