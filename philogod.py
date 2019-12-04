# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 00:25:20 2019

@author: alexandre
"""
import discord
from discord.ext import commands
import random

Parole_de_Dieu = [f'Un trou, un manque, une absence, n’étant rien, imposent qu’on tourne autour, c’est-à-dire ce minimum de danse qui est déjà un style.',f'Le « petit a » par exemple, un peu comme le « ptyx » de Mallarmé, espèce de petit x universel, conviendra d’autant mieux qu’il n’existe pas dans la langue naturelle.',f'Le minimum alors poussé au maximum des figures dessinera plus nettement la chose qui le suscite, comme c’est l’énormité bourdonnante de l’essaim qui conduit l’oeil au faible pédoncule auquel il se trouve appendu.',f'La Musique sans les Lettres se présente comme très subtil nuage : seules, elles, une monnaie si courante.']

client = commands.Bot(command_prefix = '>')
def emote(id):
    return str(client.emojis[id])
@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def illumination(ctx):
    await ctx.send(random.choice(Parole_de_Dieu))
    await ctx.send(emote(14))


client.run('NjUxNTUzMjU2MDEwNDE2MTQw.XefJWg.QUwYTePgtWweRxmotgZQt3pHNDY')
