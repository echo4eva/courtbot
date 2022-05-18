import hikari                   # discord bot library for python
import os                       # used with dotenv
from dotenv import load_dotenv  # used to hide vulnerable variables

load_dotenv()

bot = hikari.GatewayBot(token= os.getenv("TOKEN"))

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print('USER: ', event.author, 'MSG: ', event.content, 'MSG ID: ', event.message_id)

bot.run()