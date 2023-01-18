import requests

cookies = {
    '_ga': 'GA1.3.142453730.1669462354',
    'JSESSIONID': 'aaa6qdkfg-Tf6cIzEWzwy',
    'selectionBar': '1443372',
}

headers = {
    'Host': 'zhjw.scu.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'http://zhjw.scu.edu.cn',
    'Referer': 'http://zhjw.scu.edu.cn/student/teachingResources/freeClassroom/today',
}

data = {
    'dayplus': '0',
}


response = requests.post(
    'http://zhjw.scu.edu.cn/student/teachingResources/freeClassroom/today/1,2,3',
    cookies=cookies,
    headers=headers,
    data=data,
)

afTomrrowDateUrl = "http://zhjw.scu.edu.cn/student/teachingResources/freeClassroomQuery/afTomrrowDate"
tomrrowDateUrl = "http://zhjw.scu.edu.cn/student/teachingResources/freeClassroomQuery/tomrrowDate"
todayUrl = "http://zhjw.scu.edu.cn/student/teachingResources/freeClassroom/today"

print(response.text)

# curl -H "Host: zhjw.scu.edu.cn" -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0" -H "Accept: application/json, text/javascript, */*; q=0.01" -H "Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2" -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "X-Requested-With: XMLHttpRequest" -H "Origin: http://zhjw.scu.edu.cn" -H "Referer: http://zhjw.scu.edu.cn/student/teachingResources/freeClassroom/today" -H "Cookie: _ga=GA1.3.142453730.1669462354; JSESSIONID=aaa7-5RGWcnK96HHEWzwy; selectionBar=1443372" --data-binary "&xqh=03" --compressed "http://zhjw.scu.edu.cn/student/teachingResources/freeClassroom/queryCodeTeaBuildingList"
