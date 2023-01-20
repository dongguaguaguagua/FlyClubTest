import os
import json
import hashlib
import requests

# 带带弟弟 OCR
from ddddocr import DdddOcr

# 用rich输出
from rich.console import Console
from rich.columns import Columns
from rich.table import Column, Table
from rich.panel import Panel

# ------ init -------
console = Console()
console.log("正在初始化……")

ocr = DdddOcr(show_ad = False)
session = requests.session()

httpHead = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33"}
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
console.log("[green][OK]", justify="right")
# load config
with open(f"{fileDir}/userConfig.json") as f:
    userConfig = json.load(f)
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
        if http_page.status_code != 200:
            console.log("[b]ERROR![/b] status_code isn't 200.", style="red")
            return -2
        console.log(f"[u]登录页获取[/u] > 状态码[cyan]{http_page.status_code}[/cyan]")
        console.log("[green][OK]", justify="right")

        tokenValue = http_page.text.find("tokenValue")
        if tokenValue <= 0:
            console.log("[b]ERROR![/b] failed to get token.", style="red")
            return -2
        tokenValue = http_page.text[tokenValue + 37:tokenValue + 69]
        console.log(f"[u]随机码获取[/u] > [cyan]{tokenValue}[/cyan]")
        console.log("[green][OK]", justify="right")

        http_captcha = session.get(captchaImgUrl)
        if http_page.status_code != 200:
            console.log("[b]ERROR![/b] status_code isn't 200.", style="red")
            return -2
        console.log(f"[u]验证码获取[/u] > 状态码[cyan]{http_captcha.status_code}[/cyan]")
        console.log("[green][OK]", justify="right")
    except requests.exceptions.ConnectionError:
        console.log("[b]ERROR![/b] Internet Connection broken.", style="red")
        return -2
    with open(f"{fileDir}/images/captcha.jpg", "wb") as f:
        f.write(http_captcha.content)
        f.close()
    captchaResult = ocr.classification(http_captcha.content)
    console.log(f"[u]验证码识别[/u] > [cyan]{captchaResult}")
    console.log("[green][OK]", justify="right")
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
    console.log(f"[u]验证码提交[/u] > 状态码[cyan]{http_post.status_code}")
    console.log("[green][OK]", justify="right")
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
    return f"[u]{i}.[/u][b] {name}[/b]\n[[cyan]{campusName}[/cyan][yellow]{number}[/yellow]]"

def getTimeTable(campusIndex) -> Table:
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
        table.title = "{}校区教学时间表".format(campusList[campusIndex - 1])
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
        table.title = "江安校区教学时间表"
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
    return table

def searchFreeClassroom():
    console.print("[bold]您想要查询哪个校区的空闲教室？", justify="center")

    renderables = [Panel(f"[u]{i + 1}.[/u] [cyan]{name}", expand=True) for i, name in enumerate(campusList)]
    console.print(Columns(renderables))

    while True:
        try:
            console.print("[dim]>>>[/] 请输入编号: ", end="")
            campusIndex = int(input())
            if 1 <= campusIndex <= 3:
                break
            else:
                console.log("[b]WARNING[/b]: 请输入1,2,3中的一个数。",style="yellow")
        except:
            console.log("[b]WARNING[/b]: 请输入一个正整数。",style="yellow")

    # open the downloaded building list
    with open(f"{fileDir}/queryCodeTeaBuildingList.json") as f:
        d = json.load(f)

    buildingList = d[campusIndex - 1]

    renderables = [Panel(get_content(i, d, campusList[campusIndex - 1]),
                    expand=False) for i, d in enumerate(buildingList)]
    console.print(Columns(renderables))

    if userConfig["buildings"] == []:
        console.print("[dim]>>>[/] ([magenta]用空格分割[/magenta]) 请选择想要查询的教学楼编号: ", end="")
        buildingList = input().split(" ")
    else:
        buildingList = userConfig["buildings"]
        console.print(f"使用 [u i]userConfig.json[/u i] 中的值: [cyan]{' '.join(buildingList)}")
    if userConfig["rememberBuildings"]:
        userConfig["buildings"] = buildingList
    else:
        userConfig["buildings"] = []
    with open(f"{fileDir}/userConfig.json", 'w', encoding='utf-8') as f:
        json.dump(userConfig, f, ensure_ascii=False, indent=4)
        console.log(f"已将[cyan]'buildings': [{','.join(buildingList)}][/cyan]存入 [u i]userConfig.json")

    console.print(getTimeTable(campusIndex))
    console.print("[dim]>>>[/] ([magenta]用空格分割[/magenta]) 选择想要查询的时间段: ", end="")
    timeList = input().split(" ")

    http_response = session.get(todayUrl + ','.join(timeList))
    jsonList = json.loads(http_response.text)
    spareroomList = jsonList["spareroomObjList"]

    table = Table(show_edge=True, show_header=True, expand=False)
    table.title = jsonList["curxqm"] + "空闲教室一览表"
    table.add_column("[green]教学楼[/]", no_wrap=False, justify="center", style="bold")
    table.add_column("[green]教室名+容纳人数[/]", no_wrap=False, justify="center", style="bold")
    for obj in spareroomList:
        renderables = []
        for classroom in obj["claroom"]:
            renderables.append(Panel(f"[white bold]{classroom['classroom']}[/]\n[cyan]{classroom['classNumberOfSeats']}[/]", expand=False, border_style="bright_green",))
        table.add_row(f"[yellow]{obj['acmcBuilding']}[/] {obj['acmcBuildingName']}", Columns(renderables))

    console.print(table)

# # get the list through requests
# # ----- begin -----

# print("获取教学楼列表中，请稍后……")

# data = "&xqh=0{}".format(campusIndex)

# responses = requests.post(
#     buildingListUrl,
#     cookies=cookies,
#     headers=headers,
#     data=data,
# )

# print("完成")

# try:
#     buildingList = json.loads(responses.text)
#     for i in buildingList:
#         print(i["teachingBuildingName"])
# except:
#     print("cookies已过期！请重新登录")

# # ------ end ------

if __name__ == '__main__':
    if login() == 0:
        searchFreeClassroom()


