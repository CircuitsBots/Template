import discord, os, dotenv
from discord.ext import commands

dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX')

bot = commands.Bot(
    command_prefix=PREFIX,
    case_insensitive=True,
    intents=discord.Intents.all() # intents are needed after dpy 1.5 update to use guild or presence
)


# Events
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} in {len(bot.guilds)} guilds!")


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await bot.process_commands(message)


# Commands. Should eventually start using cogs, but this is good for now
@bot.command(
    name='hello', aliases=['hi'],
    brief='Make the bot say "Hello', # Quick description of command
    description='Make the bot say "Hello"' # Long description of command
)
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")


if __name__ == '__main__':
    bot.run(TOKEN)
