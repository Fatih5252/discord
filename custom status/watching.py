# hello today i will show you how to make custom status!
# you want a ticketing system? here: https://github.com/Fatih5252/discord/tree/main/ticketing
# you want a log system? here: https://github.com/Fatih5252/discord/tree/main/Logs
# you want more of this custom status? here: https://github.com/Fatih5252/discord/tree/main/custom%20status
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
tree = app_commands.CommandTree(client)

@client.event
async def on_ready()
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "TEXT"))

client.run(BOT TOKEN)
# PLS DONT SHARE YOUR BOT TOKEN TO ANYONE!!!!!