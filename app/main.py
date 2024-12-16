from telethon import TelegramClient, sync, events
import os
import dotenv

dotenv.load_dotenv()
api_id_catcher = os.getenv('API_ID_FIRST')
api_hash_catcher = os.getenv('API_HASH_FIRST')
api_id_ender = os.getenv('API_ID_SECOND')
api_hash_ender = os.getenv('API_HASH_SECOND')


catcher = TelegramClient('catcher', api_id_catcher, api_hash_catcher)
ender = TelegramClient('ender', api_id_ender, api_hash_ender)



@ender.on(events.NewMessage())
async def handler(event):
      await event.reply("Hello, World!")


catcher.start()
ender.start()
ender.run_until_disconnected()
