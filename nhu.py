#bot by Aalpha007

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random

ins=["You're as useless as the 'ueue' in 'queue'","Mirrors can't talk. Lucky for you, they can't laugh either","If I had a face like yours, I'd sue my parents."]
fu=["cactus","broom","dog","cat","donkey"]    
bot = commands.Bot(command_prefix='!!')

@bot.event
async def on_ready():
    print("Ready when you are")
    print("I am running on ", bot.user.name)
    print("with the ID: {}".format(bot.user.id))

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send(":ping_pong: ping!! xSSS")
    print("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed=discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role, inline=True)
    embed.add_field(name="Joined", value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    print(user.avatar_url)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed=discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0xff0000)
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members), inline=True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    print(ctx.message.server.icon_url)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def insult(ctx, user:discord.Member):
    i=random.randint(0,len(ins))
    await ctx.send("{} insults {} \n {}".format(ctx.author.mention, user.mention,ins[i]))

@bot.command(pass_context=True)
async def fuck(ctx, user:discord.Member):
    i=random.randint(0,len(fu))
    await ctx.send("{} gets fucked by {}".format(user.mention,fu[i]))

bot.run("Your Auth-token")

