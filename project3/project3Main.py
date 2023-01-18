import requests
from bs4 import BeautifulSoup
from urllib import parse

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}

def get_url(url):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        return ""

def get_html(html):
    soup = BeautifulSoup(html,'lxml')
    trs = soup.select('table tbody tr')
    print("outside")
    for tr in trs:
        print("inside")
        title = tr.select_one('td a').text
        link = tr.select_one('td a')['href']
        link = parse.urljoin('https://s.weibo.com/',link)
        print(title,link)

if __name__ == '__main__':
    url = 'https://s.weibo.com/top/summary?cate=realtimehot'
    url2 = 'https://s.weibo.com/top/summary?cate=socialevent'
    html = get_url(url)
    print(html)
    # get_html(html)
    html2 = get_url(url2)
    print(html2)
    # get_html(html2)
