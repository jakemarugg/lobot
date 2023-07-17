import requests
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

# Command: Check if a number is a palindrome
@bot.command()
async def is_palindrome(ctx, x: int):
    # Convert the number to a string
    str_x = str(x)

    # Check if the string is equal to its reverse
    is_palindrome = str_x == str_x[::-1]

    # Send the result as a message
    await ctx.send(f'{x} is a palindrome: {is_palindrome}')

# Command: Find all permutations of an array
@bot.command()
async def permutations(ctx, *numbers: int):
    # Check if the number of elements in the array is valid
    if len(numbers) > 6:
        await ctx.send("The array should have at most 6 elements.")
        return

    # Generate all permutations
    perms = generate_permutations(numbers)

    # Send the permutations as a message
    await ctx.send(f"All permutations:\n{perms}")

# Function to generate all permutations recursively
def generate_permutations(numbers):
    if len(numbers) <= 1:
        return [list(numbers)]

    all_perms = []
    for i in range(len(numbers)):
        curr_num = numbers[i]
        remaining_nums = numbers[:i] + numbers[i+1:]
        perms = generate_permutations(remaining_nums)

        for perm in perms:
            all_perms.append([curr_num] + perm)

    return all_perms

# Command: Get NASA's Astronomy Picture of the Day
@bot.command()
async def apod(ctx):
    # Send a request to the APOD API
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': 'DEMO_KEY'} 
    response = requests.get(url, params=params)
    data = response.json()

    # Extract the image URL and description from the API response
    image_url = data['url']
    description = data['explanation']

    # Create an embed and set the image and description
    embed = discord.Embed()
    embed.set_image(url=image_url)
    embed.description = description

    # Send the embed as a message
    await ctx.send(embed=embed)

# Replace 'YOUR_TOKEN' with your Discord bot token
bot.run(config.TOKEN)
