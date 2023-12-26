# today i will show you how to make a ticket command!
# pip install discord.py
import discord
from discord import app_commands, utils

client = aclient()
tree = app_commands.CommandTree(client)

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
          self.add_view(ticket_launcher())
          self.add_view(main())
          self.add_added = True
      print(f"logged in as {self.user}.")

class ticket_launcher(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)

    @discord.ui.button(label = "Create Ticket", style = discord.ButtonStyle.blurple, custom_id = "ticket_Button")
    async def ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        ticket = utils.get(interaction.guild.text_channels, name = f"ticket-for-{interaction.user.name}-{interaction.user.discriminator}")
        if ticket is not None: await interaction.response.send_message(f"you have already created a ticket! {ticket.mention}", ephemeral = True)
        else:
            overwrites = {
                interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages = True, attach_files = True, read_message_history = True),
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False)
            }
            try: channel = await interaction.guild.create_text_channel(name = f"ticket-for-{interaction.user.name}-{interaction.user.discriminator}", overwrites = overwrites, reason = f"ticket for {interaction.user}")
            except: return await interaction.response.send_message("channel creation failed! make sure i have the  `manage_channel` permission!", ephmeral = True)
            await channel.send(f"{interaction.user.mention} created a ticket!", view = main())
            await interaction.response.send_message(f"you created a ticket! {channel.mention}", ephemeral = True)

class main(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)
    
    @discord.ui.button(label = "close ticket", style = discord.ButtonStyle.red, custom_id = "close")
    async def close(self, interaction, button):
        embed = discord.Embed(title = "are you sure that you want to close the ticket?", color = discord.Color.blurple())
        await interaction.response.send_message(embed = embed, view = confirm(), ephemeral = True)

class confirm(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)

    @discord.ui.button(label = "confirm", style = discord.ButtonStyle.red, custom_id = "confirm")
    async def confirm_button(self, interaction, button):
        try: await interaction.channel.delete()
        except: interaction.response.send_message("i can't delete channels please make sure that i have the `manage_channel` permission!", ephemeral = True)
          
@tree.command(name = "ticket", description = "create a ticket message", guild = discord.Object(id = SERVER ID))
async def ticketing(interaction: discord.Interaction):
    embed = discord.Embed(title = "if you need help please click on the button below me!", color = discord.Colour.blue())
    await interaction.channel.send(embed = embed, view = ticket_launcher())
    await interaction.response.send_message("ticket erstellt!", ephemeral = True)    

client.run(BOT TOKEN)
# pls dont share youre bot token to anyone!
