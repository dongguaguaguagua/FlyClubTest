# 基于Nonebot的QQchatBot实现

最近火爆的chatGPT把AI聊天的热度推向新高。于是我就想结合chatGPT实现一个简单的聊天机器人。

通过使用最快的go-cqhttp框架和基于One-Bot协议的Nonebot2，使开发变得容易许多。

然而，chatGPT最近把API封锁了，github上没法找到其任何破解出来的API，包括相关的python第三方库也挂了。

所以我退而求其次，选择了基于GPT-3的text-davinci-003引擎（要知道chatGPT是基于GPT-3.5）相当于弱化版的chatGPT。

这里我不提供OPENAI_API_KEY，因为这是private的key，不允许分享到GitHub上面。请使用者在终端上运行：

```bash
export OPENAI_API_KEY=sk-****
```

程序会自动读取环境变量中的OPENAI_API_KEY，如果不存在则无法启动机器人，而如果api-key不合法，则启动后无法回答任何问题。

qq-chatgpt中包含两个nonebot2插件——chat和qqcard。我这里主要介绍chat插件。首先，基本的配置在`project4/qq-chatGPT/qq_chatgpt/plugins/chat/config.py`中，主要的逻辑则在`project4/qq-chatGPT/qq_chatgpt/plugins/chat/__init__.py`中实现。

## 如何运行？

请阅读Nonebot2的官方文档，配置好相关开发环境后，运行本插件。请看动图：

![nb run](https://raw.githubusercontent.com/dongguaguaguagua/fly_club_test/main/project4/images/HowToRunIt.gif)

机器人可以被关键字`.xxx`触发，主要实现了：

```bash
.ask        # 问AI问题，不产生上下文
.chat       # 与AI聊天，产生上下文
.clear      # 清除上下文
.image      # 生成图片，需输入图片描述
.help       # 查看帮助
.toll       # 条数n（回滚n条对话）
.backup     # 备份对话
.restore    # 恢复对话
```

## 介绍8个命令

### 1. ask命令

ask只记录一段对话。就是说，问第二个问题是，bot已经忘掉你第一句问了什么了。

### 2. chat命令

bot会记录所有「聊天」记录，即可以通过不断发送`.chat 请问xxxxx`来实现对话。其中夹杂.ask不会影响bot的记忆。

### 3. clear命令

意思就是让bot忘记刚刚的对话，从头开始。

### 4. image命令

通过OPENAI的图像生成引擎返回一张图片。有一个参数（optional），就是图片的大小，有`256x256, 512x512, 1024x1024`三个值可选，默认为256x256。图像越大生成得越慢。

### 5. help命令

bot会告诉你它的使用方法：

```text
欢迎使用chatbot QQ机器人！
基于NoneBot2.0，使用ChatGPT API实现的聊天机器人。
.ask 问AI问题，不产生上下文
.chat 与AI聊天，产生上下文
.clear 清除上下文
.image 生成图片，需输入图片描述
.help 查看帮助
.toll 条数n（回滚n条对话）
.backup 备份对话
.restore 恢复对话
[作者：@nanguagua]
```

### 6. toll命令

有一个参数为回滚的条数，`.toll 3`就是忘记三条对话。这在说错话时很管用。

### 7. backup命令

没有参数。用于把对话储存到本地。由于这个机器人还在更新维护中，所以停掉之前备份一下对话是很有必要的。

`project4/qq-chatGPT/qq_chatgpt/pickles`目录用于存放备份的`.pkl`文件。

### 8. restore命令

没有参数。用于恢复对话。

## 最后运行效果

![nb run](https://raw.githubusercontent.com/dongguaguaguagua/fly_club_test/main/project4/images/test_robot.png)
