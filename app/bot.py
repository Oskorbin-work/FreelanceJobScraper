from telethon import TelegramClient, events
from config import api_id,api_hash, bot_token
from logs.logger import create_logs

# Create the client and connect
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# create logs
logger = create_logs()

# Handler for the /start command
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Привет, это бот для поиска вакансий и фриланса!')
    logger.info(f'Начала команды {event.sender_id}')

# Start the client
client.start()
client.run_until_disconnected()