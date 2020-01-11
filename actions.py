from config import tenor_key, prefix
from helpers import print
import requests
import random
import math
import discord
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
last_gif = None


print("Reloading actions.py", log_level=1)


def get_gif(search_term, lmt=10, pos=None, wo_anime=False):
    global last_gif
    if pos is None:
        pos = random.randint(0, 15)
    if not wo_anime:
        search_term = 'anime ' + search_term
    r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&contentfilter=medium&pos=%s" % (search_term, tenor_key, lmt, pos))

    if r.status_code == 200:
        gifs = r.json()
        options = [itm["media"][0]['gif']["url"] for itm in gifs["results"]]
        if last_gif in options:
            print(len(options))
            options.remove(last_gif)
            print("last_gif in options", len(options))
        sel = random.choice(options)
        last_gif = sel
        print(sel, "<-", options)
        return sel
    else:
        return None


def get_goat():
    goats = [g for g in os.listdir(dir_path + '/assets/goats/') if not g.endswith('.mp4') and not g.endswith('.db')]
    goat = random.choice(goats)
    print(goat, "<-", len(goats))
    return goat


async def hi(channel, params, mentions, author):
    msg = 'Hi {}! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧'.format(author.mention)
    await channel.send(msg)


async def fluff(channel, params, mentions, author):
    if len(mentions) == 0:
        await channel.send('Wen denn? o.O')
        return
    msg = '{}, du wurdest von {} geflauscht'.format(mentions[0].mention, author.mention)
    gif = get_gif('headpat')

    embed = discord.Embed()
    embed.description = msg
    embed.set_image(url=gif)
    await channel.send(embed=embed)


async def yawn(channel: discord.TextChannel, params, mentions, author):
    gif = get_gif('yawn')

    embed = discord.Embed()
    embed.set_image(url=gif)
    await channel.send(embed=embed)


async def sleep(channel: discord.TextChannel, params, mentions, author):
    gif = get_gif('sleep')

    embed = discord.Embed()
    embed.set_image(url=gif)
    await channel.send(embed=embed)


async def mauw(channel, params, mentions, author):
    gif = get_gif('sad')

    embed = discord.Embed()
    embed.set_image(url=gif)
    await channel.send(embed=embed)


async def sorry(channel, params, mentions, author):
    gif = get_gif('sorry')

    embed = discord.Embed()
    if len(mentions) != 0:
        embed.description = '{} hat sich bei dir entschuldigt, {}'.format(author.mention, mentions[0].mention)
    embed.set_image(url=gif)
    await channel.send(embed=embed)


async def goat(channel, params, mentions, author):
    gif = get_goat()

    file = discord.File(dir_path + "/assets/goats/" + gif, filename=gif)
    embed = discord.Embed()
    if len(mentions) != 0:
        embed.description = 'Eine Ziege für {}!'.format(mentions[0].mention)
    embed.set_image(url="attachment://" + gif)
    await channel.send(file=file, embed=embed)


async def goatcount(channel, params, mentions, author):
    msg = '{} süße Ziegen!!!'.format(len([g for g in os.listdir(dir_path + '/assets/goats/') if not g.endswith('.mp4') and not g.endswith('.db')]))
    await channel.send(msg)


async def yes(channel, params, mentions, author):
    gif = get_gif('yes')
    embed = discord.Embed()
    if len(mentions) != 0:
        embed.description = 'Yes, {}'.format(mentions[0].mention)
    embed.set_image(url=gif)
    await channel.send(embed=embed)


async def no(channel, params, mentions, author):
    gif = get_gif('no')
    embed = discord.Embed()
    if len(mentions) != 0:
        embed.description = 'No, {}'.format(mentions[0].mention)
    embed.set_image(url=gif)
    await channel.send(embed=embed)


async def runaway(channel, params, mentions, author):
    gif = get_gif('runaway')
    embed = discord.Embed()
    if len(mentions) != 0:
        msg = '{} rennt vor {} weg'.format(author.mention, mentions[0].mention)
        embed.description = msg
    embed.set_image(url=gif)
    await channel.send(embed=embed)


async def aww(channel, params, mentions, author):
    gif = get_gif('aww')
    embed = discord.Embed()
    embed.set_image(url=gif)
    await channel.send(embed=embed)


async def giggle(channel, params, mentions, author):
    gif = get_gif('giggle')
    embed = discord.Embed()
    embed.set_image(url=gif)
    await channel.send(embed=embed)


async def kiss(channel, params, mentions, author):
    if len(mentions) == 0:
        await channel.send('Wen denn? o.O')
        return

    # self check
    if mentions[0].mention == author.mention:
        msg = 'Haha!'
        await channel.send(msg)
        return
    else:
        msg = '{}, du wurdest von {} geküsst'.format(mentions[0].mention, author.mention)

    # embed
    embed = discord.Embed()
    gif = get_gif('kiss')
    embed.description = msg

    # link check
    if mentions[0].name == "Link_iene" and mentions[0].discriminator == "8415":
        print("is link")
        if author.name == "Vincent" and author.discriminator == "0212":
            print("is vincent")
        else:
            gif = get_gif('slap')
            embed.description = "Nein."

    # vincent check
    if mentions[0].name == "Vincent" and mentions[0].discriminator == "0212":
        print("is vincent")
        if author.name == "Link_iene" and author.discriminator == "8415":
            print("is link")
        else:
            gif = get_gif('slap')
            embed.description = "Nein."

    embed.set_image(url=gif)
    await channel.send(embed=embed)


async def shutup(channel, params, mentions, author):
    gif = get_gif('stfu')

    embed = discord.Embed()
    if len(mentions) != 0:
        msg = 'Shut up, {}!'.format(mentions[0].mention)
        embed.description = msg
    embed.set_image(url=gif)
    await channel.send(embed=embed)


async def grr(channel, params, mentions, author):
    gif = get_gif('grr')

    embed = discord.Embed()
    if len(mentions) != 0:
        msg = '{}, du wurdest von {} angegrrt'.format(mentions[0].mention, author.mention)
        embed.description = msg
    embed.set_image(url=gif)
    await channel.send(embed=embed)


async def mimimi(channel, params, mentions, author):
    gif = get_gif('mimimi', wo_anime=True)

    embed = discord.Embed()
    if len(mentions) != 0:
        msg = 'Mimimi, {}!'.format(mentions[0].mention)
        embed.description = msg
    embed.set_image(url=gif)
    await channel.send(embed=embed)


async def source(channel, params, mentions, author):
    link = 'https://github.com/vincentscode/ExtendedKawaii-DiscordBot'
    msg = 'Hinter diesem Link findest du meinen Quellcode (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧\n<{}>'.format(link)
    await channel.send(msg)


async def invite(channel, params, mentions, author):
    link = 'https://discordapp.com/oauth2/authorize?client_id=665549589394227220&response_type=code&scope=bot'
    msg = 'Benutze diesen Link um mich einzuluden (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧\n<{}>'.format(link)
    await channel.send(msg)


async def list_commands(channel, params, mentions, author):
    inline = True
    if len(params) != 0:
        if params[0] == '1':
            inline = False
    embed = discord.Embed()
    embed.title = "Liste der Befehle"
    embed.description = 'Prefix: ``' + prefix + '``'
    embed.add_field(name='**Hi**', value="Hi! (✿◠‿◠)", inline=inline)
    embed.add_field(name='**Fluff / Flausch / Flauschel [Person]**', value="Jemanden flauscheln! ^-^", inline=inline)
    embed.add_field(name='**Yawn / Gähn**', value="Müdigkeit! D:", inline=inline)
    embed.add_field(name='**Sleep**', value="Zu viel Müdigkeit! D:", inline=inline)
    embed.add_field(name='**Mauw**', value=":(", inline=inline)
    embed.add_field(name='**Sorry [Optional: Person]**', value="Sich entschuldigen", inline=inline)
    embed.add_field(name='**Goat [Optional: Person]**', value="Eine von {} süßen Ziegen! owo".format(len([g for g in os.listdir(dir_path + '/assets/goats/') if not g.endswith('.mp4') and not g.endswith('.db')])), inline=inline)
    embed.add_field(name='**Yes / Ja [Optional: Person]**', value="Jaaa!", inline=inline)
    embed.add_field(name='**No / Nope / Nein [Optional: Person]**', value="Neeee!", inline=inline)
    embed.add_field(name='**runaway [Optional: Person]**', value="Nichts wie weg! (˚▽˚’!)/", inline=inline)
    embed.add_field(name='**aww**', value="Aww! (๑ºωº)", inline=False)
    embed.add_field(name='**giggle**', value="Hehe", inline=False)
    embed.add_field(name='**kkiss / küss [Person]**', value="Ein Kuss! (ɔˆ ³ˆ⋆)♥(◦’ںˉ◦)", inline=inline)
    embed.add_field(name='**shutup / stfu [Optional: Person]**', value="RUHE! (╯°□°)︻╦╤─ - - -", inline=inline)
    embed.add_field(name='**grr / hiss [Optional: Person]**', value="Grrrr (╯°□°)︻╦╤─ - - -", inline=inline)
    embed.add_field(name='**mimimi [Optional: Person]**', value="MIMIMI (╯°□°)︻╦╤─ - - -", inline=inline)
    embed.add_field(name='**invite**', value="Lad' mich ein! ʕ•́ﻌ•̀ʔ", inline=inline)
    embed.add_field(name='**source**', value="Das bin ich! :eyes:", inline=inline)
    embed.add_field(name='**help**', value="Diese Hilfe.", inline=inline)
    await channel.send(embed=embed)


async def ping(channel, params, mentions, author):
    await channel.send("Pong!")

commands = {
    'hi': hi,
    'fluff': fluff,
    'flausch': fluff,
    'flauschel': fluff,
    'yawn': yawn,
    'gähn': yawn,
    'sleep': sleep,
    'mauw': mauw,
    'sorry': sorry,
    'goat': goat,
    'goatcount': goatcount,
    'yes': yes,
    'ja': yes,
    'no': no,
    'nein': no,
    'nope': no,
    'runaway': runaway,
    'aww': aww,
    'giggle': giggle,
    'kkiss': kiss,
    'küss': kiss,
    'shutup': shutup,
    'stfu': shutup,
    'süß': kiss,
    'grr': grr,
    'hiss': grr,
    'mimimi': mimimi,
    'invite': invite,
    'source': source,
    'help': list_commands,
}
