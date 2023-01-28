import os
import json
import hashlib
import sys
import requests

# 带带弟弟 OCR
from ddddocr import DdddOcr

# 用rich输出
from rich.console import Console
from rich.columns import Columns
from rich.table import Table
from rich.panel import Panel

# ------ init -------
console = Console()
console.log("正在初始化……")

ocr = DdddOcr(show_ad=False, old=True)
session = requests.session()

httpHead = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33",
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'http://zhjw.scu.edu.cn',
    'Connection': 'keep-alive',
}
loginUrl = "http://zhjw.scu.edu.cn/login"
loginCheckUrl = "http://zhjw.scu.edu.cn/j_spring_security_check"
captchaImgUrl = "http://zhjw.scu.edu.cn/img/captcha.jpg"
afTomrrowDateUrl = "http://zhjw.scu.edu.cn/student/teachingResources/freeClassroomQuery/afTomrrowDate/"
tomrrowDateUrl = "http://zhjw.scu.edu.cn/student/teachingResources/freeClassroomQuery/tomrrowDate/"
todayUrl = "http://zhjw.scu.edu.cn/student/teachingResources/freeClassroom/today/"
buildingListUrl = "http://zhjw.scu.edu.cn/student/teachingResources/freeClassroom/queryCodeTeaBuildingList"

# 3个校区
campusList = ["望江", "华西", "江安"]

# getFreeClassroom.py 所在的目录
# 即 project3 的绝对路径
fileDir = os.path.dirname(os.path.abspath(__file__))

# 加载 userConfig.json 默认值为：
# {"username": "", "password": "", "campus": 0, "buildings": [], "rememberBuildings": true }
try:
    with open(f"{fileDir}/userConfig.json") as f:
        userConfig = json.load(f)
except json.decoder.JSONDecodeError:
    console.log("[b]ERROR![/b] Invalid userConfig file!", style="red")
    sys.exit(1)

console.log("[OK]", justify="right", style="green")
# ----- init end --------


def login() -> int:
    # -4 未知错误
    # -3 未填写config
    # -2 网络错误
    # -1 token校验失败 或 验证码不正确
    # 0  程序正常运行
    # 1  账号或密码错误
    if userConfig["username"] == "" or userConfig["password"] == "":
        console.log("[b]WARNING:[/b] Please fill the userConfig.json.", style="yellow")
        return -3
    try:
        http_page = session.get(loginUrl)
        console.log("[u]登录页获取[/u] > 状态码", http_page.status_code)
        if http_page.status_code != 200:
            console.log("[b]ERROR![/b] status_code isn't 200.", style="red")
            return -2
        console.log("[OK]", justify="right", style="green")

        tokenValue = http_page.text.find("tokenValue")
        console.log("[u]随机码获取[/u] >", tokenValue)
        if tokenValue <= 0:
            console.log("[b]ERROR![/b] failed to get token.", style="red")
            return -2
        tokenValue = http_page.text[tokenValue + 37:tokenValue + 69]
        console.log("[OK]", justify="right", style="green")

        http_captcha = session.get(captchaImgUrl)
        console.log("[u]验证码获取[/u] > 状态码", http_captcha.status_code)
        if http_page.status_code != 200:
            console.log("[b]ERROR![/b] status_code isn't 200.", style="red")
            return -2
        console.log("[OK]", justify="right", style="green")
    except requests.exceptions.ConnectionError:
        console.log("[b]ERROR![/b] Internet Connection broken.", style="red")
        return -2
    # with open(f"{fileDir}/images/captcha.jpg", "wb") as f:
    #     f.write(http_captcha.content)
    #     f.close()
    captchaResult = ocr.classification(http_captcha.content)
    console.log(f"[u]验证码识别[/u] > [cyan]{captchaResult}")
    console.log("[OK]", justify="right", style="green")
    httpHash = hashlib.md5(userConfig["password"].encode()).hexdigest()
    postData = {
        "tokenValue": tokenValue,
        "j_username": userConfig["username"],
        "j_password": httpHash,
        "j_captcha": captchaResult
    }
    try:
        http_post = session.post(loginCheckUrl, postData, httpHead)
    except requests.exceptions.ConnectionError:
        console.log("[b]ERROR![/b] Internet Connection broken.", style="red")
        return -2
    console.log("[u]验证码提交[/u] > 状态码", http_post.status_code)
    console.log("[OK]", justify="right", style="green")
    if http_post.text.find('验证码错误') != -1:
        console.log("[u]登录未成功[/u]：验证码不正确", style="red")
        # TODO: 重新获取验证码
        return -1
    elif http_post.text.find('token校验失败') != -1:
        console.log("[u]登录未成功[/u]：token校验失败", style="red")
        return -1
    elif http_post.text.find('用户密码错误') != -1:
        console.log("[u]登录未成功[/u]：账号或密码错误", style="red")
        return 1

    if http_post.text.find('的培养方案') != -1:
        console.log("[u]已成功登录[/u]：成功登录系统", style="green")
        return 0

    console.log("[u]未知错误[/u]，程序退出", style="red")
    console.log(http_post.text)
    return -4


def get_content(i, d, campusName):
    """Extract text from dict."""
    number = d["id"]["teachingBuildingNumber"]
    name = d["teachingBuildingName"]
    return f"[u]{i}.[/u][b] {name}[/b]\n[[cyan]{campusName}[/][yellow]{number}[/]]"


def printTimeTable(campusIndex) -> int:
    if campusIndex not in [1, 2, 3]:
        console.log("[b]ERROR![/b] Fail to print time table: Unknown Campus.", style="red")
        return 1
    table = Table(
        show_edge=False,
        show_header=True,
        expand=False,
        row_styles=["none", "dim"],
    )
    table.add_column("编号", justify="center", style="bold")
    table.add_column("课程", justify="center", style="bold")
    table.add_column("时间", justify="center", style="bold")
    row1 = ["1", "2", "3", "4", "", "5", "6", "7", "8", "9", "", "10", "11", "12"]
    row2 = ["第01节课", "第02节课", "第03节课", "第04节课", "", "第05节课", "第06节课", "第07节课", "第08节课", "第09节课", "", "第10节课", "第11节课", "第12节课"]
    row3 = [
        ["08:00-08:45", "08:55-09:40", "10:00-10:45", "10:55-11:40", "", "14:00-14:45", "14:55-15:40", "15:50-16:35", "16:55-17:40", "17:50-18:35", "", "19:30-20:15", "20:25-21:10", "21:20-22:05"],
        ["08:00-08:45", "08:55-09:40", "10:00-10:45", "10:55-11:40", "", "14:00-14:45", "14:55-15:40", "15:50-16:35", "16:55-17:40", "17:50-18:35", "", "19:30-20:15", "20:25-21:10", "21:20-22:05"],
        ["08:15-09:00", "09:10-09:55", "10:15-11:00", "11:10-11:55", "", "13:50-14:35", "14:45-15:30", "15:40-16:25", "16:45-17:30", "17:40-18:25", "", "19:20-20:05", "20:15-21:00", "21:10-21:55"]
    ]
    for i in range(14):
        table.add_row(f"[green u]{row1[i]}[/]", f"[blue]{row2[i]}[/]", f"[yellow]{row3[campusIndex - 1][i]}[/]")
    console.print(
        Panel.fit(
            table,
            padding=(1, 2),
            title="[bold white]{}校区教学时间表".format(campusList[campusIndex - 1]),
            border_style="bright_green"
        ),
        justify="center"
    )
    return 0


def searchFreeClassroom() -> int:
    campusMessage = Table.grid(padding=1, collapse_padding=True)
    campusMessage.pad_edge = False
    introduceMsg = [
        "[dim]四川大学 望江校区 为川大 校本部, 占地 3000 多亩, 主要为 四川大学 大三,大四 及硕博士 研究生同学 学习的地方, 望江校区 位于成都市 一环路上, 分设 东西南北 四个门, 交通方便, 地理位置优越.",
        "[dim]四川大学 华西校区 座落在 成都人民南路 三段17号, 是最早被列入国家 211工程 的 四所 综合性 重点 医科大学 之一.",
        "[dim]四川大学 江安校区 为川大的 本科教育 基地, 主要为 四川大学 大一,大二 同学 学习的地方, 校区总占地 3000亩, 另有教师住宅区 240余亩.校区地处 成都市 双流航空港 经济开发区."
    ]
    campusMessage.add_row(
        Panel(introduceMsg[0], padding=(1, 2), title="[u]1.[/u] [b]望江校区[/]"),
        Panel(introduceMsg[1], padding=(1, 2), title="[u]2.[/u] [b]华西校区[/]"),
        Panel(introduceMsg[2], padding=(1, 2), title="[u]3.[/u] [b]江安校区[/]"),
    )
    console.print(
        Panel.fit(
            campusMessage,
            padding=(1, 2),
            title="[bold white]您想要查询哪个校区的空闲教室？",
            border_style="bright_blue",
        ),
        justify="center",
    )

    if userConfig["campus"] == 0:
        while True:
            try:
                console.print("[dim]>>>[/] 请输入编号: ", end="")
                campusIndex = int(input())
                if 1 <= campusIndex <= 3:
                    userConfig["campus"] = campusIndex
                    break
                else:
                    console.log("[b]WARNING[/b]: 请输入1,2,3中的一个数。", style="yellow")
            except ValueError:
                console.log("[b]WARNING[/b]: 请输入一个正整数。", style="yellow")
    else:
        console.print("使用 [u i]userConfig.json[/] 中的值:", userConfig["campus"])
        campusIndex = userConfig["campus"]

    # open the downloaded building list
    with open(f"{fileDir}/queryCodeTeaBuildingList.json") as f:
        d = json.load(f)

    renderables = [Panel(get_content(i, d, campusList[campusIndex - 1]), expand=False)
                   for i, d in enumerate(d[campusIndex - 1])]
    console.print(Columns(renderables), justify="center")

    if userConfig["buildings"] == [] or userConfig["buildings"] == [""]:
        console.print("[dim]>>>[/] ([magenta]用空格分割[/]) 请选择想要查询的教学楼编号: ", end="")
        buildingList = input().split(" ")
    else:
        buildingList = userConfig["buildings"]
        console.log("使用 [u i]userConfig.json[/] 中的值:", ' '.join(buildingList))
    if userConfig["rememberBuildings"]:
        userConfig["buildings"] = buildingList
    else:
        userConfig["buildings"] = []

    with open(f"{fileDir}/userConfig.json", 'w', encoding='utf-8') as f:
        json.dump(userConfig, f, ensure_ascii=False, indent=4)
        console.log(f"已将[cyan]'buildings': [{','.join(buildingList)}][/]存入 [u i]userConfig.json")

    try:
        buildingList = [d[campusIndex - 1][int(i)]["id"]["teachingBuildingNumber"] for i in buildingList]
    except ValueError:
        console.log("[b]WARNING:[/b] 请输入正确的编号。", style="yellow")
        buildingList = [obj["id"]["teachingBuildingNumber"] for obj in d[campusIndex - 1]]
        console.log("[b]WARNING:[/b] 默认为选择所有教学楼。", style="yellow")

    printTimeTable(campusIndex)

    while True:
        console.print("[dim]>>>[/] ([magenta]用空格分割[/]) 选择想要查询的时间段: ", end="")
        timeList = set(input().split(" "))
        try:
            int("".join(timeList))
        except ValueError:
            console.log("[b]WARNING:[/b] 请输入正确的时间段。", style="yellow")
            continue
        break

    try:
        http_response = session.post(todayUrl, data={
            'xqm': campusList[campusIndex-1],
            'position': f"0{campusIndex}_n"
        })
        console.log("[u]今日教室获取[/u] > 状态码", http_response.status_code)
        if http_response.status_code != 200:
            console.log("[b]ERROR![/b] status_code isn't 200.", style="red")
            return -2
        console.log("[OK]", justify="right", style="green")

        http_response = session.post(todayUrl + ','.join(timeList), data={"dayplus": "0"})
        console.log("[u]空闲教室获取[/u] > 状态码", http_response.status_code)
        if http_response.status_code != 200:
            console.log("[b]ERROR![/b] status_code isn't 200.", style="red")
            return -2
        console.log("[OK]", justify="right", style="green")
    except requests.exceptions.ConnectionError:
        console.log("[b]ERROR![/b] Internet Connection broken.", style="red")
        return -2

    try:
        spareroomList = json.loads(http_response.text)["spareroomObjList"]
    except json.decoder.JSONDecodeError:
        console.log("[b]ERROR[/b] 未知错误。", style="red")
        return -4

    table = Table(show_edge=True, show_header=True, expand=False)
    table.title = f"[b]{campusList[campusIndex - 1]}空闲教室一览表"
    table.add_column("[green]教学楼[/]", no_wrap=False, justify="center", style="bold")
    table.add_column("[green]教室名 + 容纳人数[/]", no_wrap=False, justify="center", style="bold")
    # print(buildingList)
    # print(spareroomList)
    for obj in spareroomList:
        if not obj['acmcBuilding'] in buildingList:
            continue
        renderables = []
        for classroom in obj["claroom"]:
            renderables.append(Panel(f"[white bold]{classroom['classroom']}[/]\n[cyan]{classroom['classNumberOfSeats']}[/]",
                                     expand=False, border_style="bright_green",))
        table.add_row(f"[yellow]{obj['acmcBuilding']}[/] {obj['acmcBuildingName']}", Columns(renderables))
    console.print(table)
    return 0


if __name__ == '__main__':
    if login() == 0 and searchFreeClassroom() == 0:
        console.log("搜索完成", style="green")
