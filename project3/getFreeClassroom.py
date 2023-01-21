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

ocr = DdddOcr(show_ad = False)
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

# -4 未知错误
# -3 未填写config
# -2 网络错误
# -1 token校验失败 或 验证码不正确
# 0  程序正常运行
# 1  账号或密码错误
def login() -> int:
    if userConfig["username"] == "" or userConfig["password"] == "":
        console.log("[b]WARNING:[/b] Please fill the userConfig.json.", style="yellow")
        return -3
    try:
        http_page = session.get(loginUrl)
        console.log(f"[u]登录页获取[/u] > 状态码", http_page.status_code)
        if http_page.status_code != 200:
            console.log("[b]ERROR![/b] status_code isn't 200.", style="red")
            return -2
        console.log("[OK]", justify="right", style="green")

        tokenValue = http_page.text.find("tokenValue")
        console.log(f"[u]随机码获取[/u] >", tokenValue)
        if tokenValue <= 0:
            console.log("[b]ERROR![/b] failed to get token.", style="red")
            return -2
        tokenValue = http_page.text[tokenValue + 37:tokenValue + 69]
        console.log("[OK]", justify="right", style="green")

        http_captcha = session.get(captchaImgUrl)
        console.log(f"[u]验证码获取[/u] > 状态码", http_captcha.status_code)
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
    console.log(f"[u]验证码提交[/u] > 状态码", http_post.status_code)
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

    return -4

def get_content(i, d, campusName):
    """Extract text from dict."""
    number = d["id"]["teachingBuildingNumber"]
    name = d["teachingBuildingName"]
    return f"[u]{i}.[/u][b] {name}[/b]\n[[cyan]{campusName}[/][yellow]{number}[/]]"

def printTimeTable(campusIndex) -> int:
    if not campusIndex in [1,2,3]:
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
    if campusIndex == 1 or campusIndex == 2:
        table.add_row("[green u]1[/]","[blue]第01节课[/]","[yellow]08:00[/]-[yellow]08:45[/]")
        table.add_row("[green u]2[/]","[blue]第02节课[/]","[yellow]08:55[/]-[yellow]09:40[/]")
        table.add_row("[green u]3[/]","[blue]第03节课[/]","[yellow]10:00[/]-[yellow]10:45[/]")
        table.add_row("[green u]4[/]","[blue]第04节课[/]","[yellow]10:55[/]-[yellow]11:40[/]")
        table.add_row("","","")
        table.add_row("[green u]5[/]","[blue]第05节课[/]","[yellow]14:00[/]-[yellow]14:45[/]")
        table.add_row("[green u]6[/]","[blue]第06节课[/]","[yellow]14:55[/]-[yellow]15:40[/]")
        table.add_row("[green u]7[/]","[blue]第07节课[/]","[yellow]15:50[/]-[yellow]16:35[/]")
        table.add_row("[green u]8[/]","[blue]第08节课[/]","[yellow]16:55[/]-[yellow]17:40[/]")
        table.add_row("[green u]9[/]","[blue]第09节课[/]","[yellow]17:50[/]-[yellow]18:35[/]")
        table.add_row("","","")
        table.add_row("[green u]10[/]","[blue]第10节课[/]","[yellow]19:30[/]-[yellow]20:15[/]")
        table.add_row("[green u]11[/]","[blue]第11节课[/]","[yellow]20:25[/]-[yellow]21:10[/]")
        table.add_row("[green u]12[/]","[blue]第12节课[/]","[yellow]21:20[/]-[yellow]22:05[/]")
    elif campusIndex == 3:
        table.add_row("[green u]1[/]","[blue]第01节课[/]","[yellow]08:15[/]-[yellow]09:00[/]")
        table.add_row("[green u]2[/]","[blue]第02节课[/]","[yellow]09:10[/]-[yellow]09:55[/]")
        table.add_row("[green u]3[/]","[blue]第03节课[/]","[yellow]10:15[/]-[yellow]11:00[/]")
        table.add_row("[green u]4[/]","[blue]第04节课[/]","[yellow]11:10[/]-[yellow]11:55[/]")
        table.add_row("","","")
        table.add_row("[green u]5[/]","[blue]第05节课[/]","[yellow]13:50[/]-[yellow]14:35[/]")
        table.add_row("[green u]6[/]","[blue]第06节课[/]","[yellow]14:45[/]-[yellow]15:30[/]")
        table.add_row("[green u]7[/]","[blue]第07节课[/]","[yellow]15:40[/]-[yellow]16:25[/]")
        table.add_row("[green u]8[/]","[blue]第08节课[/]","[yellow]16:45[/]-[yellow]17:30[/]")
        table.add_row("[green u]9[/]","[blue]第09节课[/]","[yellow]17:40[/]-[yellow]18:25[/]")
        table.add_row("","","")
        table.add_row("[green u]10[/]","[blue]第10节课[/]","[yellow]19:20[/]-[yellow]20:05[/]")
        table.add_row("[green u]11[/]","[blue]第11节课[/]","[yellow]20:15[/]-[yellow]21:00[/]")
        table.add_row("[green u]12[/]","[blue]第12节课[/]","[yellow]21:10[/]-[yellow]21:55[/]")
    console.print(Panel.fit(
            table,
            padding=(1, 2),
            title="[bold white]{}校区教学时间表".format(campusList[campusIndex - 1]),
            border_style="bright_green"
        ), justify= "center"
    )
    return 0

def searchFreeClassroom() -> int:
    message = Table.grid()
    message.add_column()
    message.add_column()
    message.add_column()
    message.add_row(
        Panel("[u]1.[/u] [cyan]望江"),
        Panel("[u]2.[/u] [cyan]华西"),
        Panel("[u]3.[/u] [cyan]江安")
    )
    console.print(
        Panel.fit(
            message,
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
                    console.log("[b]WARNING[/b]: 请输入1,2,3中的一个数。",style="yellow")
            except:
                console.log("[b]WARNING[/b]: 请输入一个正整数。",style="yellow")
    else:
        console.print(f"使用 [u i]userConfig.json[/] 中的值:", userConfig["campus"])
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
        console.log(f"使用 [u i]userConfig.json[/] 中的值:", ' '.join(buildingList))
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
        console.log(f"[u]今日教室获取[/u] > 状态码", http_response.status_code)
        if http_response.status_code != 200:
            console.log("[b]ERROR![/b] status_code isn't 200.", style="red")
            return -2
        console.log("[OK]", justify="right", style="green")

        http_response = session.post(todayUrl + ','.join(timeList), data={"dayplus": "0"})
        console.log(f"[u]空闲教室获取[/u] > 状态码", http_response.status_code)
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


