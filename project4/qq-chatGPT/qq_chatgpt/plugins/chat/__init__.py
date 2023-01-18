from nonebot.adapters.onebot.v11 import GroupMessageEvent, PrivateMessageEvent
from nonebot.adapters.onebot.v11 import Bot, Message, Event, MessageSegment
from nonebot import on_command, get_driver, logger
from nonebot.params import CommandArg
from .config import default_config, OpenAIConfig
import openai
import pickle
import ast

try:
    openai_config = OpenAIConfig.parse_obj(get_driver().config)
except Exception as e:
    import sys
    logger.opt(colors=True).critical(f'<r>OPENAI API KEY获取失败</r>, 错误信息:\n{e}')
    sys.exit()

if (openai_config.openai_api_key == ""):
    import sys
    logger.opt(colors=True).critical('<r>您未填写OPENAI API KEY</r>')
    sys.exit()

openai.api_key = openai_config.openai_api_key
openai.organization = openai_config.openai_organization

# TODO:edit paragraph | code completion | toll back
catch_ask_str = on_command("ask", aliases={"问一下", "问问"})
catch_chat_str = on_command("chat", aliases={"聊天"})
catch_help_str = on_command("help", aliases={"帮助"})
catch_edit_str = on_command("edit", aliases={"编辑"})
catch_clear_str = on_command("clear", aliases={"清除"})
catch_image_str = on_command("image", aliases={"图片"})
catch_test_str = on_command("test", aliases={"测试"})
catch_backup_str = on_command("backup", aliases={"备份"})
catch_load_str = on_command("load", aliases={"restore", "恢复"})
catch_tollback_str = on_command("toll", aliases={"回滚"})

group_sessions = {}
private_sessions = {}


def latest_conversation(session_id: str) -> str:
    if "private_" in session_id:
        if private_sessions.get(session_id):
            return private_sessions[session_id]['context'].rsplit('\n\n', 1)[-1]
    if "group_" in session_id:
        if group_sessions.get(session_id):
            return group_sessions[session_id]['context'].rsplit('\n\n', 1)[-1]


@catch_ask_str.handle()
async def group_ask_msg(gm: GroupMessageEvent, args: Message = CommandArg()):
    group_id, msg_id = gm.group_id, gm.message_id
    session_id = f"group_{group_id}"
    if not group_sessions.get(session_id):
        group_sessions[session_id] = default_config.copy()
    local_config = group_sessions[session_id]
    questions = args.extract_plain_text()
    local_config["completion"]["prompt"] = f"Q: {questions}\nA: "
    response = openai.Completion.create(**local_config["completion"])
    response_text = response["choices"][0]["text"].strip()
    msg = Message(f"[CQ:reply,id={msg_id}]{response_text}")
    await catch_ask_str.finish(msg)


@catch_ask_str.handle()
async def private_ask_msg(pm: PrivateMessageEvent, args: Message = CommandArg()):
    user_id = pm.user_id
    session_id = f"private_{user_id}"
    if not private_sessions.get(session_id):
        private_sessions[session_id] = default_config.copy()
    local_config = private_sessions[session_id]
    questions = args.extract_plain_text()
    local_config["completion"]["prompt"] = f"Q: {questions}\nA: "
    response = openai.Completion.create(**local_config["completion"])
    # delelte the "\n" in resopnse_text
    response_text = response["choices"][0]["text"].strip()
    msg = Message(response_text)
    await catch_ask_str.finish(msg)


@catch_chat_str.handle()
async def group_chat_msg(gm: GroupMessageEvent, args: Message = CommandArg()):
    group_id, msg_id = gm.group_id, gm.message_id
    session_id = f"group_{group_id}"
    if not group_sessions.get(session_id):
        group_sessions[session_id] = default_config.copy()
    local_config = group_sessions[session_id]
    questions = args.extract_plain_text()
    local_config["context"] += f"\n\nQ: {questions}\nA: "
    local_config["completion"]["prompt"] = local_config["context"]
    print(local_config["completion"]["prompt"])
    try:
        response = openai.Completion.create(**local_config["completion"])
        response_text = response["choices"][0]["text"].strip()
        local_config["context"] += response_text
        msg = Message(f"[CQ:reply,id={msg_id}]{response_text}")
    except openai.error.InvalidRequestError as e:
        logger.opt(colors=True).critical(f"Tokens太长！已重置上下文。\n错误信息：{e}")
        local_config["context"] = ""
        msg = Message("Tokens Error Occured!")
    await catch_chat_str.finish(msg)


@catch_chat_str.handle()
# handle in private chat
async def private_chat_msg(pm: PrivateMessageEvent, args: Message = CommandArg()):
    user_id = pm.user_id  # or event.get_user_id()
    session_id = f"private_{user_id}"
    if not private_sessions.get(session_id):
        private_sessions[session_id] = default_config.copy()
    local_config = private_sessions[session_id]
    questions = args.extract_plain_text()
    local_config["context"] += f"\n\nQ: {questions}\nA: "
    local_config["completion"]["prompt"] = local_config["context"]
    print(local_config["completion"]["prompt"])
    try:
        response = openai.Completion.create(**local_config["completion"])
        response_text = response["choices"][0]["text"].strip()
        local_config["context"] += response_text
        msg = Message(response_text)
    except openai.error.InvalidRequestError as e:
        logger.opt(colors=True).critical(f"Tokens太长！已重置上下文。\n错误信息：{e}")
        local_config["context"] = ""
        msg = Message("Tokens Error Occured!")
    await catch_chat_str.finish(msg)


@catch_image_str.handle()
async def send_image_msg(args: Message = CommandArg()):
    prompt = args.extract_plain_text()
    await catch_image_str.send(Message("Image generating... Please wait."))
    for size in ["256x256", "512x512", "1024x1024"]:
        if size in prompt:
            default_config["generate_image"]["size"] = size
            prompt = prompt.replace(size, "")
    default_config["generate_image"]["prompt"] = prompt
    response = openai.Image.create(**default_config["generate_image"])
    image_url = response["data"][0]["url"]
    msg = Message(MessageSegment.image(image_url))
    await catch_image_str.finish(msg)


@catch_clear_str.handle()
async def group_clear_msg(gm: GroupMessageEvent, args: Message = CommandArg()):
    group_id = gm.group_id
    session_id = f"group_{group_id}"
    if not group_sessions.get(session_id):
        group_sessions[session_id] = default_config.copy()
    group_sessions[session_id]["context"] = ""
    msg = Message("cleared all contexts! 已清除所有上下文！")
    await catch_clear_str.finish(msg)


@catch_clear_str.handle()
async def private_clear_msg(pm: PrivateMessageEvent, args: Message = CommandArg()):
    user_id = pm.user_id  # or event.get_user_id()
    session_id = f"private_{user_id}"
    if not private_sessions.get(session_id):
        private_sessions[session_id] = default_config.copy()
    private_sessions[session_id]["context"] = ""
    msg = Message("cleared all contexts! 已清除所有上下文！")
    await catch_clear_str.finish(msg)


@catch_tollback_str.handle()
async def send_tollback_msg(pm: PrivateMessageEvent, args: Message = CommandArg()):
    try:
        number = int(args.extract_plain_text())
    except ValueError:
        await catch_tollback_str.reject(".toll后面应该跟数字，表示回滚的条数，请重新输入！")
    session_id = f"private_{pm.user_id}"
    if not private_sessions.get(session_id):
        private_sessions[session_id] = default_config.copy()
    local_config = private_sessions[session_id]
    local_config["context"] = local_config["context"].rsplit("\n\n", number)[0]
    msg = Message(f"tollbacked! 已回滚{number}条上下文！")
    catch_clear_str.send(msg)
    msg = Message(f"我只记得上次聊到：\n{latest_conversation(session_id)}")
    await catch_tollback_str.finish(msg)


@catch_backup_str.handle()
async def backup(args: Message = CommandArg()):
    # back up all sessions to pickles
    with open("./qq_chatgpt/pickles/group_sessions.pkl", "wb") as f:
        pickle.dump(group_sessions, f)
    with open("./qq_chatgpt/pickles/private_sessions.pkl", "wb") as f:
        pickle.dump(private_sessions, f)
    msg = Message("Backuped! 已备份所有数据！")
    await catch_clear_str.finish(msg)


@catch_load_str.handle()
async def load(args: Message = CommandArg()):
    try:
        # load all sessions from pickles
        with open("./qq_chatgpt/pickles/group_sessions.pkl", "rb") as f:
            group_sessions = pickle.load(f)
        with open("./qq_chatgpt/pickles/private_sessions.pkl", "rb") as f:
            private_sessions = pickle.load(f)
    except FileNotFoundError:
        msg = Message("No backup file found! 未找到备份文件！")
        await catch_clear_str.finish(msg)
    print(group_sessions)
    print(private_sessions)
    msg = Message("Loaded all data! 已加载所有数据！")
    await catch_clear_str.finish(msg)


@catch_help_str.handle()
async def send_help_msg(args: Message = CommandArg()):
    msg = Message("""
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
""".strip())
    await catch_help_str.finish(msg)


@catch_test_str.handle()
async def send_test_msg(bot: Bot, event: Event, pm: PrivateMessageEvent, args: Message = CommandArg()):
    # userid = int(event.get_user_id())
    # group_id = group_event.group_id
    # print(group_id)
    data = await bot.call_api("get_group_info", group_id=980698737)
    # 对json进行转义
    data = ast.literal_eval(str(data))
    print(data)
    # await bot.send_group_msg(group_id=980698737, message="test ok!")
    # msg = MessageSegment.location(latitude=39.90469, longitude=116.40717)
    # seq = bot.call_api("get_msg", message_id=ME.message_id)
    # print("the_seq_is:", str(seq.cr_code))
    msg = Message(f"[CQ:reply,id={pm.message_id}]123")
    await catch_test_str.send(msg)
    msg = Message([
        MessageSegment.text(f"群号：{data['group_id']}\n"),
        MessageSegment.text(f"群名称：{data['group_name']}\n"),
        # MessageSegment.image("https://cdn.luogu.com.cn/fe/logo.png"),
        MessageSegment.text(f"成员数：{data['member_count']}\n"),
    ])
    await catch_test_str.send(msg)
    # await catch_test_str.send(
    #     MessageSegment.image(
    #         file="https://cdn.luogu.com.cn/fe/logo.png", type_="flash"
    #     )
    # )
    await catch_test_str.send(Message("[CQ:dice,value=1]"))
    await catch_test_str.finish()
