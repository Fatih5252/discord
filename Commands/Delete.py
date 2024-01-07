# hello today i will show you how to make a delete command!
# you want a ticketing system? here: https://github.com/Fatih5252/discord/tree/main/ticketing
# you want a log system? here: https://github.com/Fatih5252/discord/tree/main/Logs
# you want custom status for your bot? here: https://github.com/Fatih5252/discord/tree/main/custom%20status
# you wan more commands? here: https://github.com/Fatih5252/discord/tree/main/Commands
import discord
from discord import app_commands

class aclient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents = intents)
        self.synced = False
        self.added = False
    async def on_ready(self):  
      await self.wait_until_ready()

      if not self.synced:
          await tree.sync(guild = discord.Object(id = SERVER ID))
          self.synced = True
      if not self.added:
          self.add_added = True
      print(f"logged in as {self.user}.")

client = aclient
tree = discord.Object.CommandTree(client)

@tree.command(name = "delete", description = "delete messages", guild = discord.Object(id = SERVER ID))
async def self(interaction: discord.Interaction, Number: int):
    await interaction.channel.purge(limit = Number)
    await interaction.response.send_message(f"You deleted succesfully {Number} message(s)", ephemeral = True)

client.run(BOT TOKEN)
# PLS DONT SHARE YOUR BOT TOKEN TO ANYONE!!!!