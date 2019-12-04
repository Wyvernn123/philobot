# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 00:25:20 2019

@author: alexandre
"""
import discord

client = discord.ext.commands.Bot(command_prefix = '>')

@client.event
async def on_ready():
    print('Bot is ready.')

client.run('NjUxNTUzMjU2MDEwNDE2MTQw.XefKjw.9lgWbpNQC5byTbuoP_vciZqt3Ps')
