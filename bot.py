# how to make a slash command (for beginners)

import discord
from discord.ext import app_commands

intents = discord.Intents.default()
client = aclient()
tree = app_commands.CommnadTree(client)

@tree.command(name = "hello", description = "say hello!", guild = discord.Object(id = SERVER ID))
async def self(interaction: discord.Interaction, name: str)
    await interaction.response.send_message(f"Hello {name}!", ephemeral = True)
  
  client.run(BOT TOKEN)
