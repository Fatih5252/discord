import discord, os
from discord.ext import commands
from discord import app_commands, utils
import asyncio
from datetime import datetime

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
            await interaction.response.send_message(f"you created a ticket! {channel.mention}", ephemeral = True)@discord.ui.button(label = "Create Ticket", style = discord.ButtonStyle.blurple, custom_id = "ticket_Button")
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

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False
        self.added = False
      
    async def on_ready(self):  
      await self.wait_until_ready()
      if not self.synced:
          await tree.sync(guild = discord.Object(id = 1170114856859488307))
          self.synced = True
      if not self.added:
          self.add_view(ticket_launcher())
          self.add_view(main())
      print(f"logged in as {self.user}")

intents = discord.Intents.default()
intents.message_content = True
client = aclient()
tree = app_commands.CommandTree(client)
          
@tree.command(name = "ticket", description = "create a ticket message", guild = discord.Object(id = 1170114856859488307))
async def ticketing(interaction: discord.Interaction):
    embed = discord.Embed(title = "if you need help please click on the button below me!", color = discord.Colour.blue())
    await interaction.channel.send(embed = embed, view = ticket_launcher())
    await interaction.response.send_message("ticket created!", ephemeral = True)

@tree.command(name = "ping", description = "pinki pinki ponkiiii", guild = discord.Object(id = 1170114856859488307))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message("pong!", ephemeral = True)

@tree.command(name = "dm", description = "dm a user", guild = discord.Object(id = 1170114856859488307))
async def self(interaction: discord.Interaction, wer: discord.Member, text: str):
    try:
        await wer.send(f"Hallo {wer.name} du hast ein dm von {interaction.user.name}: {text}")
        await interaction.response.send_message("DM wurde erfolgreich gesendet!", ephemeral = True)
    except discord.Forbidden:
        await interaction.response.send_message("ich kann leider diesem user kein DM senden bitte frag dem user ob er DMs offen hat!", ephemeral = True)

@client.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel) and message.author != client.user:
        # Der Bot hat eine private Nachricht erhalten
        await handle_ticket(message)

async def handle_ticket(message):
    guild = client.get_guild(1170114856859488307)  # Deine Server-ID hier einsetzen

    if guild:
        ticket_category = discord.utils.get(guild.categories, name='Tickets')

        if not ticket_category:
            # Wenn die Kategorie nicht existiert, erstelle sie
            ticket_category = await guild.create_category('Tickets')

        # Erstelle einen neuen Textkanal im Ticket-Format
        ticket_channel = await ticket_category.create_text_channel(f'ticket-für-{message.author.name}')
        await ticket_channel.set_permissions(message.author, read_messages=True, send_messages=True)

        # Sende eine Begrüßungsnachricht im Ticket-Kanal
        await ticket_channel.send(f'Hallo {message.author.mention}, dein Ticket wurde erstellt. Ein Teammitglied wird sich bald bei dir melden.', view=main())

        # Sende eine Nachricht im privaten Chat, um den Benutzer über das Ticket zu informieren
        await message.author.send(f'Dein Ticket wurde erfolgreich erstellt! Du kannst es hier finden: {ticket_channel.mention}')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="DM FOR HELP", url="https://twitch.tv/fatihsimsek52"))

@client.event
async def on_message_delete(message):
    z = client.get_channel(1170114857857732682)
    embed = discord.Embed(title = f"{message.author}s nachricht wurde gelöscht!", description = f"gelöschtes nachricht: {message.content}\nAutor: {message.author.mention}\nChannel: {message.channel.mention}", timestamp = datetime.now(), color = discord.Colour.red())
    await z.send(embed = embed)
client.run('MTE5MTEzODg4NDQ2MjA1MTQzMA.GRol09.6tifhic7uIhF3k6Zyvx5KpVO6uOmaCH3DWtG3g')