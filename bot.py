from telethon import TelegramClient, events
import os

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")

client = TelegramClient("session", api_id, api_hash)

async def main():
    print("Бот запущен и слушает сообщения...")

# Обработчик команды /start
@client.on(events.NewMessage(pattern=r'^/start$'))
async def start_handler(event):
    await event.reply("Бот работает! Сессия активна.")

# Обработчик команды /ping
@client.on(events.NewMessage(pattern=r'^/ping$'))
async def ping_handler(event):
    await event.reply("pong")

# Обработчик любого текста
@client.on(events.NewMessage)
async def echo_handler(event):
    if event.raw_text.startswith("/"):
        return
    await event.reply(f"Ты написал: {event.raw_text}")

client.start()
client.loop.run_until_complete(main())
client.run_until_disconnected()