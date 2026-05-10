import os
import logging
from dotenv import load_dotenv
from pyrogram import Client, filters

load_dotenv()

# Configuration
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

bot_username = None

@app.on_startup
async def startup(client):
    global bot_username
    me = await client.get_me()
    bot_username = me.username
    logger.info(f"Bot started as @{bot_username}")

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text(
        "**ഹലോ!**\n\nഎനിക്ക് ഒരു വീഡിയോ അല്ലെങ്കിൽ ഫയൽ അയച്ചു തരൂ."
    )

@app.on_message((filters.video | filters.document) & filters.private)
async def generate_link(client, message):
    try:
        file_id = message.video.file_id if message.video else message.document.file_id
        file_name = (message.video.file_name or message.document.file_name) or "Unknown"
        
        msg = await message.reply_text("⏳ ലിങ്ക് തയ്യാറാക്കുന്നു...")
        
        link = f"https://t.me/{bot_username}?start={file_id}"
        
        caption = (
            f"**✅ ലിങ്ക് റെഡി!**\n\n"
            f"**📄 ഫയൽ:** `{file_name}`\n"
            f"**🔗 ലിങ്ക്:** {link}"
        )
        
        await msg.edit_text(caption)
        logger.info(f"Link generated for {file_name}")
    except Exception as e:
        logger.error(f"Error generating link: {e}")
        await msg.edit_text(f"❌ എറർ സംഭവിച്ചു: കൃത്യമായി വീണ്ടും ശ്രമിക്കൂ.")

if __name__ == "__main__":
    app.run()
