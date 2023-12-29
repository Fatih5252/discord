# hey guys im back!!
# today i will show you how to make a verify button
# want a ticket system? here: https://github.com/Fatih5252/discord/tree/main/ticketing
# want some more commands like this? here: https://github.com/Fatih5252/discord/tree/main/Commands
# want a log system? here: https://github.com/Fatih5252/discord/tree/main/Logs
import discord
from discord import app_commands

class button_view(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)
        
  @discord.ui.button(label = "verify", style = discord.ButtonStyle.green, custom_id = "verify")
    async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):
        if type(client.role) is not discord.Role:
            client.role = interaction.guild.get_role(ROLE ID)
        if client.role not in interaction.user.roles:
            await interaction.user.add_roles(client.role)
            await interaction.response.send_message(f"Succesfully added the role {interaction.role.mention}!", ephemeral = True)
        else: await interaction.response.send_message(f"you have already the {interaction.role.mention}!!", ephemeral = True)

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False
        self.role = ROLE ID
        self.added = False
      
    async def on_ready(self):  
      await self.wait_until_ready()
      if not self.synced:
          await tree.sync(guild = discord.Object(id = SERVER ID))
          self.synced = True
      if not self.added:
          self.add_view(button_view())
          self.add_added = True
      print(f"logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = "verify", description = "verify button", guild = discord.Object(id = 1101408474631507998))
async def button(interaction: discord.Interaction):
    await interaction.response.send_message("success!", ephemeral = True)
    embed = discord.Embed(title = "accept the rules!", description = "press the button below this message to verify yourself!!", color = discord.Colour.green())
    await interaction.channel.send(embed = embed, view = button_view())

client.run(BOT TOKEN)
# PLS DONT SHARE YOUR BOT TOKEN TO ANYONE!!!
