from telethon import TelegramClient, events, sync
from config import api_id,api_hash, bot_token
import logging


logging.basicConfig(level=logging.INFO)


# Create the client and connect
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Handler for the /start command
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hello! I am a Telethon bot. How can I assist you today?')
    logging.info(f'Start command received from {event.sender_id}')


# Keyword-based response handler
@client.on(events.NewMessage)
async def keyword_responder(event):
    message = event.text.lower()
    print(message)

    responses = {
        'hello': 'Hi there! How can I help you today?',
        '/start': ""
    }

    response = responses.get(message, None)

    if response or response =="":
        await event.respond(response)
    else:
        # Default response
        default_response = (
            "I didn't understand that command. Here are some commands you can try:\n"
            "/start - Start the bot\n"
        )
        await event.respond(default_response)
        logging.warning(f'Warn response {response}')
    logging.info(f'Message received from {event.sender_id}: {event.text}')

# Start the client
client.start()
client.run_until_disconnected()