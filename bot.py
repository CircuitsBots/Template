import discord, os, dotenv
from discord.ext import commands

dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX')

bot = commands.Bot(
    command_prefix=PREFIX,
    case_insensitive=True
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
    await ctx.send(f"Hello {ctx.message.author.mention}!")


if __name__ == '__main__':
    bot.run(TOKEN)