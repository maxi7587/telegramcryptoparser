import os
from telethon import TelegramClient, events
from functions import save_message, get_credentials, create_config, query_yes_no

if os.path.exists('config.py'):
    override_config = query_yes_no('Use saved user data?', 'yes')

if not os.path.exists('config.py') or not override_config:
    user_data = get_credentials()
    create_config(user_data)

from config import verbose, api_name, api_id, api_hash, chat_name

client = TelegramClient(api_name, api_id, api_hash)

@client.on(events.NewMessage(chats=chat_name))
async def my_event_handler(event):
    if verbose:
        print('new message arrived:', event.message.message)
    save_message(event.message.message)

client.start()
client.run_until_disconnected()
