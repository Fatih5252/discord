# pip install discord.py
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_context = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!)
                  
bot.run(BOT TOKEN)
# pls dont share anyone your bot token!!!
# try !ping
