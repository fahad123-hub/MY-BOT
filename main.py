import os
from pyrogram import Client, filters

# നിന്റെ വിവരങ്ങൾ ഇവിടെ ചേർക്കുക
API_ID = 34315895  # നിന്റെ API ID ഇവിടെ നൽകുക
API_HASH = "e8fcf47ab1442cea2a778f580f8f299d"
BOT_TOKEN = "8263661855:AAH5R8GVLX6GOLnypXncsGv3dhtVQWwkMk8"

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("ഹലോ! എനിക്ക് വീഡിയോ അയച്ചു തരൂ, ഞാൻ അതിന്റെ ലിങ്ക് തരാം. (ലിങ്ക് താത്കാലികമായിരിക്കും).")

@app.on_message(filters.video | filters.document)
async def generate_link(client, message):
    # ഫയൽ ഇൻഫർമേഷൻ എടുക്കുന്നു
    file_id = message.video.file_id if message.video else message.document.file_id
    file_name = message.video.file_name if message.video else message.document.file_name
    
    # ഒരു താൽക്കാലിക മറുപടി
    msg = await message.reply_text("ലിങ്ക് തയ്യാറാക്കുന്നു... ദയവായി കാത്തിരിക്കൂ.")
    
    # ഇവിടെ നമ്മൾ ഫയൽ ഡൗൺലോഡ് ചെയ്യാതെ തന്നെ ഒരു താൽക്കാലിക ലിങ്ക് ഉണ്ടാക്കുന്നു
    # ശ്രദ്ധിക്കുക: ഇത് ടെലിഗ്രാം സെർവറിൽ നിന്നുള്ള ഡയറക്ട് ലിങ്ക് ആണ്.
    try:
        link = f"https://t.me/{client.me.username}?start={file_id}"
        await msg.edit_text(f"**ഫയൽ നാമം:** `{file_name}`\n\n**ലിങ്ക്:** {link}\n\nഈ ലിങ്ക് വഴി നിനക്ക് ഫയൽ ഷെയർ ചെയ്യാം.")
    except Exception as e:
        await msg.edit_text(f"എറർ സംഭവിച്ചു: {e}")

app.run()
