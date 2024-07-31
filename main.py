import discord
from discord.ext import commands
from random import choice
from random import randint
import os
import requests

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


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']




@bot.command('duck')
async def duck(ctx):
    number_random = randint(0, 100)

    if number_random > 30:
        image_url = get_duck_image_url()
        await ctx.send(image_url)
    else:
        random_image2 = choice(os.listdir('images'))

        with open(f"images/{random_image2}", "rb") as image2:
            picture2 =  discord.File(image2)

        await ctx.send(file = picture2)  
        await ctx.send("Ты нашёл секретикккк :)))))")

        
bot.run('')



