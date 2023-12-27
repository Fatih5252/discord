# today i will show you how to make a dm slash command!
import discord
from discord import app_commands

intents = discord.Intents.default()
client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name="senddm", description="Sends a dm to a person.", guild=discord.Object(id = SERVER ID))
async def self(interaction: discord.Interaction, text: str, who: discord.Member):
    try:
        await who.send(f"Hello {who.name}, you have a dm from {interaction.user.name}: {text}")
        await interaction.response.send_message('Dm successfully sent!', ephemeral=True)
    except discord.Forbidden:
        await interaction.response.send_message('I can't dm this user make sure that the user have dms on!', ephemeral=True)

client.run(BOT TOKEN)
# pls dont send your BOT TOKEN to anyone!!!
