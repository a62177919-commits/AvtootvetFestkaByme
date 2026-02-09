from telethon import TelegramClient, events
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

# Используем session.session из репозитория
client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(pattern=r'^/start$'))
async def start(event):
    await event.reply("Бот работает! Сессия активна.")

@client.on(events.NewMessage(pattern=r'^/ping$'))
async def ping(event):
    await event.reply("pong")

@client.on(events.NewMessage)
async def echo(event):
    text = event.raw_text
    if text.startswith("/"):
        return
    await event.reply(f"Ты написал: {text}")

async def main():
    print("Бот запущен и слушает сообщения...")

client.start()
client.loop.run_until_complete(main())
client.run_until_disconnected()