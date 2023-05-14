from discord.ext import commands
import discord
import json
import requests
from colorama import *
import random

with open("config.json", "r") as confjson:
        configData = json.load(confjson)

token = configData["Token"]
prefix = configData["Prefix"]

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = commands.when_mentioned_or(prefix), help_command = None, intents=intents)


async def random_color():
    number_lol = random.randint(1, 999999)

    while len(str(number_lol)) != 6:
        number_lol = int(str(f'{random.randint(1, 9)}{number_lol}'))

    return number_lol

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type = discord.ActivityType.playing, name = "Playing with numbers"))#activity status
    print("Bot is now online!")


    @client.command()
    async def locate(ctx, ip):
            r = requests.get( url = f'Insert your ipinfo api here')#API
            embed = discord.Embed(title="You can't hide", color=await random_color())
            embed.add_field(name="Ip address", value=(r.json()["ip"]), inline=False)
            embed.add_field(name="ISP", value=(r.json()["org"]), inline=False)
            try:
                hostname = r.json()["hostname"]
                embed.add_field(name="Hostname", value=hostname, inline=False)
            except KeyError:
                embed.add_field(name="Hostname", value="Hostname is hidden", inline=False)
            embed.add_field(name="City", value=(r.json()["city"]), inline=False)
            embed.add_field(name="Region", value=(r.json()["region"]), inline=False)
            embed.add_field(name="Country", value=(r.json()["country"]), inline=False)
            embed.add_field(name="Timezone", value=(r.json()["timezone"]), inline=False)
            await ctx.send(embed=embed)

    @client.command()
    async def help(ctx, cmd=None):
            embed = discord.Embed()
            embed.title = "Discord Bot Help / Dashboard"
            embed.add_field(name=":globe_with_meridians: **IP Location**", value="`geoip`", inline=False)
            embed.set_thumbnail(url= ctx.guild.icon_url)
            embed.set_footer(text="Help Commands", icon_url = ctx.guild.icon_url)
            embed.color = discord.Color.blurple()
            await ctx.reply(embed=embed, mention_author=False)

client.run(token)#put your bot token inside of config.json
