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
            r = requests.get( url = f'https://ipinfo.io/{ip}/geo')#API
            embed = discord.Embed(title="You can't hide", color=await random_color())
            embed.set_thumbnail(url="https://lh3.googleusercontent.com/LJu2b82H2hJMK3AVAViB3CL3PBx_rhd83jha0qw9rhVrKMRAmkLUUDNW2XO3cSdUpwRzq9_V3-ESGz_YNQFte3Cv8BsnnGI1gbbBwRHW292mwcb2U359JucIQYAoo8da8dBVsEdsd3v5-ToHd32EmM1OtpU3EpiCa0ppJ_L1SUC3LuQHn5C4ZBV766SkUpModjJKH41g-MJPr0sNea7-BLzKFuoGUKQjnsNLZaCml0Lxusb14-FXL2CS7bzcHbiSOD5G-unz59I3Nv7SoHsiagtMIJ7yYisIUo7H5SxDgs5CMy1pA-j8DxoLqh627PlwUK5L_HLRBA8sVVf4kKXs-9VhWdJ5tMb6QtI7YINZ_nltFJtnnBGjFWhS8nAeDKAxQ3ZgRYSB1UyCajVtLRYblK5FB-GAU8iimF0JYSlWzhnGlvjxAkbSxMYUgXCkMXH_Qw6dxqz2sRZbAAGF7S8lxAUmOeiyXPqW3Gqp5Q9AdiXx0TKXE96UB2Tf77FcKUTsktZOI7Y-PNIjrwNNVm2aDKzompPU1PaXd5XZFZ4TEko0E0Z1d21RVOkiqU5idwDWSy3yzqYieKzmNe0yj3lB0N7jHkXQTX2h5_dG32YPeJUYETei8cl_r0yXED-jzLyP5XgLM7VyXBAw0YfQ5ssEtYRbzfSJYRR8SpFJl8Hqz-DMB7Q292XupNw57TebQi4M3-WMSyquwzyAWoRHAY5arD5yvAQvzWCnE3WQC_e1JD8oV4YesjF0i--EnLn_aNgDdrO0qUAgc5FMDJaGeUX8N90WoK8QeOJDIKIYMjBqijprDFvDf2_9fM8cLUTQhF5i9wDpO6OJELoQjXoSeT9-HNPxEa5sF9-fUAN3oQxXw2jdDJ-dJ5LlB1goHGIdJQglYYwNN6ITTc_E9gOR9xUU4jQLhXjEuE9Vdim8Qc3C5k4S2azKzK_Qcw6mcp6yqqDt187Dm2Bgdd4dSHZzksZL=w947-h947-s-no?authuser=0")
            embed.add_field(name="Ip address", value=(r.json()["ip"]), inline=False)
            embed.add_field(name="ISP", value=(r.json()["org"]), inline=False)
            try:
                hostname = r.json()["hostname"]
                embed.add_field(name="Hostname", value=hostname, inline=False)
            except KeyError:
            # If "hostname" is not found in the JSON response, add a message to the embed
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

client.run(token)#you put your bot token inside of config.json
