import os
from telethon import TelegramClient, events
from functions import save_message, get_credentials, create_config, query_yes_no

if os.path.exists('config.py'):
    use_saved_data = query_yes_no('Use saved user data?', 'yes')

if not os.path.exists('config.py') or not use_saved_data:
    user_data = get_credentials()
    create_config(user_data)

from config import verbose, api_name, api_id, api_hash, chat_name, commands_chat

client = TelegramClient(api_name, api_id, api_hash)

@client.on(events.NewMessage(chats=chat_name))
async def my_event_handler(event):
    if verbose:
        print('new message arrived:', event.message.message)
    save_message(event.message.message)

@client.on(events.NewMessage(chats=commands_chat))
async def get_all_messages(event):
    if 'get_messages' in event.raw_text:
        print('gathering messages...')
        async for message in client.iter_messages('crp_signals', 100):
            print(message.date)
            save_message(str(message.date), 'last_messages.txt')
            save_message(message.message, 'last_messages.txt')

client.start()
client.run_until_disconnected()
