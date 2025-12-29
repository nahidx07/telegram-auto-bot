import asyncio
from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated
from apscheduler.schedulers.asyncio import AsyncIOScheduler

API_ID = 37269932
API_HASH = "8ac0efd814be34d613addc15e9d3f8ce"
BOT_TOKEN = "8482864533:AAGHtvmZhhYxmz-lk22YLy9MA_PhwWJnPk8"

CHANNEL_ID = -1001234567890   # আপনার চ্যানেল
GROUP_IDS = [-1001111111111]  # গ্রুপ লিস্ট

app = Client(
    "auto_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_chat_member_updated()
async def welcome(client, event: ChatMemberUpdated):
    if event.new_chat_member:
        await client.send_message(
            event.chat.id,
            f"👋 Welcome {event.new_chat_member.user.mention}!\nআমাদের গ্রুপে স্বাগতম 🤍"
        )

async def auto_post():
    async for msg in app.get_chat_history(CHANNEL_ID, limit=1):
        for group in GROUP_IDS:
            await app.copy_message(group, CHANNEL_ID, msg.id)

scheduler = AsyncIOScheduler()
scheduler.add_job(auto_post, "interval", minutes=20)

async def main():
    scheduler.start()
    await app.start()
    await asyncio.Event().wait()

asyncio.run(main())
