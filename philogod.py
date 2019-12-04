# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 00:25:20 2019

@author: alexandre
"""
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready.')

client.run(os.environ['DISCORD_TOKEN'])
