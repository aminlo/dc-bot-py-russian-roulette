import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def roll(ctx):
    random_number1 = random.randint(1, 3)
    await ctx.send(f'{ctx.author.mention} , {random_number1}')
    if random_number1 != 1:
        await ctx.send(f'you survived {ctx.author.mention}')
    else:
        await ctx.author.send('womp womp')
        await ctx.author.kick(reason="L")
in_game = False
player2 = None
@client.command()
async def test(ctx):
    if len(ctx.message.mentions) == 1:
        global player2
        global in_game
        in_game = True
        player2 = ctx.message.mentions[0]
        player1 = ctx.author
        await ctx.send(f'yoh {player2.name}, {player1} wants to wager their life with you. \nDo you dare accept ( do !rhelp for what this is) ? Type "yes"')
        
@client.event
async def on_message(message):
    if message.author == player2 and in_game == True:
        if message.content == "yes":
            await messsage.send(f'{player2.name} has accepted, woaahhh be ready. \n{player2.name} pick a number between 1 and 6')

client.run('')

# What will happen when you run this code?
# write roullete !help, or introduction
# ping another user or do urself, ask if ready
# other user picks number for other user, othe user roles?
# say "shoot"
# edit 1 message constant