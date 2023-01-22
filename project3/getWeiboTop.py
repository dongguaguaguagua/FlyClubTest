from datetime import datetime
import requests
from bs4 import BeautifulSoup

url = "https://s.weibo.com/top/summary"

cookies = {
    'SUB': '_2AkMUmx2wf8NxqwJRmP0RzGzjZYpzwwjEieKix-xrJRMxHRl-yj9kqkdetRB6PxszX2D20nHm0oIeT2ilDeAjHyr_GotC',
    'SUBP': '0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhrWh6ZI_H2ib563Yk-j-zm',
    'SINAGLOBAL': '7587231095983.274.1662561748038',
    'ULV': '1674023512048:3:1:1:6332481451455.533.1674023511966:1663576357807',
    'UOR': ',,www.baidu.com',
    '_s_tentry': '-',
    'Apache': '6332481451455.533.1674023511966',
}

headers = {
    'Host': 's.weibo.com',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'upgrade-insecure-requests': '1',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
}

response = requests.get(url, cookies=cookies, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
all_tds = soup.find_all('td')
#  This should be as simple as:

with open(f"微博热搜榜{str(datetime.today())}.csv", 'a') as csv_file:
    csv_file.write("排名,热搜名称,链接\n")
    i = 1
    for td in all_tds:
        if "td-02" in td.get("class") and td.a.get("href") != "javascript:void(0);":
            text = td.a.get_text()
            href = "https://s.weibo.com" + td.a.get("href")
            result = "- [{}]({})".format(text, href)
            csv_file.write(f"{i},{text},{href}\n")
            print(result)
            i += 1
