import re
import os
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import random

session = requests.session()

github_root_url = "https://github.com"
python_topic_url = "https://github.com/topics/python"
test_url = "https://github.com/donnemartin/system-design-primer"

http_head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33"
}

fileDir = os.path.dirname(os.path.abspath(__file__))


def get_1000_github_repo() -> None:
    # 爬取前1000个python写的repo（按star排序）
    params = {
        'l': 'python',
        's': 'stars',
        'page': 1,
    }
    # 存入python_repository_list便于读取
    with open(f"{fileDir}/data/python_repository_list.txt", "w") as file:
        # 50页·每页20条 => 1000条
        for i in range(1, 51):
            params['page'] = i
            page_response = session.get(python_topic_url, params=params, headers=http_head)
            soup = BeautifulSoup(page_response.text, "lxml")
            all_uls = soup.select(".tabnav-tabs")
            print("working on page", i, "...")
            for ul in all_uls:
                file.write(ul.li.a["href"] + '\n')
                print(ul.li.a["href"])


def get_information(href: str):
    result = []
    href = href.strip()
    # 名称
    result.append(href.split("/")[-1])
    # 地址
    result.append(github_root_url + href)
    try:
        main_page = session.get(github_root_url + href, headers=http_head)
        sleep(random())
        issue_page = session.get(github_root_url + href + '/issues', headers=http_head)
        sleep(random())
        pull_page = session.get(github_root_url + href + '/pulls', headers=http_head)
        sleep(random())
    except Exception as e:
        print("Fail to load", href, "because of Error:", e)
        return result + [""] * 13
    if main_page.status_code != 200:
        print("Fail to load", href, "status_code isn't 200: ", main_page.status_code)
        return result + [""] * 13
    soup = BeautifulSoup(main_page.text, "lxml")
    # 星标数(star)
    selected_stars = soup.select("#repo-stars-counter-unstar") + soup.select("#repo-stars-counter-star")
    numbers_of_stars = selected_stars[0]['title'].replace(",", "")
    result.append(numbers_of_stars)
    # 复刻数(fork)
    selected_forks = soup.select("#repo-network-counter")
    numbers_of_forks = selected_forks[0]['title'].replace(",", "")
    result.append(numbers_of_forks)
    # 简介(About)
    selected_about = soup.select("p.f4:nth-child(2)")
    about_text = "No description or website provided."
    if selected_about != []:
        about_text = selected_about[0].text.strip().replace(",", "")
    result.append(about_text)
    # Readme
    readme_file_name = "No README file found."
    selected_readme = soup.select(".Box-title > a")
    if selected_readme != []:
        readme_file_name = github_root_url + href + "/blob/master/" + selected_readme[0].text.strip()
    result.append(readme_file_name)
    # 主题标(Topic，About 下面)
    selected_topics = soup.select(".topic-tag")
    result.append(" | ".join(topic.text.strip() for topic in selected_topics))
    # Release & Contributors
    selected = soup.select("div.BorderGrid-row > div:nth-child(1) > h2:nth-child(1) > a:nth-child(1)")
    numbers_of_releases = numbers_of_contributors = "0"
    for item_tag in selected:
        # 发布版本数量(Release)
        if "Releases" in item_tag.text:
            if item_tag.span is not None:
                numbers_of_releases = item_tag.span['title'].replace(",", "")
        # 贡献者数量(Contributors)
        elif "Contributors" in item_tag.text:
            if item_tag.span is not None:
                numbers_of_contributors = item_tag.span['title'].replace(",", "")
    result.append(numbers_of_releases)
    result.append(numbers_of_contributors)
    # 语言构成(Languages)
    selected_languages = soup.select("span.Progress:nth-child(1) > span")
    result.append(" | ".join(language['aria-label'] for language in selected_languages))
    # 分支数(Branch)
    selected_branches = soup.select("a.ml-3:nth-child(1) > strong:nth-child(2)")
    numbers_of_branches = selected_branches[0].text.replace(",", "")
    result.append(numbers_of_branches)
    # Issues
    if issue_page.status_code != 200:
        print("Fail to load", href, "status_code isn't 200: ", issue_page.status_code)
        return result + [""] * 4
    soup = BeautifulSoup(issue_page.text, "lxml")
    selected_issues = soup.find('div', class_="flex-auto d-none d-lg-block no-wrap")
    number_list = re.findall(r"\d+\.?\d*", selected_issues.text.replace(",", ""))
    # 开放议题数(Issues open)
    result.append(number_list[0])
    # 关闭议题数(Issues closed)
    result.append(number_list[1])
    # Pull Requests
    if pull_page.status_code != 200:
        print("Fail to load", href, "status_code isn't 200: ", pull_page.status_code)
        return result + [""] * 2
    soup = BeautifulSoup(pull_page.text, "lxml")
    selected_pulls = soup.find('div', class_="flex-auto d-none d-lg-block no-wrap")
    number_list = re.findall(r"\d+\.?\d*", selected_pulls.text.replace(",", ""))
    # 开放拉取请求数(Pull Requests open)
    result.append(number_list[0])
    # 关闭拉取请求数(Pull Requests closed)
    result.append(number_list[1])
    # 依赖的项目(Dependency)
    return result


def save_to_csv():
    index = 1
    with open(f"{fileDir}/data/python_repository_list.csv", "a") as file:
        file.write("序号,名称,地址,星标数(star),复刻数(fork),简介(About),README,主题标(Topic),发布版本数量(Release),贡献者数量(Contributors),语言构成(Languages),分支数(Branch),开放议题数(Issues open),关闭议题数(Issues closed),开放拉取请求数(Pull Requests open),关闭拉取请求数(Pull Requests closed)\n")
        for repo in open(f"{fileDir}/data/python_repository_list.txt"):
            print(index, "-> working on", repo)
            info_list = get_information(repo)
            info_list.insert(0, str(index))
            file.write(",".join(info_list) + "\n")
            index += 1
            print("done")


if __name__ == '__main__':
    # get_1000_github_repo()
    # print("\n".join(get_information("/3b1b/manim")))
    save_to_csv()
