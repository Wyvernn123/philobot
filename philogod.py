# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 00:25:20 2019

@author: alexandre
"""
import discord
import os
from discord.ext import commands
import numpy

Sagesse_infini = open("Parole de Dieu.txt",'r')
Parole_de_Dieu = []
for Infime_partie in Sagesse_infini:
    Citation = Infime_partie.strip()
    Parole_de_Dieu.append(Citation)

client = commands.Bot(command_prefix = '>')
def emote(id):
    return str(client.emojis[id])
@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def illumination(ctx):
    await ctx.send(numpy.random.choice(Parole_de_Dieu), tts=True)
    await ctx.send(emote(14))


client.run(os.environ['DISCORD_TOKEN'])
