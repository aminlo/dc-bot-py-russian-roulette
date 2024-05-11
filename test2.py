import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
#login
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
#ping
@client.command()
async def ping(ctx):
    await ctx.send(f'wah {ctx.author}, {ctx.guild}')
#kick
@client.command()
async def death(ctx):
    member = ctx.author
    await ctx.send(f'byebye {ctx.author}')
    await member.kick(reason="Kicked for using !ping command")
#mention
@client.command()
async def mention(ctx):
    #await ctx.send(f'{ctx.author.mention}')
    await ctx.send(f'<@{ctx.author.id}>')
#roll
@client.command()
async def roll(ctx):
    random_number1 = random.randint(1, 3)
    await ctx.send(f'{ctx.author.mention} , {random_number1}')
    if random_number1 != 1:
        await ctx.send(f'you survived {ctx.author.mention}')
    else:
        await ctx.author.send('womp womp')
        await ctx.author.kick(reason="L")
#log
@client.command()
async def log(ctx):
    channel = ctx.guild.get_channel(1234902841387126878)
    await channel.send('test')
#dm
@client.command()
async def dm(ctx):
    await ctx.author.send('Hello there!')
#dm2
@client.command()
async def dm2(client):
    user = await client.fetch_user(1148608568371716236)
    await user.send('Hello there!')

client.run('')

