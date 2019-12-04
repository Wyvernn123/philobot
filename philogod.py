# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 00:25:20 2019

@author: alexandre
"""
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready.')

client.run('NjUxNTUzMjU2MDEwNDE2MTQw.XefP8w.8A4QVWOtGJScdWokPD5KEK7BRs0')
