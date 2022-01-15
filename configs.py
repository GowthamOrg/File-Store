# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **ᴍʏ ɴᴀᴍᴇ:** [𝙵𝚒𝚕𝚎𝚂𝚝𝚘𝚛𝚎𝙱𝚘𝚝](https://t.me/{BOT_USERNAME})

📝 **ʟᴀɴɢᴜᴀɢᴇ:** [𝙿𝚢𝚝𝚑𝚘𝚗3](https://www.python.org)

📚 **ʟɪʙʀᴀʀʏ:** [𝙿𝚢𝚛𝚘𝚐𝚛𝚊𝚖](https://docs.pyrogram.org)

📡 **ʜᴏsᴛᴇᴅ ᴏɴ:** [𝙷𝚎𝚛𝚘𝚔𝚞](https://heroku.com)

🧑🏻‍💻 **ᴅᴇᴠᴇʟᴏᴘᴇʀ:** @benwolf24

👥 **ɢʀᴏᴜᴘ:** [𝚂𝚞𝚙𝚙𝚘𝚛𝚝𝙶𝚛𝚘𝚞𝚙](https://t.me/rex_bots_support)

📢 **ᴄʜᴀɴɴᴇʟ:** [𝚁𝚎𝚡𝙱𝚘𝚝𝚣](https://t.me/rex_botz)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛:** @benwolf24

𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 𝚒𝚜 𝚜𝚞𝚙𝚎𝚛 𝙽𝚘𝚘𝚋. 𝙹𝚞𝚜𝚝 𝚕𝚎𝚊𝚛𝚗𝚒𝚗𝚐 𝚏𝚛𝚘𝚖 𝚘𝚏𝚏𝚒𝚌𝚒𝚊𝚕 𝙳𝚘𝚌𝚜. 𝙿𝚕𝚎𝚊𝚜𝚎 𝙳𝚘𝚗𝚊𝚝𝚎 𝚝𝚑𝚎 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 𝚝𝚘 𝚔𝚎𝚎𝚙 𝚝𝚑𝚒𝚜 𝚜𝚎𝚛𝚟𝚒𝚌𝚎 𝚊𝚕𝚒𝚟𝚎.

𝙰𝚕𝚜𝚘 𝚛𝚎𝚖𝚎𝚖𝚋𝚎𝚛 𝚝𝚑𝚊𝚝 𝚊𝚍𝚞𝚕𝚝 𝚌𝚘𝚗𝚝𝚎𝚗𝚝𝚜 𝚠𝚒𝚕𝚕 𝚋𝚎 𝚛𝚎𝚖𝚘𝚟𝚎𝚍 𝚋𝚢 𝚍𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛. 𝚂𝚘 𝚋𝚎𝚝𝚝𝚎𝚛 𝚍𝚘𝚗'𝚝 𝚜𝚝𝚘𝚛𝚎 𝚝𝚑𝚘𝚜𝚎 𝚔𝚒𝚗𝚍𝚜 𝚘𝚏 𝚝𝚑𝚒𝚗𝚐𝚜.

[ᴅᴏɴᴀᴛᴇ ᴅᴇᴠ](https://t.me/benwolf24) (AnyMethod)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\n𝚃𝚑𝚒𝚜 𝚒𝚜 𝚊 𝙿𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 **𝙵𝚒𝚕𝚎 𝚂𝚝𝚘𝚛𝚎 𝙱𝚘𝚝**.

𝚂𝚎𝚗𝚍 𝙼𝚎 𝚊𝚗𝚢 𝙵𝚒𝚕𝚎 𝙸 𝚠𝚒𝚕𝚕 𝚐𝚒𝚟𝚎 𝚢𝚘𝚞 𝚙𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚜𝚑𝚊𝚛𝚊𝚋𝚕𝚎 𝙻𝚒𝚗𝚔. 𝙸 𝚜𝚞𝚙𝚙𝚘𝚛𝚝 𝚒𝚗 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚊𝚕𝚜𝚘! 𝙲𝚑𝚎𝚌𝚔 **About Bot** 𝙱𝚞𝚝𝚝𝚘𝚗.
"""
