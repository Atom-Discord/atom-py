import discord
from discord.ext import commands, tasks
import os
import json
from itertools import cycle
import periodictable as pt
from equation import Equation
from youtubesearchpython import SearchVideos
from ast import literal_eval
import asyncio
import sqlite3


from UnitConversions import mass_to_moles
from UnitConversions import moles_to_mass
from UnitConversions import mass_to_units
from UnitConversions import units_to_mass
from UnitConversions import units_to_moles
from UnitConversions import moles_to_units

"""
SETUP

"""
queues = {}
players = {}

def get_prefix(client, message):
    with open('C:\Atom\src\prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


client = commands.Bot("-")
status = cycle(['Chemistry', 'Dreaming About Chemistry'])


@client.event
async def on_guild_join(guild):
    with open('C:\Atom\src\prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '-'

    with open('C:\Atom\src\prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
    with open('C:\Atom\src\prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('C:\Atom\src\prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.command()
async def changeprefix(ctx, new_prefix):
    with open('C:\Atom\src\prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = new_prefix

    with open('C:\Atom\src\prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to {new_prefix}')




@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)


@client.command()
async def kick(ctx, member: discord.Member, *args, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *args, reason=None):
    await member.ban(reason=reason)
    await ctx.send('Banned {member.mention}')


@client.command()
async def unban(ctx, *args, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban in banned_users:
        user = ban.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('C:\Atom\src\cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@tasks.loop(hours=1)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found")
    else:
        raise error



@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete!')


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')


def is_it_me(ctx):
    return ctx.author.id == 320187068212969472


@client.command()
@commands.check(is_it_me)
async def example(ctx):
    await ctx.send(f'Hi im {ctx.author}')






@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

"""
YOUTUBE

"""

        



"""
CHEM CODE (UNIT CONVERSIONS)

"""


@client.command(aliases=['mass-to-moles', 'mass2moles', 'mass->moles'])
async def mass_to_moles(ctx, element, original_mass: float, sig_figs: int, answer=0):
    await ctx.send(str(mass_to_moles(element, original_mass, sig_figs)))


@client.command(aliases=['moles-to-mass', 'moles2mass', 'moles->mass'])
async def moles_to_mass(ctx, element, moles: float, sig_figs: int, answer=0):
    await ctx.send(asyncio.run(moles_to_mass(element, moles, sig_figs)))


@client.command(aliases=['mass-to-units', 'mass->units', 'mass2units'])
async def mass_to_units(ctx, element, mass: float, sig_figs: int, units):
    await ctx.send(mass_to_units(element, mass, sig_figs, units))


@client.command(aliases=['units-to-mass', 'units->mass', 'units2mass'])
async def units_to_mass(ctx, element, coef: float, exponent: float, sig_figs, units):
    await ctx.send(units_to_mass(element, coef, exponent, sig_figs, units))


@client.command(aliases=['units-to-moles', 'units->moles', 'units2moles'])
async def units_to_moles(ctx, coef: float, exponent: float, sig_figs: int):
    await ctx.send(units_to_moles(coef, float, exponent, sig_figs, int))


@client.command(aliases=['moles-to-units', 'moles->units', 'moles2units'])
async def moles_to_units(ctx, moles, sig_figs, units):
    await ctx.send(moles_to_units(moles, sig_figs, units))

@client.command()
async def testembed(ctx):
    emb = discord.Embed(title="Title", description="Description", colour=discord.Color.red(), url="https://www.google.com")
    await ctx.send(embed=emb)

@client.event
async def on_message(message):

    if message.content == "-bot_version":
        general_channel = client.get_channel(730271257416826963)

        myEmbed = discord.Embed(title="Current Version", description="Version 1.0", color=0x00ff00)
        myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date Released:", value="July", inline=False)
        myEmbed.set_footer(text="This is a sample footer")
        await general_channel.send(embed=myEmbed)

    await client.process_commands(message)

"""
CHEM CODE (BALANCING EQUATIONS)

"""


# @client.command()
# async def run_balance(ctx, unbalanced):
#     """
#     Runs the chemical equation balance algorithm
#     """
#     equation = Equation(unbalanced)
#     ctx.send('Balanced equation: ' + equation.balance())

@client.command()
async def balance(ctx, *, equation):
    """
    Runs the chemical equation balance algorithm
    """
    equation = Equation(equation)
    await ctx.send('Balanced equation: ' + equation.balance())


@client.command()
async def proto(ctx, mass, coefA, coefB, element1, element2):
    x = getattr(pt, element1, 'element not on periodic table')
    y = getattr(pt, element2, 'element not on periodic table')
    mmA = x.mass
    mmB = y.mass
    mass_to_mass = (mass * coefB) * mmB / (mmA * coefA)
    ctx.send(mass_to_mass)


# @client.command()
# async def stoichiometry(ctx, element, unknown_element, known_mass: float, mmA: float, mmB: float, *, eq):
#     equation = Equation(eq)
#     balanced_equation = equation.balance()
#     print(balanced_equation)
#     split = balanced_equation.split(' = ')
#     left = split[0]
#     right = split[1]
#     left_components = left.split(' + ')
#     right_components = right.split(' + ')
#     left_coefs = {}
#     right_coefs = {}
#     lis = []
#     lis2 = []
#     u = 0
#     u2 = 0
#     p = lambda x: enumerate(x)
#     o  = list(p(left_components))
#     o2  = list(p(right_components))
#     for i in range(len(o)):
#         lis.append(o[u][0])
#         u += 1
#     for i in range(len(o2)):
#         lis2.append(o[u2][0])
#         u2 += 1
#     for x in lis:
#         if x >= 0:
#             left_coefs[left_components[x][1:len(left_components[x]) + 1]] = left_components[x][0]
#     for x2 in lis2:
#         if x2 >= 0:
#             right_coefs[right_components[x2][1:len(right_components[x2]) + 1]] = right_components[x2][0]


#     if element in left_coefs.keys(): coefA = int(left_coefs[element])
#     elif element in right_coefs.keys(): coefA = int(right_coefs[element])
#     else: await ctx.send(left_coefs)

#     if unknown_element in left_coefs.keys():
#         coefB = int(left_coefs[unknown_element])
#     elif unknown_element + " " in right_coefs.keys():
#         coefB = int(right_coefs[unknown_element + ' '])
#     else:
#         await ctx.send(right_coefs)

#     # Calculation

#     mass_to_mass = (known_mass * coefB) * (mmB) / (mmA * coefA)
#     await ctx.send(f'{round(mass_to_mass, 2)} grams of {unknown_element}')

client.run("NzQwMzI0OTEyNzk5MTU0MTc2.XynXTQ.cej4mq5khr3p8xwau6eCS6GKAYA")
