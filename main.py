import os
import asyncio
from pyrogram import Client, filters

# നിന്റെ വിവരങ്ങൾ (ഇത് കൃത്യമാണെന്ന് ഉറപ്പുവരുത്തുക)
API_ID = 34315895 
API_HASH = "e8fcf47ab1442cea2a778f580f8f299d"
BOT_TOKEN = "8263661855:AAH5R8GVLX6GOLnypXncsGv3dhtVQWwkMk8"

app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text(
        "**ഹലോ!**\n\nഎനിക്ക് ഒരു വീഡിയോ അല്ലെങ്കിൽ ഫയൽ അയച്ചു തരൂ, ഞാൻ അതിന്റെ ഷെയറബിൾ ലിങ്ക് തരാം."
    )

@app.on_message((filters.video | filters.document) & filters.private)
async def generate_link(client, message):
    # ഫയൽ ഇൻഫർമേഷൻ എടുക്കുന്നു
    file_id = message.video.file_id if message.video else message.document.file_id
    file_name = message.video.file_name if message.video else message.document.file_name
    
    msg = await message.reply_text("⏳ ലിങ്ക് തയ്യാറാക്കുന്നു... ദയവായി കാത്തിരിക്കൂ.")
    
    try:
        # ബോട്ടിന്റെ യൂസർനെയിം എടുക്കുന്നു
        bot_info = await client.get_me()
        bot_username = bot_info.username
        
        # ടെലിഗ്രാം ഡയറക്ട് ലിങ്ക് ഫോർമാറ്റ്
        link = f"https://t.me/{bot_username}?start={file_id}"
        
        caption = (
            f"**✅ ലിങ്ക് റെഡി!**\n\n"
            f"**📄 ഫയൽ:** `{file_name}`\n"
            f"**🔗 ലിങ്ക്:** {link}\n\n"
            f"_*ശ്രദ്ധിക്കുക: ഈ ലിങ്ക് ബോട്ട് വഴി മാത്രമേ പ്രവർത്തിക്കൂ._"
        )
        
        await msg.edit_text(caption)
    except Exception as e:
        await msg.edit_text(f"❌ എറർ സംഭവിച്ചു: {e}")

# ബോട്ട് റൺ ചെയ്യുന്നു
if __name__ == "__main__":
    app.run()
