import os
import json
import time
import requests
import random

session = requests.session()

fileDir = os.path.dirname(os.path.abspath(__file__))

github_raw_url = "https://raw.githubusercontent.com"

http_head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33"
}

index = 1

dependency = {}
for repo in open(f"{fileDir}/data/python_repository_list.txt"):
    time.sleep(random.random())
    repo = repo.strip()
    dependency[repo] = []
    print("working on ->", repo)
    href = github_raw_url + repo + "/master/requirements.txt"
    requirements = session.get(href, headers=http_head)
    if requirements.status_code == 200:
        for line in requirements.content.decode("utf-8", "ignore").split('\n'):
            line = line.strip().replace("\x00", "")
            if line == "" or (not 'a' <= line[0] <= 'z'):
                continue
            for op in ["#", ";", "<=", ">=", ">", "<", "==", "~=", "!=", '[', "@"]:
                pos = line.find(op)
                if pos != -1:
                    line = line[:pos].strip()
            dependency[repo].append(line)
    else:
        print("failed! status_code isn't 200.")

# print(dependency)

with open('dependency_data.json', 'w', encoding='utf-8') as f:
    json.dump(dependency, f, ensure_ascii=True, indent=4)
