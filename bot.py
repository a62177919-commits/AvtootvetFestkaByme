import os
from telethon import TelegramClient, events

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("session", api_id, api_hash)

auto_reply_enabled = True

@client.on(events.NewMessage)
async def main_handler(event):
    global auto_reply_enabled

    if event.raw_text == "/on":
        auto_reply_enabled = True
        await event.reply("Автоответчик включён")
        return

    if event.raw_text == "/off":
        auto_reply_enabled = False
        await event.reply("Автоответчик выключен")
        return

    if auto_reply_enabled and event.is_private:
        await event.reply("Привет! Я сейчас не могу ответить, напишу позже.")

client.start()
print("Userbot запущен")
client.run_until_disconnected()
