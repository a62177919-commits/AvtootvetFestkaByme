from pyrogram import Client, filters
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

app = Client(
    "session",  # имя твоего session.session
    api_id=api_id,
    api_hash=api_hash
)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("Pyrogram автоответчик работает!")

@app.on_message(filters.command("ping"))
async def ping_handler(client, message):
    await message.reply("pong")

@app.on_message(filters.text & ~filters.command(["start", "ping"]))
async def echo_handler(client, message):
    await message.reply(f"Ты написал: {message.text}")

print("Бот запущен и слушает сообщения...")
app.run()