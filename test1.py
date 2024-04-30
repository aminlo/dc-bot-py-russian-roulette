import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('wah'):
        await message.channel.send('oh')

async def on_member_join(member):
        guild = member.guild
        await message.channel.send(f'{guild_name}')

async def on_member_update(before, after):
     await message.channel.send(f'{before} -> {after}')
     print("s")

client.run('')