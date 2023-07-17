import discord
from discord.ext import commands

# Create an instance of the bot
bot = commands.Bot(command_prefix='!')

# Event: Bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

# Event: Bot receives a new message
@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself to prevent infinite loops
    if message.author == bot.user:
        return

    # Process commands
    await bot.process_commands(message)

# Command: Ping the bot
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Command: Echo a message
@bot.command()
async def echo(ctx, *, message):
    await ctx.send(message)

# Add more commands and events as needed

# Replace 'YOUR_TOKEN' with your Discord bot token
bot.run('YOUR_TOKEN')
