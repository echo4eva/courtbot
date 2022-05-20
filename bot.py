import asyncio
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

# @bot.command
# @lightbulb.command(name="testprefix", description="testing prefix")
# @lightbulb.implements(lightbulb.PrefixCommand)
# async def testing(ctx):
#     await ctx.respond(f"this prefix rocks!")

@bot.command
@lightbulb.command(name="court", description="Go to court with someone")
@lightbulb.implements(lightbulb.PrefixCommand)
async def accuse(ctx: lightbulb.PrefixContext):
    command_author = ctx.event.author
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
    # print(msg)
    # print(mentioned_user)
    # print(reason)
    print(command_author)

    await ctx.respond(f'The ID of the mentioned user: **{mentioned_user}**\
        \nThe reason being accused: **{reason}**')

    await ctx.respond(f'Please provide evidence of a screenshot')

    try:
        # Waits for a response or message from the user.
        response_event = await ctx.app.wait_for(
            hikari.GuildMessageCreateEvent, 
            timeout= 30, 
            predicate= lambda x: x.message.author == command_author
            )

        # Code stole from `def evidence`
        attachment = response_event.message.attachments
        if len(attachment) == 0:
            await ctx.respond("There's no attatchment!")
        else:
            attachment_string = str(attachment)
            extracted_url = attachment_string.partition("url=")[2].split(",")[0].replace("'", "")
            await ctx.respond(extracted_url)
    except asyncio.TimeoutError:
        await ctx.respond("Something went wrong")




@bot.command
@lightbulb.command(name="evidence", description="Adds evidence to the court")
@lightbulb.implements(lightbulb.PrefixCommand)
async def evidence(ctx: lightbulb.PrefixContext):
    # TODO: find better way to get URL from attachment
    # Gets attachment from the messagel
    attachment = ctx.event.message.attachments
    # Checks if there's an attachment
    # an empty attachment displays as []
    if len(attachment) == 0:
        await ctx.respond("There's no attatchment!")
    else:
        # The attachment comes as "Sequence[Attachment]", but not sure how to go through it
        # as it only has one element in the list. When print, it says a lot of data including url, filename,
        # but can only access the filename in the list as it has 1 element in it?
        # So turned into a string, lol
        attachment_string = str(attachment)
        # Slice up to the point where we can get the URL
        extracted_url = attachment_string.partition("url=")[2].split(",")[0].replace("'", "")
        # Sends the URL in the chat
        await ctx.respond(extracted_url)
        
        

    
    
# # Bot passive until event happens just using hikari
# @bot.listen(hikari.GuildMessageCreateEvent)
# async def print_message(event):
#     print('USER: ', event.author, 'MSG: ', event.content, 'MSG ID: ', event.message_id)
#     print(event.message.attachments) # able to get whatever attachment from the message

# # Bot command using lightbulb
# @bot.command
# @lightbulb.command(name= 'ping', description= 'pong')
# @lightbulb.implements(lightbulb.SlashCommand)
# async def ping(ctx):
#     await ctx.respond('pong!')

# # Group commands using lightbulb
# @bot.command
# @lightbulb.command('group', 'this is a group')
# @lightbulb.implements(lightbulb.SlashCommandGroup)
# async def my_group(ctx):
#     pass

# # Sub command using lightbulb
# @my_group.child
# @lightbulb.command('subcommand', 'this is a subcommand')
# @lightbulb.implements(lightbulb.SlashSubCommand)
# async def subcommand(ctx):
#     await ctx.respond('pog')

# # Slash commands and options using lightbulb
# @bot.command
# @lightbulb.option('reason', 'why user go to court', type= str)
# @lightbulb.option('user', 'user to go to court against', type= str)
# @lightbulb.command('test', 'testing options')
# @lightbulb.implements(lightbulb.SlashCommand)
# async def court(ctx):
#     await ctx.respond(f"{ctx.options.user}, has been accused because, {ctx.options.reason}.")

bot.run()