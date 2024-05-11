import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix="!r", intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def ping(ctx):
    latency = round(client.latency * 1000) 
    await ctx.send(f'Pong! Latency: {latency}ms')

@client.command()
async def roll(ctx):
    random_number1 = random.randint(1, 3)
    await ctx.send(f'{ctx.author.mention} , {random_number1}')
    if random_number1 != 1:
        await ctx.send(f'you survived {ctx.author.mention}')
    else:
        await ctx.author.send('womp womp')
        await ctx.author.kick(reason="L")




client.run('')