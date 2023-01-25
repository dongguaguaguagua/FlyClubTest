# 项目三

## 版一 抓包获取微博热搜榜

### 安装必要的库

> 本项目需要request beautifulsoup lxml等包。
>
> 可使用如下命令安装

```bash
git clone https://github.com/dongguaguaguagua/flyClubTest.git
cd flyClubTest/project3
pip install -r requirements.txt
```

> **强烈建议使用python虚拟环境**，步骤如下：

```bash
git clone https://github.com/dongguaguaguagua/flyClubTest.git
cd flyClubTest
python -m venv project3
cd project3
source ./bin/activate # OSX
pip install -r requirements.txt
```

![](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project3/images/weiboTop.png)

其他都挺顺利的，就是我一开始爬[微博热搜榜](https://s.weibo.com/top/summary)的时候，response里面总是没有热搜列表，只有一堆scripts。

改headers都没用，无奈只好打开Charles把请求抓包抓了下来，包括我浏览器的cookie和请求头，然后就成功了。

所以代码长得这么丑，一点也不优雅。而且不知道这个cookie能用几天。。。不过程序的逻辑没啥问题：

![code](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project3/images/code.png)

程序会输出一个markdown列表的格式，看起来舒服些。

### 程序输出

#### 1. 命令行输出Markdown格式文本

2023/1/18 3:38PM 运行结果：

```markdown
- [出站就是团圆](https://s.weibo.com/weibo?q=%23%E5%87%BA%E7%AB%99%E5%B0%B1%E6%98%AF%E5%9B%A2%E5%9C%86%23&Refer=new_time)
- [台当局要下架螺蛳粉民众狂囤货](https://s.weibo.com/weibo?q=%23%E5%8F%B0%E5%BD%93%E5%B1%80%E8%A6%81%E4%B8%8B%E6%9E%B6%E8%9E%BA%E8%9B%B3%E7%B2%89%E6%B0%91%E4%BC%97%E7%8B%82%E5%9B%A4%E8%B4%A7%23&t=31&band_rank=1&Refer=top)
- [王俊凯王一博易烊千玺直播动图](https://s.weibo.com/weibo?q=%23%E7%8E%8B%E4%BF%8A%E5%87%AF%E7%8E%8B%E4%B8%80%E5%8D%9A%E6%98%93%E7%83%8A%E5%8D%83%E7%8E%BA%E7%9B%B4%E6%92%AD%E5%8A%A8%E5%9B%BE%23&t=31&band_rank=2&Refer=top)
- [感谢每个坚守岗位的奋斗者](https://s.weibo.com/weibo?q=%23%E6%84%9F%E8%B0%A2%E6%AF%8F%E4%B8%AA%E5%9D%9A%E5%AE%88%E5%B2%97%E4%BD%8D%E7%9A%84%E5%A5%8B%E6%96%97%E8%80%85%23&t=31&band_rank=3&Refer=top)
- [浪胃仙创始人被逮捕](https://s.weibo.com/weibo?q=%23%E6%B5%AA%E8%83%83%E4%BB%99%E5%88%9B%E5%A7%8B%E4%BA%BA%E8%A2%AB%E9%80%AE%E6%8D%95%23&t=31&band_rank=4&Refer=top)
- [山姆回应蓝环章鱼事件](https://s.weibo.com/weibo?q=%23%E5%B1%B1%E5%A7%86%E5%9B%9E%E5%BA%94%E8%93%9D%E7%8E%AF%E7%AB%A0%E9%B1%BC%E4%BA%8B%E4%BB%B6%23&t=31&band_rank=5&Refer=top)
- [网易称暴雪离婚不离身](https://s.weibo.com/weibo?q=%23%E7%BD%91%E6%98%93%E7%A7%B0%E6%9A%B4%E9%9B%AA%E7%A6%BB%E5%A9%9A%E4%B8%8D%E7%A6%BB%E8%BA%AB%23&t=31&band_rank=6&Refer=top)
- [岳云鹏 师父生日快乐爱您呦](https://s.weibo.com/weibo?q=%E5%B2%B3%E4%BA%91%E9%B9%8F%20%E5%B8%88%E7%88%B6%E7%94%9F%E6%97%A5%E5%BF%AB%E4%B9%90%E7%88%B1%E6%82%A8%E5%91%A6&t=31&band_rank=7&Refer=top)
- [云南一男子连跑三次办结婚证未果](https://s.weibo.com/weibo?q=%23%E4%BA%91%E5%8D%97%E4%B8%80%E7%94%B7%E5%AD%90%E8%BF%9E%E8%B7%91%E4%B8%89%E6%AC%A1%E5%8A%9E%E7%BB%93%E5%A9%9A%E8%AF%81%E6%9C%AA%E6%9E%9C%23&t=31&band_rank=8&Refer=top)
- [张子枫章子怡张颂文演绎初代外交天团](https://s.weibo.com/weibo?q=%23%E5%BC%A0%E5%AD%90%E6%9E%AB%E7%AB%A0%E5%AD%90%E6%80%A1%E5%BC%A0%E9%A2%82%E6%96%87%E6%BC%94%E7%BB%8E%E5%88%9D%E4%BB%A3%E5%A4%96%E4%BA%A4%E5%A4%A9%E5%9B%A2%23&t=31&band_rank=9&Refer=top)
- [黄晓明对家人报喜不报忧](https://s.weibo.com/weibo?q=%23%E9%BB%84%E6%99%93%E6%98%8E%E5%AF%B9%E5%AE%B6%E4%BA%BA%E6%8A%A5%E5%96%9C%E4%B8%8D%E6%8A%A5%E5%BF%A7%23&t=31&band_rank=10&Refer=top)
- [浙江省考](https://s.weibo.com/weibo?q=%E6%B5%99%E6%B1%9F%E7%9C%81%E8%80%83&t=31&band_rank=11&Refer=top)
- [暴雪绿茶定价13](https://s.weibo.com/weibo?q=%23%E6%9A%B4%E9%9B%AA%E7%BB%BF%E8%8C%B6%E5%AE%9A%E4%BB%B713%23&t=31&band_rank=12&Refer=top)
- [金采源恋情](https://s.weibo.com/weibo?q=%23%E9%87%91%E9%87%87%E6%BA%90%E6%81%8B%E6%83%85%23&t=31&band_rank=13&Refer=top)
- [吃播账号浪胃仙被判属原公司](https://s.weibo.com/weibo?q=%23%E5%90%83%E6%92%AD%E8%B4%A6%E5%8F%B7%E6%B5%AA%E8%83%83%E4%BB%99%E8%A2%AB%E5%88%A4%E5%B1%9E%E5%8E%9F%E5%85%AC%E5%8F%B8%23&t=31&band_rank=14&Refer=top)
- [迪奥](https://s.weibo.com/weibo?q=%23%E8%BF%AA%E5%A5%A5%23&t=31&band_rank=15&Refer=top)
- [于和伟 这样的大史形似贴脸了](https://s.weibo.com/weibo?q=%E4%BA%8E%E5%92%8C%E4%BC%9F%20%E8%BF%99%E6%A0%B7%E7%9A%84%E5%A4%A7%E5%8F%B2%E5%BD%A2%E4%BC%BC%E8%B4%B4%E8%84%B8%E4%BA%86&t=31&band_rank=16&Refer=top)
- [文在寅退休后在村里开书店](https://s.weibo.com/weibo?q=%23%E6%96%87%E5%9C%A8%E5%AF%85%E9%80%80%E4%BC%91%E5%90%8E%E5%9C%A8%E6%9D%91%E9%87%8C%E5%BC%80%E4%B9%A6%E5%BA%97%23&t=31&band_rank=17&Refer=top)
- [无名](https://s.weibo.com/weibo?q=%E6%97%A0%E5%90%8D&t=31&band_rank=18&Refer=top)
- [一只猫咪可以有多黑](https://s.weibo.com/weibo?q=%23%E4%B8%80%E5%8F%AA%E7%8C%AB%E5%92%AA%E5%8F%AF%E4%BB%A5%E6%9C%89%E5%A4%9A%E9%BB%91%23&t=31&band_rank=19&Refer=top)
- [福兔](https://s.weibo.com/weibo?q=%23%E7%A6%8F%E5%85%94%23&t=31&band_rank=20&Refer=top)
- [虞书欣北京春晚舞台花絮](https://s.weibo.com/weibo?q=%23%E8%99%9E%E4%B9%A6%E6%AC%A3%E5%8C%97%E4%BA%AC%E6%98%A5%E6%99%9A%E8%88%9E%E5%8F%B0%E8%8A%B1%E7%B5%AE%23&t=31&band_rank=21&Refer=top)
- [陈凯歌保密电影预告还在保密](https://s.weibo.com/weibo?q=%23%E9%99%88%E5%87%AF%E6%AD%8C%E4%BF%9D%E5%AF%86%E7%94%B5%E5%BD%B1%E9%A2%84%E5%91%8A%E8%BF%98%E5%9C%A8%E4%BF%9D%E5%AF%86%23&t=31&band_rank=22&Refer=top)
- [转发王鹤棣的微博能得开心卡](https://s.weibo.com/weibo?q=%23%E8%BD%AC%E5%8F%91%E7%8E%8B%E9%B9%A4%E6%A3%A3%E7%9A%84%E5%BE%AE%E5%8D%9A%E8%83%BD%E5%BE%97%E5%BC%80%E5%BF%83%E5%8D%A1%23&t=31&band_rank=23&Refer=top)
- [宁艺卓生图状态](https://s.weibo.com/weibo?q=%23%E5%AE%81%E8%89%BA%E5%8D%93%E7%94%9F%E5%9B%BE%E7%8A%B6%E6%80%81%23&t=31&band_rank=24&Refer=top)
- [陈飞宇逛街被偶遇](https://s.weibo.com/weibo?q=%23%E9%99%88%E9%A3%9E%E5%AE%87%E9%80%9B%E8%A1%97%E8%A2%AB%E5%81%B6%E9%81%87%23&t=31&band_rank=25&Refer=top)
- [重庆街头巨型兔子灯被市民吐槽太丑](https://s.weibo.com/weibo?q=%23%E9%87%8D%E5%BA%86%E8%A1%97%E5%A4%B4%E5%B7%A8%E5%9E%8B%E5%85%94%E5%AD%90%E7%81%AF%E8%A2%AB%E5%B8%82%E6%B0%91%E5%90%90%E6%A7%BD%E5%A4%AA%E4%B8%91%23&t=31&band_rank=26&Refer=top)
- [人类幼崽为了吃的能有多会](https://s.weibo.com/weibo?q=%23%E4%BA%BA%E7%B1%BB%E5%B9%BC%E5%B4%BD%E4%B8%BA%E4%BA%86%E5%90%83%E7%9A%84%E8%83%BD%E6%9C%89%E5%A4%9A%E4%BC%9A%23&t=31&band_rank=27&Refer=top)
- [妈妈买900斤橘子等女儿回家过年](https://s.weibo.com/weibo?q=%23%E5%A6%88%E5%A6%88%E4%B9%B0900%E6%96%A4%E6%A9%98%E5%AD%90%E7%AD%89%E5%A5%B3%E5%84%BF%E5%9B%9E%E5%AE%B6%E8%BF%87%E5%B9%B4%23&t=31&band_rank=28&Refer=top)
- [网易园区拆除暴雪魔兽斧头雕塑](https://s.weibo.com/weibo?q=%23%E7%BD%91%E6%98%93%E5%9B%AD%E5%8C%BA%E6%8B%86%E9%99%A4%E6%9A%B4%E9%9B%AA%E9%AD%94%E5%85%BD%E6%96%A7%E5%A4%B4%E9%9B%95%E5%A1%91%23&t=31&band_rank=29&Refer=top)
- [新生儿成白肺医生跪地抢救](https://s.weibo.com/weibo?q=%23%E6%96%B0%E7%94%9F%E5%84%BF%E6%88%90%E7%99%BD%E8%82%BA%E5%8C%BB%E7%94%9F%E8%B7%AA%E5%9C%B0%E6%8A%A2%E6%95%91%23&t=31&band_rank=30&Refer=top)
- [原来优雅是不分年龄的](https://s.weibo.com/weibo?q=%23%E5%8E%9F%E6%9D%A5%E4%BC%98%E9%9B%85%E6%98%AF%E4%B8%8D%E5%88%86%E5%B9%B4%E9%BE%84%E7%9A%84%23&t=31&band_rank=31&Refer=top)
- [英专生又多了一个就业方向](https://s.weibo.com/weibo?q=%23%E8%8B%B1%E4%B8%93%E7%94%9F%E5%8F%88%E5%A4%9A%E4%BA%86%E4%B8%80%E4%B8%AA%E5%B0%B1%E4%B8%9A%E6%96%B9%E5%90%91%23&t=31&band_rank=32&Refer=top)
- [许红豆只休三个月的原因](https://s.weibo.com/weibo?q=%23%E8%AE%B8%E7%BA%A2%E8%B1%86%E5%8F%AA%E4%BC%91%E4%B8%89%E4%B8%AA%E6%9C%88%E7%9A%84%E5%8E%9F%E5%9B%A0%23&t=31&band_rank=33&Refer=top)
- [蒲熠星说这调子一季比一季高](https://s.weibo.com/weibo?q=%23%E8%92%B2%E7%86%A0%E6%98%9F%E8%AF%B4%E8%BF%99%E8%B0%83%E5%AD%90%E4%B8%80%E5%AD%A3%E6%AF%94%E4%B8%80%E5%AD%A3%E9%AB%98%23&t=31&band_rank=34&Refer=top)
- [微博音乐盛典](https://s.weibo.com/weibo?q=%E5%BE%AE%E5%8D%9A%E9%9F%B3%E4%B9%90%E7%9B%9B%E5%85%B8&t=31&band_rank=35&Refer=top)
- [龚俊说如果不做演员可能会开串串香店](https://s.weibo.com/weibo?q=%23%E9%BE%9A%E4%BF%8A%E8%AF%B4%E5%A6%82%E6%9E%9C%E4%B8%8D%E5%81%9A%E6%BC%94%E5%91%98%E5%8F%AF%E8%83%BD%E4%BC%9A%E5%BC%80%E4%B8%B2%E4%B8%B2%E9%A6%99%E5%BA%97%23&t=31&band_rank=36&Refer=top)
- [鼓励生育要先解决年轻人的后顾之忧](https://s.weibo.com/weibo?q=%23%E9%BC%93%E5%8A%B1%E7%94%9F%E8%82%B2%E8%A6%81%E5%85%88%E8%A7%A3%E5%86%B3%E5%B9%B4%E8%BD%BB%E4%BA%BA%E7%9A%84%E5%90%8E%E9%A1%BE%E4%B9%8B%E5%BF%A7%23&t=31&band_rank=37&Refer=top)
- [原来做饭真的会加速女性衰老](https://s.weibo.com/weibo?q=%23%E5%8E%9F%E6%9D%A5%E5%81%9A%E9%A5%AD%E7%9C%9F%E7%9A%84%E4%BC%9A%E5%8A%A0%E9%80%9F%E5%A5%B3%E6%80%A7%E8%A1%B0%E8%80%81%23&t=31&band_rank=38&Refer=top)
- [猫咪这表情似乎它听懂了](https://s.weibo.com/weibo?q=%23%E7%8C%AB%E5%92%AA%E8%BF%99%E8%A1%A8%E6%83%85%E4%BC%BC%E4%B9%8E%E5%AE%83%E5%90%AC%E6%87%82%E4%BA%86%23&t=31&band_rank=39&Refer=top)
- [澳网纳达尔出局](https://s.weibo.com/weibo?q=%23%E6%BE%B3%E7%BD%91%E7%BA%B3%E8%BE%BE%E5%B0%94%E5%87%BA%E5%B1%80%23&t=31&band_rank=40&Refer=top)
- [孙俪 我问邓先生今天天气预报](https://s.weibo.com/weibo?q=%E5%AD%99%E4%BF%AA%20%E6%88%91%E9%97%AE%E9%82%93%E5%85%88%E7%94%9F%E4%BB%8A%E5%A4%A9%E5%A4%A9%E6%B0%94%E9%A2%84%E6%8A%A5&t=31&band_rank=41&Refer=top)
- [日本刘大锤](https://s.weibo.com/weibo?q=%E6%97%A5%E6%9C%AC%E5%88%98%E5%A4%A7%E9%94%A4&t=31&band_rank=42&Refer=top)
- [陈都灵新剧孤舟旗袍造型](https://s.weibo.com/weibo?q=%23%E9%99%88%E9%83%BD%E7%81%B5%E6%96%B0%E5%89%A7%E5%AD%A4%E8%88%9F%E6%97%97%E8%A2%8D%E9%80%A0%E5%9E%8B%23&t=31&band_rank=43&Refer=top)
- [中国乒乓首映礼](https://s.weibo.com/weibo?q=%23%E4%B8%AD%E5%9B%BD%E4%B9%92%E4%B9%93%E9%A6%96%E6%98%A0%E7%A4%BC%23&t=31&band_rank=44&Refer=top)
- [宋慧乔黑暗荣耀2定档](https://s.weibo.com/weibo?q=%23%E5%AE%8B%E6%85%A7%E4%B9%94%E9%BB%91%E6%9A%97%E8%8D%A3%E8%80%802%E5%AE%9A%E6%A1%A3%23&t=31&band_rank=45&Refer=top)
- [网易 阴阳师](https://s.weibo.com/weibo?q=%E7%BD%91%E6%98%93%20%E9%98%B4%E9%98%B3%E5%B8%88&t=31&band_rank=46&Refer=top)
- [iG选手](https://s.weibo.com/weibo?q=iG%E9%80%89%E6%89%8B&t=31&band_rank=47&Refer=top)
- [周焯华获刑18年](https://s.weibo.com/weibo?q=%23%E5%91%A8%E7%84%AF%E5%8D%8E%E8%8E%B7%E5%88%9118%E5%B9%B4%23&t=31&band_rank=48&Refer=top)
- [周也新春汉服大片](https://s.weibo.com/weibo?q=%23%E5%91%A8%E4%B9%9F%E6%96%B0%E6%98%A5%E6%B1%89%E6%9C%8D%E5%A4%A7%E7%89%87%23&t=31&band_rank=49&Refer=top)
- [苏醒张远与十年前的自己对话](https://s.weibo.com/weibo?q=%23%E8%8B%8F%E9%86%92%E5%BC%A0%E8%BF%9C%E4%B8%8E%E5%8D%81%E5%B9%B4%E5%89%8D%E7%9A%84%E8%87%AA%E5%B7%B1%E5%AF%B9%E8%AF%9D%23&t=31&band_rank=50&Refer=top)
```

- [出站就是团圆](https://s.weibo.com/weibo?q=%23%E5%87%BA%E7%AB%99%E5%B0%B1%E6%98%AF%E5%9B%A2%E5%9C%86%23&Refer=new_time)
- [台当局要下架螺蛳粉民众狂囤货](https://s.weibo.com/weibo?q=%23%E5%8F%B0%E5%BD%93%E5%B1%80%E8%A6%81%E4%B8%8B%E6%9E%B6%E8%9E%BA%E8%9B%B3%E7%B2%89%E6%B0%91%E4%BC%97%E7%8B%82%E5%9B%A4%E8%B4%A7%23&t=31&band_rank=1&Refer=top)
- [王俊凯王一博易烊千玺直播动图](https://s.weibo.com/weibo?q=%23%E7%8E%8B%E4%BF%8A%E5%87%AF%E7%8E%8B%E4%B8%80%E5%8D%9A%E6%98%93%E7%83%8A%E5%8D%83%E7%8E%BA%E7%9B%B4%E6%92%AD%E5%8A%A8%E5%9B%BE%23&t=31&band_rank=2&Refer=top)
- [感谢每个坚守岗位的奋斗者](https://s.weibo.com/weibo?q=%23%E6%84%9F%E8%B0%A2%E6%AF%8F%E4%B8%AA%E5%9D%9A%E5%AE%88%E5%B2%97%E4%BD%8D%E7%9A%84%E5%A5%8B%E6%96%97%E8%80%85%23&t=31&band_rank=3&Refer=top)
- [浪胃仙创始人被逮捕](https://s.weibo.com/weibo?q=%23%E6%B5%AA%E8%83%83%E4%BB%99%E5%88%9B%E5%A7%8B%E4%BA%BA%E8%A2%AB%E9%80%AE%E6%8D%95%23&t=31&band_rank=4&Refer=top)
- [山姆回应蓝环章鱼事件](https://s.weibo.com/weibo?q=%23%E5%B1%B1%E5%A7%86%E5%9B%9E%E5%BA%94%E8%93%9D%E7%8E%AF%E7%AB%A0%E9%B1%BC%E4%BA%8B%E4%BB%B6%23&t=31&band_rank=5&Refer=top)
- [网易称暴雪离婚不离身](https://s.weibo.com/weibo?q=%23%E7%BD%91%E6%98%93%E7%A7%B0%E6%9A%B4%E9%9B%AA%E7%A6%BB%E5%A9%9A%E4%B8%8D%E7%A6%BB%E8%BA%AB%23&t=31&band_rank=6&Refer=top)
- [岳云鹏 师父生日快乐爱您呦](https://s.weibo.com/weibo?q=%E5%B2%B3%E4%BA%91%E9%B9%8F%20%E5%B8%88%E7%88%B6%E7%94%9F%E6%97%A5%E5%BF%AB%E4%B9%90%E7%88%B1%E6%82%A8%E5%91%A6&t=31&band_rank=7&Refer=top)
- [云南一男子连跑三次办结婚证未果](https://s.weibo.com/weibo?q=%23%E4%BA%91%E5%8D%97%E4%B8%80%E7%94%B7%E5%AD%90%E8%BF%9E%E8%B7%91%E4%B8%89%E6%AC%A1%E5%8A%9E%E7%BB%93%E5%A9%9A%E8%AF%81%E6%9C%AA%E6%9E%9C%23&t=31&band_rank=8&Refer=top)
- [张子枫章子怡张颂文演绎初代外交天团](https://s.weibo.com/weibo?q=%23%E5%BC%A0%E5%AD%90%E6%9E%AB%E7%AB%A0%E5%AD%90%E6%80%A1%E5%BC%A0%E9%A2%82%E6%96%87%E6%BC%94%E7%BB%8E%E5%88%9D%E4%BB%A3%E5%A4%96%E4%BA%A4%E5%A4%A9%E5%9B%A2%23&t=31&band_rank=9&Refer=top)
- [黄晓明对家人报喜不报忧](https://s.weibo.com/weibo?q=%23%E9%BB%84%E6%99%93%E6%98%8E%E5%AF%B9%E5%AE%B6%E4%BA%BA%E6%8A%A5%E5%96%9C%E4%B8%8D%E6%8A%A5%E5%BF%A7%23&t=31&band_rank=10&Refer=top)
- [浙江省考](https://s.weibo.com/weibo?q=%E6%B5%99%E6%B1%9F%E7%9C%81%E8%80%83&t=31&band_rank=11&Refer=top)
- [暴雪绿茶定价13](https://s.weibo.com/weibo?q=%23%E6%9A%B4%E9%9B%AA%E7%BB%BF%E8%8C%B6%E5%AE%9A%E4%BB%B713%23&t=31&band_rank=12&Refer=top)
- [金采源恋情](https://s.weibo.com/weibo?q=%23%E9%87%91%E9%87%87%E6%BA%90%E6%81%8B%E6%83%85%23&t=31&band_rank=13&Refer=top)
- [吃播账号浪胃仙被判属原公司](https://s.weibo.com/weibo?q=%23%E5%90%83%E6%92%AD%E8%B4%A6%E5%8F%B7%E6%B5%AA%E8%83%83%E4%BB%99%E8%A2%AB%E5%88%A4%E5%B1%9E%E5%8E%9F%E5%85%AC%E5%8F%B8%23&t=31&band_rank=14&Refer=top)
- [迪奥](https://s.weibo.com/weibo?q=%23%E8%BF%AA%E5%A5%A5%23&t=31&band_rank=15&Refer=top)
- [于和伟 这样的大史形似贴脸了](https://s.weibo.com/weibo?q=%E4%BA%8E%E5%92%8C%E4%BC%9F%20%E8%BF%99%E6%A0%B7%E7%9A%84%E5%A4%A7%E5%8F%B2%E5%BD%A2%E4%BC%BC%E8%B4%B4%E8%84%B8%E4%BA%86&t=31&band_rank=16&Refer=top)
- [文在寅退休后在村里开书店](https://s.weibo.com/weibo?q=%23%E6%96%87%E5%9C%A8%E5%AF%85%E9%80%80%E4%BC%91%E5%90%8E%E5%9C%A8%E6%9D%91%E9%87%8C%E5%BC%80%E4%B9%A6%E5%BA%97%23&t=31&band_rank=17&Refer=top)
- [无名](https://s.weibo.com/weibo?q=%E6%97%A0%E5%90%8D&t=31&band_rank=18&Refer=top)
- [一只猫咪可以有多黑](https://s.weibo.com/weibo?q=%23%E4%B8%80%E5%8F%AA%E7%8C%AB%E5%92%AA%E5%8F%AF%E4%BB%A5%E6%9C%89%E5%A4%9A%E9%BB%91%23&t=31&band_rank=19&Refer=top)
- [福兔](https://s.weibo.com/weibo?q=%23%E7%A6%8F%E5%85%94%23&t=31&band_rank=20&Refer=top)
- [虞书欣北京春晚舞台花絮](https://s.weibo.com/weibo?q=%23%E8%99%9E%E4%B9%A6%E6%AC%A3%E5%8C%97%E4%BA%AC%E6%98%A5%E6%99%9A%E8%88%9E%E5%8F%B0%E8%8A%B1%E7%B5%AE%23&t=31&band_rank=21&Refer=top)
- [陈凯歌保密电影预告还在保密](https://s.weibo.com/weibo?q=%23%E9%99%88%E5%87%AF%E6%AD%8C%E4%BF%9D%E5%AF%86%E7%94%B5%E5%BD%B1%E9%A2%84%E5%91%8A%E8%BF%98%E5%9C%A8%E4%BF%9D%E5%AF%86%23&t=31&band_rank=22&Refer=top)
- [转发王鹤棣的微博能得开心卡](https://s.weibo.com/weibo?q=%23%E8%BD%AC%E5%8F%91%E7%8E%8B%E9%B9%A4%E6%A3%A3%E7%9A%84%E5%BE%AE%E5%8D%9A%E8%83%BD%E5%BE%97%E5%BC%80%E5%BF%83%E5%8D%A1%23&t=31&band_rank=23&Refer=top)
- [宁艺卓生图状态](https://s.weibo.com/weibo?q=%23%E5%AE%81%E8%89%BA%E5%8D%93%E7%94%9F%E5%9B%BE%E7%8A%B6%E6%80%81%23&t=31&band_rank=24&Refer=top)
- [陈飞宇逛街被偶遇](https://s.weibo.com/weibo?q=%23%E9%99%88%E9%A3%9E%E5%AE%87%E9%80%9B%E8%A1%97%E8%A2%AB%E5%81%B6%E9%81%87%23&t=31&band_rank=25&Refer=top)
- [重庆街头巨型兔子灯被市民吐槽太丑](https://s.weibo.com/weibo?q=%23%E9%87%8D%E5%BA%86%E8%A1%97%E5%A4%B4%E5%B7%A8%E5%9E%8B%E5%85%94%E5%AD%90%E7%81%AF%E8%A2%AB%E5%B8%82%E6%B0%91%E5%90%90%E6%A7%BD%E5%A4%AA%E4%B8%91%23&t=31&band_rank=26&Refer=top)
- [人类幼崽为了吃的能有多会](https://s.weibo.com/weibo?q=%23%E4%BA%BA%E7%B1%BB%E5%B9%BC%E5%B4%BD%E4%B8%BA%E4%BA%86%E5%90%83%E7%9A%84%E8%83%BD%E6%9C%89%E5%A4%9A%E4%BC%9A%23&t=31&band_rank=27&Refer=top)
- [妈妈买900斤橘子等女儿回家过年](https://s.weibo.com/weibo?q=%23%E5%A6%88%E5%A6%88%E4%B9%B0900%E6%96%A4%E6%A9%98%E5%AD%90%E7%AD%89%E5%A5%B3%E5%84%BF%E5%9B%9E%E5%AE%B6%E8%BF%87%E5%B9%B4%23&t=31&band_rank=28&Refer=top)
- [网易园区拆除暴雪魔兽斧头雕塑](https://s.weibo.com/weibo?q=%23%E7%BD%91%E6%98%93%E5%9B%AD%E5%8C%BA%E6%8B%86%E9%99%A4%E6%9A%B4%E9%9B%AA%E9%AD%94%E5%85%BD%E6%96%A7%E5%A4%B4%E9%9B%95%E5%A1%91%23&t=31&band_rank=29&Refer=top)
- [新生儿成白肺医生跪地抢救](https://s.weibo.com/weibo?q=%23%E6%96%B0%E7%94%9F%E5%84%BF%E6%88%90%E7%99%BD%E8%82%BA%E5%8C%BB%E7%94%9F%E8%B7%AA%E5%9C%B0%E6%8A%A2%E6%95%91%23&t=31&band_rank=30&Refer=top)
- [原来优雅是不分年龄的](https://s.weibo.com/weibo?q=%23%E5%8E%9F%E6%9D%A5%E4%BC%98%E9%9B%85%E6%98%AF%E4%B8%8D%E5%88%86%E5%B9%B4%E9%BE%84%E7%9A%84%23&t=31&band_rank=31&Refer=top)
- [英专生又多了一个就业方向](https://s.weibo.com/weibo?q=%23%E8%8B%B1%E4%B8%93%E7%94%9F%E5%8F%88%E5%A4%9A%E4%BA%86%E4%B8%80%E4%B8%AA%E5%B0%B1%E4%B8%9A%E6%96%B9%E5%90%91%23&t=31&band_rank=32&Refer=top)
- [许红豆只休三个月的原因](https://s.weibo.com/weibo?q=%23%E8%AE%B8%E7%BA%A2%E8%B1%86%E5%8F%AA%E4%BC%91%E4%B8%89%E4%B8%AA%E6%9C%88%E7%9A%84%E5%8E%9F%E5%9B%A0%23&t=31&band_rank=33&Refer=top)
- [蒲熠星说这调子一季比一季高](https://s.weibo.com/weibo?q=%23%E8%92%B2%E7%86%A0%E6%98%9F%E8%AF%B4%E8%BF%99%E8%B0%83%E5%AD%90%E4%B8%80%E5%AD%A3%E6%AF%94%E4%B8%80%E5%AD%A3%E9%AB%98%23&t=31&band_rank=34&Refer=top)
- [微博音乐盛典](https://s.weibo.com/weibo?q=%E5%BE%AE%E5%8D%9A%E9%9F%B3%E4%B9%90%E7%9B%9B%E5%85%B8&t=31&band_rank=35&Refer=top)
- [龚俊说如果不做演员可能会开串串香店](https://s.weibo.com/weibo?q=%23%E9%BE%9A%E4%BF%8A%E8%AF%B4%E5%A6%82%E6%9E%9C%E4%B8%8D%E5%81%9A%E6%BC%94%E5%91%98%E5%8F%AF%E8%83%BD%E4%BC%9A%E5%BC%80%E4%B8%B2%E4%B8%B2%E9%A6%99%E5%BA%97%23&t=31&band_rank=36&Refer=top)
- [鼓励生育要先解决年轻人的后顾之忧](https://s.weibo.com/weibo?q=%23%E9%BC%93%E5%8A%B1%E7%94%9F%E8%82%B2%E8%A6%81%E5%85%88%E8%A7%A3%E5%86%B3%E5%B9%B4%E8%BD%BB%E4%BA%BA%E7%9A%84%E5%90%8E%E9%A1%BE%E4%B9%8B%E5%BF%A7%23&t=31&band_rank=37&Refer=top)
- [原来做饭真的会加速女性衰老](https://s.weibo.com/weibo?q=%23%E5%8E%9F%E6%9D%A5%E5%81%9A%E9%A5%AD%E7%9C%9F%E7%9A%84%E4%BC%9A%E5%8A%A0%E9%80%9F%E5%A5%B3%E6%80%A7%E8%A1%B0%E8%80%81%23&t=31&band_rank=38&Refer=top)
- [猫咪这表情似乎它听懂了](https://s.weibo.com/weibo?q=%23%E7%8C%AB%E5%92%AA%E8%BF%99%E8%A1%A8%E6%83%85%E4%BC%BC%E4%B9%8E%E5%AE%83%E5%90%AC%E6%87%82%E4%BA%86%23&t=31&band_rank=39&Refer=top)
- [澳网纳达尔出局](https://s.weibo.com/weibo?q=%23%E6%BE%B3%E7%BD%91%E7%BA%B3%E8%BE%BE%E5%B0%94%E5%87%BA%E5%B1%80%23&t=31&band_rank=40&Refer=top)
- [孙俪 我问邓先生今天天气预报](https://s.weibo.com/weibo?q=%E5%AD%99%E4%BF%AA%20%E6%88%91%E9%97%AE%E9%82%93%E5%85%88%E7%94%9F%E4%BB%8A%E5%A4%A9%E5%A4%A9%E6%B0%94%E9%A2%84%E6%8A%A5&t=31&band_rank=41&Refer=top)
- [日本刘大锤](https://s.weibo.com/weibo?q=%E6%97%A5%E6%9C%AC%E5%88%98%E5%A4%A7%E9%94%A4&t=31&band_rank=42&Refer=top)
- [陈都灵新剧孤舟旗袍造型](https://s.weibo.com/weibo?q=%23%E9%99%88%E9%83%BD%E7%81%B5%E6%96%B0%E5%89%A7%E5%AD%A4%E8%88%9F%E6%97%97%E8%A2%8D%E9%80%A0%E5%9E%8B%23&t=31&band_rank=43&Refer=top)
- [中国乒乓首映礼](https://s.weibo.com/weibo?q=%23%E4%B8%AD%E5%9B%BD%E4%B9%92%E4%B9%93%E9%A6%96%E6%98%A0%E7%A4%BC%23&t=31&band_rank=44&Refer=top)
- [宋慧乔黑暗荣耀2定档](https://s.weibo.com/weibo?q=%23%E5%AE%8B%E6%85%A7%E4%B9%94%E9%BB%91%E6%9A%97%E8%8D%A3%E8%80%802%E5%AE%9A%E6%A1%A3%23&t=31&band_rank=45&Refer=top)
- [网易 阴阳师](https://s.weibo.com/weibo?q=%E7%BD%91%E6%98%93%20%E9%98%B4%E9%98%B3%E5%B8%88&t=31&band_rank=46&Refer=top)
- [iG选手](https://s.weibo.com/weibo?q=iG%E9%80%89%E6%89%8B&t=31&band_rank=47&Refer=top)
- [周焯华获刑18年](https://s.weibo.com/weibo?q=%23%E5%91%A8%E7%84%AF%E5%8D%8E%E8%8E%B7%E5%88%9118%E5%B9%B4%23&t=31&band_rank=48&Refer=top)
- [周也新春汉服大片](https://s.weibo.com/weibo?q=%23%E5%91%A8%E4%B9%9F%E6%96%B0%E6%98%A5%E6%B1%89%E6%9C%8D%E5%A4%A7%E7%89%87%23&t=31&band_rank=49&Refer=top)
- [苏醒张远与十年前的自己对话](https://s.weibo.com/weibo?q=%23%E8%8B%8F%E9%86%92%E5%BC%A0%E8%BF%9C%E4%B8%8E%E5%8D%81%E5%B9%B4%E5%89%8D%E7%9A%84%E8%87%AA%E5%B7%B1%E5%AF%B9%E8%AF%9D%23&t=31&band_rank=50&Refer=top)

#### 2. 当前目录下创建微博热搜榜表格

鉴于CSV格式有跨平台（不可能每个电脑都装Execl吧）而且简洁的特性，我选择创建CSV表格来保存微博热搜数据。

（主要是写入CSV不需要xlrd xlwt pandas这些库的帮助）

CSV文件名符合 `微博热搜榜[年]-[月]-[日] [时][分][秒]`。使用numbers打开:

![](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project3/images/weiboTopCSV.png)

## 版二 爬取四川大学教务管理系统[SCU URP](http://zhjw.scu.edu.cn/)空闲教室

### 安装并运行

> 本项目需要request ddddocr rich等包。
>
> 可使用如下命令安装

```bash
cd project3
pip install -r requirements.txt
```

> 仍然推荐使用虚拟环境，毕竟ddddocr 300+MB不是盖的
> 方法同上

这是一个自动登录，自动爬取SCU URP空闲教室的脚本，没有将结果保存为Excel而是**直接在命令行输出**，因为我觉得后者更优雅一些。

使用者只需要安装所需的python第三方库，然后在`userConfig.json`中设置好自己的账号、密码，即可用`python getFreeClassroom.py`搜索空闲教室了。

### 文件介绍

`userConfig.json` 默认状态+使用说明（注释）

```json
{
    "username": "",             // 用户名（一般就是学号）
    "password": "",             // 密码（zhjw.scu.edu.cn 的登陆密码）
    "campus": 0,                // 校区编号：1:望江 2.华西 3.江安 0.运行时让我选择
    "buildings": [],            // 想要查询的教学楼列表
    "rememberBuildings": false  // 记住我选择的教学楼列表，下次再用
}
```

`queryCodeTeaBuildingList.json` 是从 [四川大学教务管理系统教学楼列表](http://zhjw.scu.edu.cn/student/teachingResources/freeClassroom/queryCodeTeaBuildingList) 爬取下来的json源文件。

由于教学楼列表是不会变的，所以存到本地有助于提高效率，减少请求量。

### 部分技术原理

[点我看演示动图1](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project3/images/display_gif1.gif)

[点我看演示动图2](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project3/images/display_gif2.gif)

- 脚本使用request发送请求，python的rich模块美化输出，使用ddddocr进行自动OCR验证码识别（有一定识别失败率）。脚本输出非常好看，截图如下：

![](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project3/images/getFreeClassroom1.png)

![](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project3/images/getFreeClassroom2.png)

![](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project3/images/getFreeClassroom3.png)

![](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project3/images/getFreeClassroom4.png)

- 主要逻辑代码在`getFreeClassroom.py`中，其中`login()->int`函数负责登录教务系统，`searchFreeClassroom()->int`负责剩下的爬取工作。
- 登录的接口采用 http://zhjw.scu.edu.cn/j_spring_security_check
- 成功登录需要提供：
    - token_value
    - 正确的验证码
    - 正确的账号密码
    - 其中密码采用md5值哈希加密
- 空闲教室的接口为 http://zhjw.scu.edu.cn/student/teachingResources/freeClassroom/today/ 有两个参数，可通过传入`position=01_n`来指定望江的教学楼。


<!-- ![](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project3/images/display_gif1.gif) -->

<!-- ![](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project3/images/display_gif2.gif) -->


