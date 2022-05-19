import hikari                   # discord bot library for python
import lightbulb                # command handler for hikari
import os                       # used with dotenv
from dotenv import load_dotenv  # used to hide vulnerable variables

load_dotenv()

bot = lightbulb.BotApp(
    token= os.getenv("TOKEN"), 
    default_enabled_guilds= (int(os.getenv("GUILD_ID"))),
    prefix= "~"
)

@bot.command
@lightbulb.command(name="testprefix", description="testing prefix")
@lightbulb.implements(lightbulb.PrefixCommand)
async def testing(ctx):
    await ctx.respond(f"this prefix rocks!")

@bot.command
@lightbulb.command(name="court", description="Go to court with someone")
@lightbulb.implements(lightbulb.PrefixCommand)
async def accuse(ctx: lightbulb.PrefixContext):
    # Get the command length
    command_length = len("~court") + 1
    # Get the whole content of the message
    msg = ctx.event.content
    # Slice the message to only contain the user who was mentioned and the reason going to court
    msg = msg[command_length : len(msg)]
    # Get the user ID of who was mentioned
    mentioned_user = msg.split()[0]
    # Get the length of the mentioned user format so we can get the starting index of the reason going to court
    mentioned_user_format_length = len(mentioned_user) + 1
    # Get the reason by itself
    reason = msg[mentioned_user_format_length : len(msg)]
    # Get the mentioned user's ID by itself
    mentioned_user = mentioned_user[2: len(mentioned_user) - 1]

    # Debugging purposes
    print(msg)
    print(mentioned_user)
    print(reason)

    await ctx.respond(f'The ID of the mentioned user: **{mentioned_user}**\
        \nThe reason being accused: **{reason}**')

    await ctx.respond(f'Please provide evidence of a screenshot')
    
    
# Bot passive until event happens just using hikari
@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print('USER: ', event.author, 'MSG: ', event.content, 'MSG ID: ', event.message_id)

# Bot command using lightbulb
@bot.command
@lightbulb.command(name= 'ping', description= 'pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('pong!')

# Group commands using lightbulb
@bot.command
@lightbulb.command('group', 'this is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass

# Sub command using lightbulb
@my_group.child
@lightbulb.command('subcommand', 'this is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('pog')

# Slash commands and options using lightbulb
@bot.command
@lightbulb.option('reason', 'why user go to court', type= str)
@lightbulb.option('user', 'user to go to court against', type= str)
@lightbulb.command('test', 'testing options')
@lightbulb.implements(lightbulb.SlashCommand)
async def court(ctx):
    await ctx.respond(f"{ctx.options.user}, has been accused because, {ctx.options.reason}.")

bot.run()