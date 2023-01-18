from nonebot.adapters.onebot.v11 import Bot, Event, MessageSegment, Message
from nonebot import get_driver
from nonebot import on_command
from .config import Config
# import json

global_config = get_driver().config
config = Config.parse_obj(global_config)


catch_json_str = on_command("json", aliases={"json", "JSON", "Json"})
catch_xml_str = on_command("xml", aliases={"xml", "XML", "Xml"})
catch_cardimg_str = on_command("cardimg", aliases={"ci", "cardimage", "CardImage"})


@catch_xml_str.handle()
async def send_xml_msg(bot: Bot, event: Event):
    # prompt = args.extract_plain_text()
    # print(prompt)
    data = """
<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><msg serviceID="107" templateID="14" action="web" actionData="" brief="QQ群798700487" sourcePublicUin="3043786528" sourceMsgId="1495460701626432" url="https://post.mp.qq.com/" flag="0" adverSign="0" multiMsgFlag="0"><item layout="1"><vote cover="http://shp.qpic.cn/collector/2387068393/4b99b0db-6442-4f0c-8112-2d5384ee72a3/0" /></item><item layout="0"><hr hidden="false" style="0" /></item><source name="" icon="" action="" appid="0" /></msg>
"""
    msg = Message(f"[CQ:xml,data={data}]")
    await catch_xml_str.send(msg)
    await catch_xml_str.finish()


@catch_json_str.handle()
async def send_json_msg(bot: Bot, event: Event):
    # &#44;"view":"notification"&#44;"ver":"0.0.0.1"&#44;"prompt":"&#91;应用&#93;"&#44;"appID":""&#44;"sourceName":""&#44;"actionData":""&#44;"actionData_A":""&#44;"sourceUrl":""&#44;"meta":{"notification":{"appInfo":{"appName":"全国疫情数据统计"&#44;"appType":4&#44;"appid":1109659848&#44;"iconUrl":"http:\/\/gchat.qpic.cn\/gchatpic_new\/719328335\/-2010394141-6383A777BEB79B70B31CE250142D740F\/0"}&#44;"data":&#91;{"title":"确诊"&#44;"value":"80932"}&#44;{"title":"今日确诊"&#44;"value":"28"}&#44;{"title":"疑似"&#44;"value":"72"}&#44;{"title":"今日疑似"&#44;"value":"5"}&#44;{"title":"治愈"&#44;"value":"60197"}&#44;{"title":"今日治愈"&#44;"value":"1513"}&#44;{"title":"死亡"&#44;"value":"3140"}&#44;{"title":"今亡"&#44;"value":"17"}&#93;&#44;"title":"中国加油, 武汉加油"&#44;"button":&#91;{"name":"病毒 : SARS-CoV-2, 其导致疾病命名 COVID-19"&#44;"action":""}&#44;{"name":"传染源 : 新冠肺炎的患者。无症状感染者也可能成为传染源。"&#44;"action":""}&#93;&#44;"emphasis_keyword":""}}&#44;"text":""&#44;"sourceAd":""
    data = r"""
{"app": "com.tencent.miniapp"&#44;"desc": ""&#44;"view": "notification"&#44;"ver": "0.0.0.1"&#44;"prompt": "&#91;应用&#93;"&#44;"appID": ""&#44;"sourceName": ""&#44;"actionData": ""&#44;"actionData_A": ""&#44;"sourceUrl": ""&#44;"meta": &#123;&#125;}
""".strip()
    data2 = r"""
{"app":"com.tencent.structmsg","desc":"新闻","view":"news","ver":"0.0.0.1","prompt":"[分享]群精华消息","appID":"","sourceName":"","actionData":"","actionData_A":"","sourceUrl":"","meta":{"news":{"action":"","android_pkg_name":"","app_type":1,"appid":101890901,"ctime":1671203396,"desc":"\/PIKACHUIM\/UrpHelps","jumpUrl":"https:\/\/qun.qq.com\/essence\/share?_wv=3&_wwv=128&_wvx=2&sharekey=bffe0f3f57d75915c279d8a81e746577ab39c903","preview":"https:\/\/pub.idqqimg.com\/pc\/misc\/files\/20191015\/32ed5b691a1138ac452a59e42f3f83b5.png","source_icon":"http:\/\/i.gtimg.cn\/open\/app_icon\/00\/68\/68\/48\/\/100686848_100_m.png","source_url":"","tag":"群精华消息","title":"群精华消息","uin":2694536263}},"config":{"ctime":1671203396,"forward":false,"token":"26593b46bb0b0e1310cc99d600cac4b3","type":"normal"},"text":"","sourceAd":"","extra":"{\"app_type\":1,\"appid\":101890901,\"uin\":2694536263}"}
""".strip().replace(",", "&#44;").replace("&", "&amp;").replace("[", "&#91;").replace("]", "&#93;")
    print(data)
    await catch_json_str.send(Message(f"[CQ:json,data={data}]"))
    # print(data2)
    # await catch_json_str.send(Message(f"[CQ:json,data={data2}]"))
    await catch_json_str.finish()


@catch_cardimg_str.handle()
async def send_cardimg_msg(bot: Bot, event: Event):
    cardimgContent = r"""
[CQ:cardimage,file=http://gchat.qpic.cn/gchatpic_new/1169088181/4177879595-3121117498-74EB28C523F12CE933EEF3BCF50D4ED1/0]
""".strip()
    print(cardimgContent)
    await catch_xml_str.send(MessageSegment.image(file="http://gchat.qpic.cn/gchatpic_new/1169088181/4177879595-3121117498-74EB28C523F12CE933EEF3BCF50D4ED1/0"))
    await catch_cardimg_str.finish(Message(cardimgContent))


# from nonebot import on_command
# from nonebot.rule import to_me
# from nonebot.matcher import Matcher
# from nonebot.adapters import Message
# from nonebot.params import Arg, CommandArg, ArgPlainText

# weather = on_command("weather", rule=to_me(), aliases={"天气", "天气预报"}, priority=5)


# @weather.handle()
# async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
#     plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
#     print(plain_text)
#     if plain_text:
#         matcher.set_arg("city", args)  # 如果用户发送了参数则直接赋值


# @weather.got("city", prompt="你想查询哪个城市的天气呢？")
# async def handle_city(city: Message = Arg(), city_name: str = ArgPlainText("city")):
#     if city_name not in ["北京", "上海"]:  # 如果参数不    符合要求，则提示用户重新输入
#         # 可以使用平台的 Message 类直接构造模板消息
#         await weather.reject(city.template("你想查询的城市 {city} 暂不支持，请重新输入！"))

#     city_weather = await get_weather(city_name)
#     await weather.finish(city_weather)


# # 在这里编写获取天气信息的函数
# async def get_weather(city: str) -> str:
#     return f"{city}的天气是..."
