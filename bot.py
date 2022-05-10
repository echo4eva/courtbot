import hikari                   # discord bot library for python
import os                       # used with dotenv
from dotenv import load_dotenv  # used to hide vulnerable variables

load_dotenv()

bot = hikari.GatewayBot(token= os.getenv("TOKEN"))
bot.run()