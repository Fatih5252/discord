# hey guys today i will show you how to open a ticket witch dming the bot!
# you want slash commands? here: https://github.com/Fatih5252/discord/tree/main/Commands
# you want some more ticketing system? here: https://github.com/Fatih5252/discord/tree/main/ticketing
# you want a log system? here: https://github.com/Fatih5252/discord/tree/main/Logs
import discord
from discord import app_commands, utils

class main(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)
    
    @discord.ui.button(label = "close ticket", style = discord.ButtonStyle.red, custom_id = "close")
    async def close(self, interaction, button):
        embed = discord.Embed(title = "are you sure that you want to close the ticket?", color = discord.Color.blurple())
        await interaction.response.send_message(embed = embed, view = confirm(), ephemeral = True)
      
class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False
        self.added = False
      
    async def on_ready(self):  
      await self.wait_until_ready()
      if not self.synced:
          await tree.sync(guild = discord.Object(id = SERVER ID))
          self.synced = True
     if not self.added:
          self.add(main())
      print(f"logged in as {self.user}")

intents = discord.Intents.default()
intents.message_content = True
client = aclient()
tree = app_commands.CommandTree(client)

@client.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel) and message.author != client.user:
        # Der Bot hat eine private Nachricht erhalten
        await handle_ticket(message)

async def handle_ticket(message):
    guild = client.get_guild(SERVER ID)

    if guild:
        ticket_category = discord.utils.get(guild.categories, name='Tickets')

        if not ticket_category:
            ticket_category = await guild.create_category('Tickets')
          
        ticket_channel = await ticket_category.create_text_channel(f'ticket-for-{message.author.name}-{message.author.discriminator}')
        await ticket_channel.set_permissions(message.author, read_messages=True, send_messages=True, attach_files = True, read_message_history = True)

        await ticket_channel.send(f'Hello {message.author.mention}, i created you a ticket!', view=main()
                                  
        await message.author.send(f'Hey here is your ticket: {ticket_channel.mention}!')

client.run(BOT TOKEN) 
# pls dont share your bot token to anyone!!
