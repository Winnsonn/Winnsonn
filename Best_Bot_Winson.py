# Imports
import discord
import discord.utils
import time
import random
from discord.ext import commands
from discord.utils import get
from discord import user
import asyncio
from asyncio import *
import requests
import json
from datetime import datetime
from pytz import timezone
from discord.ext.commands import clean_content
import wikipedia
import math
import aiohttp
import subprocess
import sys
from random import randint
from platform import python_version
import os
import wolframalpha
import youtube_dl  # pip install -U discord.py[voice], pip install youtube-dl, pip install --upgrade youtube-dl
""" if music command not working do the following command ^^ in shell """
import shutil
from os import system
import urllib.request
from googletrans import Translator

# start


client = commands.Bot(command_prefix= "?!")


# bot = discord.Client()
# bot = commands.Bot(command_prefix="?!")
def get_channels(client, guild):
    with open('channels.json','r') as f:
        channelss = json.load(f)

    return channelss[str(guild.id)]

# quote
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


# wikipedia
def wiki_summary(arg):
    definition = wikipedia.summary(arg,
                                   sentences=3,
                                   chars=1000,
                                   auto_suggest=False,
                                   redirect=False,
                                   )
    return definition


# events


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle,
                                 activity=discord.Streaming(name=" **?!help** to start",
                                                            url='https://discord.com/api/oauth2/authorize?client_id=762256825621807104&permissions=8&scope=bot'))
    print('Im ready and logged in {0.user}'.format(client))


#SWITCHBLOX building server only

@client.event
async def on_raw_reaction_add(payload):
    """This is the reaction role event"""
    if payload.message_id == 866258028412272660:
        guild = client.get_guild(payload.guild_id)
        channel = guild.get_channel(payload.channel_id)

        if payload.emoji.name == '❌':
            await payload.member.kick(reason=None)
        elif payload.emoji.name == '✅':
            role_name = 'Applying'
            role = await commands.RoleConverter().convert(channel, role_name)
            await payload.member.add_roles(role, reason="auto role")


# @client.event
# async def on_member_join(member):
#     channel = client.get_channel(761196644993335306)
#     embed = discord.Embed(title="A User has Joined The Server",
#                           description=f'Welcome {member} to the server',
#                           colour=discord.Colour.blue())
#     pfp = member.avatar_url
#     embed.set_image(url=pfp)
#     embed.set_footer(text="-Winson")
#     await channel.send(embed=embed)


snipe_message_content = None
snipe_message_author = None
snipe_message_id = None


@client.event
async def on_message_delete(message):
    global snipe_message_content
    global snipe_message_author
    global snipe_message_id

    snipe_message_content = message.content
    snipe_message_author = message.author.id
    snipe_message_id = message.id
    await asyncio.sleep(60)

    if message.id == snipe_message_id:
        snipe_message_author = None
        snipe_message_content = None
        snipe_message_id = None

    # single function commands

    # general id = (761196644993335306)
    # mcgeneral id = (769508180001685535)
    # @client.event
    # async def on_message(message):
    #   if ' ip' in message.content.casefold():
    #     if message.channel.id != (769508180001685535):
    #       embed992 = discord.Embed(
    #         title=("Join our MC Server"),
    #         description=("Join at:\nglobal.darkpurplemc.net"),
    #         color=discord.Colour.gold()
    #       )
    #       embed992.set_thumbnail(url="https://eu.mc-api.net/v3/server/favicon/Landicious-survival.mcnetwork.me")
    #       await message.channel.send(embed = embed992)
    #   if ' ip' in message.content.casefold():
    #     if message.channel.id == (769508180001685535):
    #       await message.channel.send("heres the invite: https://discord.gg/HaXaVCAJGy")

    # @client.listen("on_message")
    # async def on_message(ctx):
    #   if 'Server has stopped**' in ctx.content:
    #     if ctx.channel.id == (769508180001685535):
    #       try:
    #         fchannel = client.get_channel(811441560226889739)
    #         await fchannel.edit(name="Server Status: Offline")
    #       except:
    #         print("error")
    #       finally:
    #         gchannel = client.get_channel(761196644993335306)
    #         embed= discord.Embed(
    #           title= ("DarkPurple Status: Offline"),
    #           description=("Minecraft Server is now Offline"),
    #           color=discord.Colour.red()
    #         )
    #         embed.set_thumbnail(url="https://eu.mc-api.net/v3/server/favicon/Landicious-survival.mcnetwork.me")
    #         await gchannel.send(embed=embed)

    #   if 'Server has started**' in ctx.content:
    #     if ctx.channel.id == (769508180001685535):
    #       try:
    #         fchannel  = client.get_channel(811441560226889739)
    #         await fchannel.edit(name="DarkPurple Status: Online")
    #       except:
    #         print("error")
    #       finally:
    #         gchannel = client.get_channel(761196644993335306)
    #         embed = discord.Embed(
    #           title=("DarkPurple Status: Online"),
    #           description=("Minecraft Server is back ONLINE\n\nJoin at:\n"+("  ")+"global.darkpurplemc.net"),
    #           color=discord.Colour.green()
    #         )
    #         embed.set_thumbnail(url="https://eu.mc-api.net/v3/server/favicon/Landicious-survival.mcnetwork.me")
    #         await gchannel.send(embed=embed)

    await client.process_commands(message)


# the one above this is important below client.event to make Flask run client.command

# Dont process command here, because this is client.listen
# ctx is the one in the defined function

# commands
# reformation the define command

client.remove_command("help")

@client.command()
async def help(ctx):
    ownerid = '<@466528033638055936>'
    embedFIRST = discord.Embed(title="-HELP COMMAND-\n🔖Knowledge",
                               description="Commands containing about knowledge and education",
                               colour=discord.Colour.gold()
                               )
    embedFIRST.add_field(name="Commands:", value="``?!fact`` : sends facts\n``?!quote`` : sends quotes\n``?!langdetect (sentence)`` : detects what language is the sentence"
                                                 "\n``?!translate (language(from langdetect)) (sentence)`` : translates a sentence\n``?!oracle (question)`` :"
                                                 "answers almost every questions\n``?!define (question)`` : answers questions based from english wikipedia\n"
                                                 "``?!tempconvert (1st number) (Temp symbol) (2nd number)`` : converts temperatures")
    embedFIRST.set_author(name="NotARobot/NotaroBot",
                         icon_url='https://scontent.fmnl4-5.fna.fbcdn.net/v/t1.15752-9/79164084_574144910039928_5634080804029071360_n.jpg?_nc_cat=106&ccb=1-3&_nc_sid=ae9488&_nc_eui2=AeE7JwwXuci6hesiv6azd7-MX3eHdHXFj1Vfd4d0dcWPVfHWn_KCQW_5Et4k1UHO5e2Z4zkfZjQG-n7nwZbOYv-Z&_nc_ohc=vy63kNq1vVIAX9mA7IS&_nc_ht=scontent.fmnl4-5.fna&oh=97150d719bb985004a32343f56ba1dde&oe=60C092A8')

    embedSECOND = discord.Embed(title="-HELP COMMAND-\n🎲Games",
                                description="Just Fun and Games that the bot has",
                                colour=discord.Colour.gold()
                                )
    embedSECOND.add_field(name="Commands:",value="``?!8ball (question)`` : Yes or no...\n``?!tictactoe (player1) (player2)`` : play tictactoe with someone\n"
                                                 "``?!slot`` : slot machine\n``?!hothow (user)`` : tells how hot a user is\n``?!reverse (sentence)`` : spells the sentence in reverse")
    embedSECOND.set_author(name="NotARobot/NotaroBot",
                         icon_url='https://scontent.fmnl4-5.fna.fbcdn.net/v/t1.15752-9/79164084_574144910039928_5634080804029071360_n.jpg?_nc_cat=106&ccb=1-3&_nc_sid=ae9488&_nc_eui2=AeE7JwwXuci6hesiv6azd7-MX3eHdHXFj1Vfd4d0dcWPVfHWn_KCQW_5Et4k1UHO5e2Z4zkfZjQG-n7nwZbOYv-Z&_nc_ohc=vy63kNq1vVIAX9mA7IS&_nc_ht=scontent.fmnl4-5.fna&oh=97150d719bb985004a32343f56ba1dde&oe=60C092A8')


    embedTHIRD= discord.Embed(title="-HELP COMMAND-\n🛠️Moderation",
                              description="Use for informations or updates for the server",
                              colour=discord.Colour.gold()
                              )
    embedTHIRD.add_field(name="Commands:",value="``?!setreportchannel (channel)`` : sets the report command's channel\n``?!report (user) (reason)`` : reports a user to server staffs\n"
                                                "``?!userinfo (user)`` : sends the information of the user\n``?!serverinfo`` : sends the information of the server\n"
                                                "``?!snipe`` : sends the recent deleted message\n``?!purge (number)`` : deletes the amount of messages in the channel\n``?!invitebot`` : sends a discord Bot invite link ")
    embedTHIRD.set_author(name="NotARobot/NotaroBot",
                           icon_url='https://scontent.fmnl4-5.fna.fbcdn.net/v/t1.15752-9/79164084_574144910039928_5634080804029071360_n.jpg?_nc_cat=106&ccb=1-3&_nc_sid=ae9488&_nc_eui2=AeE7JwwXuci6hesiv6azd7-MX3eHdHXFj1Vfd4d0dcWPVfHWn_KCQW_5Et4k1UHO5e2Z4zkfZjQG-n7nwZbOYv-Z&_nc_ohc=vy63kNq1vVIAX9mA7IS&_nc_ht=scontent.fmnl4-5.fna&oh=97150d719bb985004a32343f56ba1dde&oe=60C092A8')

    embedMAIN = discord.Embed(title = "-HELP COMMAND-",
                            description=f"-{client.user} is a discord bot made by {ownerid}, the bot is a custom bot that can do alot of things\n\nPrefix: ?!\n\n-React to see how to use the commands:\n❌ will bring you back here\n",
                            colour=discord.Colour.gold()
               )
    embedMAIN.add_field(name="🔖Knowledge", value="-quote\n-translate\n-langdetect \n-oracle\n-define\n-tempconvert", inline=True)
    embedMAIN.add_field(name="🎲Games", value="-8ball\n-tictactoe\n-slot\n-howhot\n-reverse", inline=True)
    embedMAIN.add_field(name="🛠️Moderation", value="-setreportchannel\n-report\n-userinfo\n-serverinfo\n-snipe\n-purge\n-invitebot", inline=False)
    embedMAIN.set_author(name="NotARobot/NotaroBot",icon_url='https://scontent.fmnl4-5.fna.fbcdn.net/v/t1.15752-9/79164084_574144910039928_5634080804029071360_n.jpg?_nc_cat=106&ccb=1-3&_nc_sid=ae9488&_nc_eui2=AeE7JwwXuci6hesiv6azd7-MX3eHdHXFj1Vfd4d0dcWPVfHWn_KCQW_5Et4k1UHO5e2Z4zkfZjQG-n7nwZbOYv-Z&_nc_ohc=vy63kNq1vVIAX9mA7IS&_nc_ht=scontent.fmnl4-5.fna&oh=97150d719bb985004a32343f56ba1dde&oe=60C092A8')


    msg = await ctx.send(embed=embedMAIN)
    await msg.add_reaction( "🔖")
    await msg.add_reaction("🎲")
    await msg.add_reaction("🛠️")
    await msg.add_reaction("❌")
    valid_reactions = ["🔖","🎲","🛠️","❌"]


    def check(reaction, user):
        return (str(reaction.emoji) in valid_reactions) and (user.id != 762256825621807104) and (reaction.message.id == msg.id)
        #return (str(reaction.emoji) in valid_reactions) and (user.id == ctx.author.id) and (reaction.message.id == msg.id)

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", check=check, timeout=60)

        except asyncio.TimeoutError:
            return
        if str(reaction.emoji) == "🔖":
            await msg.edit(embed=embedFIRST)
            await msg.remove_reaction("🔖", user)
        if str(reaction.emoji) == "🎲":
            await msg.edit(embed=embedSECOND)
            await msg.remove_reaction("🎲", user)
        if str(reaction.emoji) == "🛠️":
            await msg.edit(embed=embedTHIRD)
            await msg.remove_reaction("🛠️",user)
        if str(reaction.emoji) == "❌":
            await msg.edit(embed=embedMAIN)
            await msg.remove_reaction("❌",user)

@client.command()
@commands.has_permissions(manage_channels=True, administrator=True)
async def setreportchannel(ctx, channels: discord.TextChannel):
    with open('channels.json','r') as f:
        channelss = json.load(f)

    channelss[str(ctx.guild.id)] = int(channels.id)

    with open('channels.json','w') as f:
        json.dump(channelss,f,indent=4)

    embed32 = discord.Embed(
        title='Set Report Channel',
        description=f"Report channel has been set to {channels}",
        color = discord.Colour.gold()
    )
    embed32.set_author(name="NotARobot",
                        icon_url='https://scontent.fmnl4-5.fna.fbcdn.net/v/t1.15752-9/79164084_574144910039928_5634080804029071360_n.jpg?_nc_cat=106&ccb=1-3&_nc_sid=ae9488&_nc_eui2=AeE7JwwXuci6hesiv6azd7-MX3eHdHXFj1Vfd4d0dcWPVfHWn_KCQW_5Et4k1UHO5e2Z4zkfZjQG-n7nwZbOYv-Z&_nc_ohc=vy63kNq1vVIAX9mA7IS&_nc_ht=scontent.fmnl4-5.fna&oh=97150d719bb985004a32343f56ba1dde&oe=60C092A8')

    await ctx.send(embed=embed32)

@client.command()
async def report(ctx, member:discord.Member, *, reason):
    try:
        with open('channels.json', 'r') as f:
            channelss = json.load(f)


        channel_log = ctx.guild.get_channel(channelss[str(ctx.guild.id)])
        embed33 = discord.Embed(
            title=f'{member} has been Reported',
            description=f'Reason: {reason}',
            colour=discord.Colour.lighter_grey()
        )
        embed33.set_footer(text=f"Reported by {ctx.author.name}#{ctx.author.discriminator}",
                         icon_url=ctx.author.avatar_url)
        await channel_log.send(embed=embed33)

    except:
        await ctx.send("Please set the report channel first, do ?!setreportchannel (channel)")

@client.command()
async def define(ctx, *, words):
    async with ctx.typing():
        try:
            try:
                search = discord.Embed(title="Searching for " + words,
                                       description=wiki_summary(words),
                                       color=discord.Colour.gold())
                await ctx.send(content=None, embed=search)
                print("1")
            except:
                wordss = wikipedia.suggest(words)
                search = discord.Embed(title=(f"Searching for {wordss}"),
                                       description=wiki_summary(wordss),
                                       color=discord.Colour.gold()
                                       )
                await ctx.send(content=None, embed=search)
                print("2")

        except:
            try:
                wordss = wikipedia.suggest(words)
                wordsss = wikipedia.search(wordss)
                search = discord.Embed(title="Searching for " + words,
                                       description=wiki_summary(wordsss[0]),
                                       color=discord.Colour.gold())
                await ctx.send(content=None, embed=search)
                print("3")
            except:
                try:
                    wordss = wikipedia.suggest(words)
                    search = discord.Embed(title="Searching for " + wordss,
                                           description=wiki_summary(wordss[0]),
                                           color=discord.Colour.gold())
                    await ctx.send(content=None, embed=search)
                    print("4")
                except:
                    wordss = wikipedia.search(words)
                    search = discord.Embed(title=f"Searching for {words}",
                                           description=wiki_summary(wordss[0]),
                                           color=discord.Colour.gold()
                                           )
                    await ctx.send(content=None, embed=search)
                    print("5")


@client.command()
async def snipe(message):
    if snipe_message_content == None:
        await message.channel.send("Theres nothing to snipe.")
    else:
        embed = discord.Embed(
            description= f"**<@{snipe_message_author}>**\n\n{snipe_message_content}")
        embed.set_footer(text=f"Asked by {message.author.name}#{message.author.discriminator}",
                         icon_url=message.author.avatar_url)
        embed.set_author(name="Message Sniped")
        await message.channel.send(embed=embed)
        return


@client.command(aliases = ["invite"])
async def invitebot(ctx):
    embed132 = discord.Embed(
        title="Invite me to your server: ",
        url="https://dsc.gg/notarobot",
        description="``2 types of invites``\n\n**Role with admin:** https://discord.com/api/oauth2/authorize?client_id=762256825621807104&permissions=8&scope=bot\n\n**Role without Admin:** https://discord.com/api/oauth2/authorize?client_id=762256825621807104&permissions=4294967287&scope=bot",
        colour=discord.Colour.blurple()
    )
    embed132.set_author(name="NotARobot",
                        icon_url='https://scontent.fmnl4-5.fna.fbcdn.net/v/t1.15752-9/79164084_574144910039928_5634080804029071360_n.jpg?_nc_cat=106&ccb=1-3&_nc_sid=ae9488&_nc_eui2=AeE7JwwXuci6hesiv6azd7-MX3eHdHXFj1Vfd4d0dcWPVfHWn_KCQW_5Et4k1UHO5e2Z4zkfZjQG-n7nwZbOYv-Z&_nc_ohc=vy63kNq1vVIAX9mA7IS&_nc_ht=scontent.fmnl4-5.fna&oh=97150d719bb985004a32343f56ba1dde&oe=60C092A8')
    await ctx.send(embed=embed132)


@client.command()
async def serverscount(ctx):
    await ctx.send("I'm in " + str(len(client.guilds)) + " servers!")


@client.command(aliases = ['server'])
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.lighter_grey()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)


# MATHS

@client.command()
async def solve(ctx, x, op, y):
    if op == "+":
        embed = discord.Embed(
            title=("Solved!"),
            description=("Problem: " + str(x + " + " + y + " \n") +
                         "Answer: " + str(int(x) + int(y))),
            colour=discord.Colour.green())
    elif op == "-":
        embed = discord.Embed(
            title=("Solved!"),
            description=("Problem: " + str(x + " - " + y + " \n") +
                         "Answer: " + str(int(x) - int(y))),
            colour=discord.Colour.green())
    elif op == "x" or "×":
        embed = discord.Embed(
            title=("Solved!"),
            description=("Problem: " + str(x + " x " + y + " \n") +
                         "Answer: " + str(int(x) * int(y))),
            colour=discord.Colour.green())
    elif op == "/" or "÷":
        embed = discord.Embed(
            title=("Solved!"),
            description=("Problem: " + str(x + " / " + y + " \n") +
                         "Answer: " + str(int(x) / int(y))),
            colour=discord.Colour.green())
    else:
        await ctx.send("Wrong Argument")

    await ctx.send(embed=embed)


@client.command()
async def tempconvert(ctx5, a, temp1, to, temp2):
    if temp1 == "C" and temp2 == "F":
        resultC = (int(a) * 1.8 + 32)
        await ctx5.send(str(a) + "°C = " + str(resultC) + "°F")
    elif temp1 == "C" and temp2 == "K":
        resultC = (int(a) + 273.15)
        await ctx5.send(str(a) + "°C = " + str(resultC) + "°K")
    elif temp1 == "F" and temp2 == "C":
        resultF = ((int(a) - 32) / 1.8)
        await ctx5.send(str(a) + "°F = " + str(resultF) + "°C")
    elif temp1 == "F" and temp2 == "K":
        resultF = (int(a) + 459.67)
        await ctx5.send(str(a) + "°F = " + str(resultF) + "°K")
    elif temp1 == "K" and temp2 == "C":
        resultK = (int(a) - 273.15)
        await ctx5.send(str(a) + "°K equals to " + str(resultK) + "°C")
    elif temp1 == "K" and temp2 == "F":
        resultK = (int(a) - 459.67)
        await ctx5.send(str(a) + "°K equals to " + str(resultK) + "°F")


@client.command()
async def math_sin(ctx, number):
    answer = math.sin(int(number))
    await ctx.send(f"sin for {number} is {answer}")


@client.command()
async def math_cos(ctx, number):
    answer = math.cos(int(number))
    await ctx.send(f"cos for {number} is {answer}")


@client.command()
async def math_tan(ctx, number):
    answer = math.tan(int(number))
    await ctx.send(f"tan for {number} is {answer}")


@client.command()
async def math_pow(ctx, number, numberr):
    answer = math.pow(int(number), int(numberr))
    await ctx.send(f"Answer: {answer}")


# informations

@client.command(aliases=['8ball'])
async def _8ball(ctx6, *, question):
    responses = [
        "Yes", "it is certain", "definitely", "pretty sure", "Mostly yes",
        "Most Likely", "No", "Probably not", "Surely Yes", "Maybe not",
        "My rely is no", "Mostly No", "Sorry but no", "Never"
    ]
    embed2 = discord.Embed(
        title="",
        description=(
            f'Question: {question}\nAnswer: {random.choice(responses)}'),
        color=discord.Colour.blue())
    await ctx6.send(embed=embed2)


@client.command()
async def say(ctx14, *, messages):
    if ctx14.author.id == 466528033638055936:
        await ctx14.message.delete()
        await ctx14.send("{}".format(messages))


@client.command(aliases=['wolframalpha', 'wa'])
async def oracle(ctx, *, args):
    async with ctx.typing():
        app_id = "T7PAG4-5TQ3W8JGKW"
        clientss = wolframalpha.Client(app_id)
        res = clientss.query(args)
        answer = (next(res.results).text)
        embed2322 = discord.Embed(
            title="",
            description=f"**Question:** {args}\n**Answer:** {answer}",
            color=discord.Colour.gold()
        )
        embed2322.set_author(name="NotARobot",
                             icon_url='https://scontent.fmnl4-5.fna.fbcdn.net/v/t1.15752-9/79164084_574144910039928_5634080804029071360_n.jpg?_nc_cat=106&ccb=1-3&_nc_sid=ae9488&_nc_eui2=AeE7JwwXuci6hesiv6azd7-MX3eHdHXFj1Vfd4d0dcWPVfHWn_KCQW_5Et4k1UHO5e2Z4zkfZjQG-n7nwZbOYv-Z&_nc_ohc=vy63kNq1vVIAX9mA7IS&_nc_ht=scontent.fmnl4-5.fna&oh=97150d719bb985004a32343f56ba1dde&oe=60C092A8')
        await ctx.send(embed=embed2322)


@client.command(aliases=["howhot", "hot"])
async def hotcalc(ctx, *, user: discord.Member = None):
    """ Returns a random percent for how hot is a discord user """
    user = user or ctx.author

    random.seed(user.id)
    r = random.randint(1, 100)
    hot = r / 1.17

    if hot > 25:
        emoji = "❤"
    elif hot > 50:
        emoji = "💖"
    elif hot > 75:
        emoji = "💞"
    else:
        emoji = "💔"

    await ctx.send(f"**{user.name}** is **{hot:.2f}%** hot {emoji}")


@client.command()
async def reverse(ctx, *, text: str):
    """ !poow ,ffuts esreveR
    Everything you type after reverse will of course, be reversed
    """
    t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
    await ctx.send(f"🔁 {t_rev}")


@client.command(aliases=["slots", "bet"])
async def slot(ctx):
    """ Roll the slot machine """
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)

    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

    if (a == b == c):
        await ctx.send(f"{slotmachine} All matching, you won! 🎉")
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
    else:
        await ctx.send(f"{slotmachine} No match, you lost 😢")


@client.command(aliases=['test', 'restart'])
async def refresh(ctx):
    if ctx.author.id == 466528033638055936:
        msg2 = await ctx.channel.send("Refreshing commands...")
        await asyncio.sleep(2)
        await msg2.edit(content="Testing Client events...")
        await asyncio.sleep(2)
        await msg2.edit(content="Setting up events...")
        await asyncio.sleep(2)
        await msg2.edit(content="Refreshing Commands")
        await asyncio.sleep(2)
        await msg2.edit(content="Refreshing Winson's Bots....")
        await asyncio.sleep(2)
        await msg2.edit(content="Restarting DiscordBot")
        await asyncio.sleep(2)
        await msg2.edit(content="Discord Bot has been refreshed")
    elif ctx.author.id != 466528033638055936:
        msg2 = await ctx.channel.send("refreshing-")
        await asyncio.sleep(1)
        await msg2.edit(content="wait-...")
        await asyncio.sleep(2)
        await msg2.edit(content="You aren't Winson idiot! -_-")



@client.command()
async def quote(ctx):
    quote = get_quote()
    embed11 = discord.Embed(title="Quote Generated",
                            description=quote,
                            color=discord.Color.gold())
    await ctx.channel.send(embed=embed11)


# @client.command()
# async def discordinv(ctx):
#   await ctx.channel.send("heres the invite: https://discord.gg/HaXaVCAJGy")


# tictactoe
player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                     [2, 5, 8], [0, 4, 8], [2, 4, 6]]


@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:"
        ]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
            await ctx.send("use ``?!place (number)``\ndo ``?!game_end`` to end the game")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
            await ctx.send("use ``?!place (number)``\ndo ``?!game_end`` to end the game")
    else:
        await ctx.send(
            "A game is already in progress! Finish it before starting a new one."
        )


@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send(
                    "Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile."
                )
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the ?!tictactoe command."
                       )


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[
            condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True


@client.command()
async def game_end(ctx):
    global gameOver
    gameOver = True
    await ctx.send("Game has been stopped")


@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send(
            "Please make sure to mention/ping players (ie. <@688534433879556134>)."
        )


@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")


# MORE APIs COMMAND

@client.command()
async def translate(ctx, langto, *, sentence):
    translator = Translator()
    output = translator.translate(sentence, dest=(langto))
    embed465 = discord.Embed(
        title="Translated",
        description=f"**Input**: {sentence}\n**Output**: {output.text}",
        color=discord.Colour.light_grey()
    )
    embed465.set_author(name="NotARobot",
                        icon_url='https://scontent.fmnl4-5.fna.fbcdn.net/v/t1.15752-9/79164084_574144910039928_5634080804029071360_n.jpg?_nc_cat=106&ccb=1-3&_nc_sid=ae9488&_nc_eui2=AeE7JwwXuci6hesiv6azd7-MX3eHdHXFj1Vfd4d0dcWPVfHWn_KCQW_5Et4k1UHO5e2Z4zkfZjQG-n7nwZbOYv-Z&_nc_ohc=vy63kNq1vVIAX9mA7IS&_nc_ht=scontent.fmnl4-5.fna&oh=97150d719bb985004a32343f56ba1dde&oe=60C092A8')
    await ctx.send(embed=embed465)


@client.command()
async def langdetect(ctx, *, sentence):
    translator = Translator()
    output = translator.detect(sentence)
    await ctx.send(output)


@client.command(aliases=['user','userinfo'])
async def info(ctx, user: discord.Member):
    """Gets info on a member, such as their ID."""
    try:
        embed = discord.Embed(title="User profile: " + user.name, colour=user.colour)
        embed.add_field(name="Name:", value=user.name)
        embed.add_field(name="ID:", value=user.id)
        embed.add_field(name="Status:", value=user.status)
        embed.add_field(name="Highest role:", value=user.top_role)
        embed.add_field(name="Joined:", value=user.joined_at)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)
    except:
         pass


@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit: int):
    await ctx.message.delete()
    await asyncio.sleep(1)
    await ctx.channel.purge(limit=limit)
    purge_embed = discord.Embed(title='Purge [!purge]',
                                description=f'Successfully purged {limit} messages. \n Command executed by {ctx.author}.',
                                color=discord.Colour.random())
    purge_embed.set_footer(text=str(datetime.datetime.now()))
    await ctx.channel.send(embed=purge_embed, delete_after=True)


# facts
@client.command()
async def datefact(ctx):
    url = "https://numbersapi.p.rapidapi.com/6/21/date"

    querystring = {"fragment": "true", "json": "true"}

    headers = {
        'x-rapidapi-key': "77fb564b77mshd53aa6fc524730ap13fd4ajsnf4eca3d67a94",
        'x-rapidapi-host': "numbersapi.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    embed6637 = discord.Embed(title="Did you know?",
                              description=(response.text),
                              color=discord.Colour.blurple())
    await ctx.send(embed=embed6637)


@client.command()
async def fact(ctx):
    url = "https://numbersapi.p.rapidapi.com/random/trivia"

    querystring = {
        "max": "20",
        "fragment": "true",
        "min": "10",
        "json": "true"
    }

    headers = {
        'x-rapidapi-key': "77fb564b77mshd53aa6fc524730ap13fd4ajsnf4eca3d67a94",
        'x-rapidapi-host': "numbersapi.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    embed6637 = discord.Embed(title="Did you know?",
                              description=(response.text),
                              color=discord.Colour.blurple())
    await ctx.send(embed=embed6637)


@client.command()
async def mathfact(ctx):
    url = "https://numbersapi.p.rapidapi.com/1729/math"

    querystring = {"fragment": "true", "json": "true"}

    headers = {
        'x-rapidapi-key': "77fb564b77mshd53aa6fc524730ap13fd4ajsnf4eca3d67a94",
        'x-rapidapi-host': "numbersapi.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    embed6637 = discord.Embed(title="Did you know?",
                              description=(response.text),
                              color=discord.Colour.blurple())
    await ctx.send(embed=embed6637)


@client.command()
async def triviafact(ctx):
    url = "https://numbersapi.p.rapidapi.com/42/trivia"

    querystring = {"fragment": "true", "notfound": "floor", "json": "true"}

    headers = {
        'x-rapidapi-key': "77fb564b77mshd53aa6fc524730ap13fd4ajsnf4eca3d67a94",
        'x-rapidapi-host': "numbersapi.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    embed6637 = discord.Embed(title="Did you know?",
                              description=(response.text),
                              color=discord.Colour.blurple())
    await ctx.send(embed=embed6637)


# vc
@client.command(pass_context=True)
async def join(ctx):
    try:
        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

            await voice.disconnect()

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
            print(f"The bot has connected to {channel}\n")

        await ctx.send(f"Joined {channel}")
    except:
        pass


@client.command(pass_context=True)
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        await ctx.send(f"Left {channel}")
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("Don't think I am in a voice channel")



client.run(TOKEN)
