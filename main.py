import discord
from discord.ext import commands
from random import choice
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)



@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def mem(ctx):

    random_image = choice(os.listdir('images'))

    with open(f"images/{random_image}", "rb") as image:
       picture =  discord.File(image)

    await ctx.send(file = picture)


bot.run('')



