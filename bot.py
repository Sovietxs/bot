from vkbottle.user import User, Message
import random
import time
import secondsconverter
import asyncio

user = User("твой токен https://oauth.vk.com/authorize?client_id=6146827&scope=1073737727&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1", debug=True, mobile=True)


@user.on.message_handler(text=["команды", "помощь", "хелп"], lower=True)
async def commands(ans: Message):
    emoji = random.choice("🙊🤕🤓💬💭🌍🌈🌐🎨🧱")
    await ans(f"{emoji} » Мои команды:\n"
              "• Секс\n"
              "• Флекс\n"
              "• Сообщение <время> <текст>\n\n"
              "🖍 » Примечания:\n️"
              "• Для корректной работы мне требуются права администратора в чате.\n"
              "• Команды \"Секс/Флекс\" требуют отвечать на сообщения человека, для взаимодействия.\n"
              "• В команде \"Сообщение\" аргумент \"время\" принимает значение в секундах вплоть до 86400.\n")


@user.on.message_handler(text=["секс", "выебать", "трахнуть"], lower=True)
async def sex(ans: Message):
    phrases = random.choice(["выебал", "принудил к сексу", "трахнул", "обкончал", "выебал в рот", "кончил в рот", "пернул в рот", "нагнул", "жестоко трахнул", "отдался в руки", "стал пидором, благодаря рукам", "пизданул хуем в рот", "отодрал зад", "порвал очко"])
    emoji = random.choice("😏♥️🤐😱🤯😵🥵🤑😎☠️🙊💘🔥👄👅💑🌭?🥒🍌🍑🚨🚓💍💄🚫🔞")
    
    sticker = random.choice([11118, 11125, 12116, 6310, 6325, 4859, 4863, 4865])
    
    if ans.reply_message:
        if ans.reply_message.from_id == 2517089734:
            await ans(f"{emoji} • Себя трахни, ублюдок😏")
        elif ans.reply_message.from_id > 0:
            user_first = await user.api.users.get(user_ids=ans.from_id)
            user_second = await user.api.users.get(user_ids=ans.reply_message.from_id, name_case="acc")
            message = f"{emoji} • *id{ans.from_id} ({user_first[0].first_name} {user_first[0].last_name}) {phrases} *id{ans.reply_message.from_id} ({user_second[0].first_name} {user_second[0].last_name}) (команда будет доступна через 3 сек.)"
            await user.api.messages.send(peer_id=ans.peer_id, message=message, random_id=random.randint(1,99999), expire_ttl=10, disable_mentions=True)
            await asyncio.sleep(3)
        else:
            await ans(f"{emoji} • Взаимодействие с пользователями типа «BOT» запрещены.")
    else:
        await ans(f"{emoji} • Ответьте на сообщение пользователя, прописав данную команду.")


@user.on.message_handler(text=["танец", "станцевать", "танцевать", "флекс", "флексить", "денсить", "зафлексить", "заденсить"], lower=True)
async def dance(ans: Message):
    phrases = random.choice(["станцевал для", "пофлексил для", "зафлексил для", "попрыгал для", "заденсил для", "повертел ногами для", "станцевал стриптиз для", "станцевал, но ему помешали яйца для", "флексанул для", "пригласил на танец и потанцевал для"])
    emoji = random.choice("🔥🤖🤸💃🕺🧔👯👭")
    
    if ans.reply_message:
        if ans.reply_message.from_id > 0:
            user_first = await user.api.users.get(user_ids=ans.from_id)
            user_second = await user.api.users.get(user_ids=ans.reply_message.from_id, name_case="gen")

            message = f"{emoji} • *id{ans.from_id} ({user_first[0].first_name} {user_first[0].last_name}) {phrases} *id{ans.reply_message.from_id} ({user_second[0].first_name} {user_second[0].last_name}) (команда будет доступна через 3 сек.)"
            await user.api.messages.send(peer_id=ans.peer_id, message=message, random_id=random.randint(1,99999), expire_ttl=10, disable_mentions=True)
            await asyncio.sleep(3)
        else:
            await ans(f"{emoji} • Взаимодействие с пользователями типа «BOT» запрещены.")
    else:
        await ans(f"{emoji} • Ответьте на сообщение пользователя, прописав данную команду.")


@user.on.message_handler(text=["позвать", "созвать"], lower=True)
async def conversation_members(ans: Message):
    emoji = "🐀🐁🐂🐃🐄🐅🐆🐇🐈🐉🐊🐋🐌🐍🐎🐐🐑🐒🐓🐔🐕🐖🐗🐘🐙🐛🐜🐝🐞🐟🐠🐡🐢🐥🐦🐧🐨🐪🐫🐬🐭🐮🐯🐰🐳🐴🐵🐶🐷🐸🐹🐺🐻🐼⛄"
    if ans.from_id == 251708973:
        members = await user.api.messages.get_conversation_members(peer_id=ans.peer_id)
        members_ids = []
        for i in range(members.count):
            if members.items[i].member_id > 0:
                members_ids.append(str(members.items[i].member_id))
                
        members_ids_normal = ""
        for i in members_ids:
            members_ids_normal = members_ids_normal + " [id" + str(i) + (f"|{random.choice(emoji)}]")
        message = f"• *id{ans.from_id} (Вы) позвали всех участников чата.\n{members_ids_normal}"
        await user.api.messages.send(peer_id=ans.peer_id, message=message, random_id=random.randint(1,99999), expire_ttl=10, disable_mentions=False)
    else:
        pass


@user.on.message_handler(text=["сообщение <interval:int> <text>"], lower=True)
async def msg_timer(ans: Message,interval, text):
    if interval <= 86400:
        if "vto.pe" not in text.lower():
            user_data = await user.api.users.get(user_ids=ans.from_id)
            if len(text) < 250:
                msg =f"*id{ans.from_id} (») " + text.capitalize().replace(".", " ").replace("@", "").replace("/", " ") + f"\n• *id{ans.from_id} ({user_data[0].first_name} {user_data[0].last_name})"
            
                await user.api.messages.send(peer_id=ans.peer_id, message=msg, random_id=random.randint(1,99999), expire_ttl=interval, disable_mentions=True, dont_parse_links=True)
            else:
                await user.api.messages.send(peer_id=ans.peer_id, message=f"• Сообщение не может быть длиной более 250 символов.", random_id=random.randint(1,99999), expire_ttl=5, disable_mentions=True)
        else:
            await user.api.messages.send(peer_id=ans.peer_id, message=f"• *id{ans.from_id} (Ты) случайно хуём подавился 😘.", random_id=random.randint(1,99999), expire_ttl=60, disable_mentions=False)
    else:
        await user.api.messages.send(peer_id=ans.peer_id, message=f"• Указывать интервал больше 86400 (24 часа) запрещено.", random_id=random.randint(1,99999), expire_ttl=5, disable_mentions=True)
    try:
        await user.api.messages.delete(message_ids=ans.message_id, delete_for_all=1)
    except:
        pass

@user.on.message_handler(text=["code <text>", "код <text>"], lower=True)
async def code(ans: Message, text):
	if ans.from_id == 251708973:
		try:
			evaled = eval(text)
			await ans(f"{evaled}")
		except Exception as error:
			await ans(f"Ошибка > {error}")
	else:
		await ans("У вас нету прав!")

        

user.run_polling()