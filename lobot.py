import discord
import config
from discord.ext import commands

intents = discord.Intents.all()

# Create an instance of the bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f'Logged in as LOBOT ({bot.user.id})')
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
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

# Command: Echo a message
@bot.command()
async def echo(ctx, *, message):
    await ctx.send(message)

# Command: Add two numbers
@bot.command()
async def add(ctx, num1: float, num2: float):
    # Calculate the sum
    result = num1 + num2

    # Send the result as a message
    await ctx.send(f'The sum of {num1} and {num2} is: {result}')

# Replace 'YOUR_TOKEN' with your Discord bot token
bot.run(config.TOKEN)
