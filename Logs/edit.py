# today i will show you basic logs!
# today is edit message!
# you want to know how to code a ticket system? here: https://github.com/Fatih5252/discord/tree/main/ticketing
# do you want more of these type of logs? here:https://github.com/Fatih5252/discord/tree/main/Logs
import discord
from discord import app_commands
from datetime import datetime

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

client = aclient()
tree = app_commands.CommandTree(client)

@client.event
async def on_message_edit(before, after):
    z = client.get_channel(CHANNEL ID)
    embed = discord.Embed(title = f"{before.author} edited a message", description = f"before: {before.content}\nafter: {after.content}\nAuthor: {before.author.mention}\nChannel: {before.channel.mention}", timestamp = datetime.now(), color = discord.Colour.blue())
    await z.send(embed = embed)

client.run(BOT TOKEN)
# pls dont share your BOT TOKEN to anyone!!!
