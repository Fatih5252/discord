# how to make a slash command (for beginners)
# pip install discord.py
# pls dont share youre discord token to anyone!! 
# you want a prefix command? here: https://github.com/Fatih5252/discord/blob/main/Commands/prefix.py
import discord
from discord import app_commands

intents = discord.Intents.default()
client = aclient()
tree = app_commands.CommnadTree(client)

@tree.command(name = "hello", description = "say hello!", guild = discord.Object(id = SERVER ID))
async def self(interaction: discord.Interaction, name: str)
    await interaction.response.send_message(f"Hello {name}!", ephemeral = True)
  
client.run(BOT TOKEN)

# ephemeral = True = only you can see the message
# ephemeral = False = everyone can see the message
