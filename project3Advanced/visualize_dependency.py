import os
import re
import json
import time
import random
import requests
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup


session = requests.session()

fileDir = os.path.dirname(os.path.abspath(__file__))

github_raw_url = "https://raw.githubusercontent.com"
github_root_url = "https://github.com"
http_head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33"
}


def get_dependency_data() -> int:
    # 粗略获取项目依赖（只爬取根目录下的requirements.txt）
    dependency = {}
    for repo in open(f"{fileDir}/data/python_repository_list.txt"):
        time.sleep(random.random())
        repo = repo.strip()
        dependency[repo] = []
        print("working on ->", repo)
        href = github_raw_url + repo + "/master/requirements.txt"
        try:
            requirements = session.get(href, headers=http_head)
        except requests.exceptions.ConnectionError:
            print("Internet ConnectionError.")
            return -2
        if requirements.status_code != 200:
            print("failed! status_code isn't 200.")
            return -1
        for line in requirements.content.decode("utf-8", "ignore").split('\n'):
            line = line.strip().replace("\x00", "")
            if line == "" or (not 'a' <= line[0] <= 'z'):
                continue
            for op in ["#", ";", "<=", ">=", ">", "<", "==", "~=", "!=", '[', "@"]:
                pos = line.find(op)
                if pos != -1:
                    line = line[:pos].strip()
            dependency[repo].append(line)

    with open(f'{fileDir}/data/dependency_data.json', 'w', encoding='utf-8') as f:
        json.dump(dependency, f, ensure_ascii=True, indent=4)
    return 0


def get_complete_data() -> int:
    # 获取项目所有的依赖（爬取insight->dependency中的所有数据）
    dependency = {}
    for repo in open(f"{fileDir}/data/python_repository_list.txt"):
        # repo = "/dongguaguaguagua/FlyClubTest"
        repo = repo.strip()
        item_set = set([])
        time.sleep(random.random())
        print("working on ->", repo)
        href = github_root_url + repo + "/network/dependencies"
        while True:
            try:
                requirements = session.get(href, headers=http_head)
            except requests.exceptions.ConnectionError:
                print("Internet ConnectionError.\nRetring...")
                continue
            if requirements.status_code != 200:
                print("failed! status_code isn't 200.")
                return -1
            break
        html_text_all = requirements.text
        soup = BeautifulSoup(requirements.text, "lxml")
        load_more_dependencies = soup.find_all(class_="ajax-pagination-form")
        for button in load_more_dependencies:
            url = github_root_url + button['action'].strip()
            print("GET", url)
            http_more = session.get(url, headers=http_head)
            html_text_all += http_more.text
        save = False
        for item in re.findall(r"href=\"/[a-zA-Z0-9_-]*/[a-zA-Z0-9_-]*\"", html_text_all):
            item = item[6:-1]
            if save and item != repo:
                item_set.add(item)
                continue
            if item == repo:
                save = True
        dependency[repo] = list(item_set)

    with open(f'{fileDir}/data/complete_dependency_data.json', 'w', encoding='utf-8') as f:
        json.dump(dependency, f, ensure_ascii=True, indent=4)
    return 0


def draw_dependency_map(rank=100) -> None:
    # 绘制依赖关系图
    csv = pd.read_csv(f"{fileDir}/data/python_repository_list.csv", encoding="utf8")
    star_list = list(csv['星标数(star)'][:rank])
    repo_name = list(csv['名称'][:rank])
    G = nx.MultiDiGraph()  # 有多重边有向图
    edge_list = []

    with open(f"{fileDir}/data/complete_dependency_data.json") as f:
        dependency = json.load(f)
    for key, value in dependency.items():
        if value == []:
            continue
        el = []
        key = key.split('/')[-1]
        for item in value:
            item = item.split('/')[-1]
            if item in repo_name:
                el.append((key, item))
        G.add_edges_from(el)
        edge_list.append(el)
        rank -= 1
        if rank == 0:
            break
    # 用下来arf_layout最清晰
    pos = nx.arf_layout(G)
    # pos = nx.circular_layout(G)
    # pos = nx.random_layout(G)
    # pos = nx.spring_layout(G)

    for index, el in enumerate(edge_list):
        nx.draw_networkx_edges(G, pos, edgelist=el, width=star_list[index] / 100000, alpha=0.5, edge_color='b')
    nx.draw_networkx_nodes(G, pos, alpha=0.5, node_size=100, edgecolors="b", node_color="w", linewidths=0.5)
    nx.draw_networkx_labels(G, pos, font_size=5, font_color="r", font_family=["Fira Code"], font_weight="bold")
    plt.title(f'Github Python Topic top{index + 1}')
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    # get_dependency_data()
    # get_complete_data()
    draw_dependency_map(rank=300)
