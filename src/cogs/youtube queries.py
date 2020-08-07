import discord
from discord.ext import commands
from youtubesearchpython import SearchVideos
from ast import literal_eval
import asyncio

class YouTube(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog is ready.')

    # Commands
    @commands.command()
    async def search(self, ctx, *, topic):
        
        general_channel = ctx.channel
        maxVal = 8
        search = SearchVideos(topic, offset = 1, mode = "json", max_results = maxVal)

        links = []
        title = []
        obj = literal_eval(search.result())
        i = 0
        for elems in obj['search_result'][i]: # iterate over dictionary and grab links
            if elems == 'link':
                if i != maxVal - 1:
                    for link in obj['search_result'][i]:
                        links.append(obj['search_result'][i]['link'])
                        title.append(obj['search_result'][i]['title'])
                        if i == maxVal - 1:
                            break
                        else:
                            i += 1
                            continue
                

        myEmbed = discord.Embed(
            title="Search Results", 
            description="Choose a video below!", 
            color=0x00ff00
            )
        myEmbed.add_field(name=f"{title[0]} (1)", value=links[0], inline=False)
        myEmbed.add_field(name=f"{title[1]} (2)", value=links[1], inline=False)
        myEmbed.add_field(name=f"{title[2]} (3)", value=links[2], inline=False)
        myEmbed.add_field(name=f"{title[3]} (4)", value=links[3], inline=False)
        myEmbed.add_field(name=f"{title[4]} (5)", value=links[4], inline=False)
        myEmbed.add_field(name=f"{title[5]} (6)", value=links[5], inline=False)
        myEmbed.add_field(name=f"{title[6]} (7)", value=links[6], inline=False)
        myEmbed.add_field(name=f"{title[7]} (8)", value=links[7], inline=False)
        myEmbed.set_footer(text="Pick the number of your query")
        await ctx.send(embed=myEmbed)
        if ctx.author.id == self.client.user.id:
            return

        def check(m):
            return general_channel.id == m.channel.id and m.content.isdigit()

        try:
            number = await self.client.wait_for('message', check=check, timeout=60.0)
        except asyncio.TimeoutError:
            return await ctx.send('Took too long!')
                    
        if number.content:
            await ctx.send(links[int(number.content) - 1])
        else:
            await ctx.send("Not an integer!")

            




    # Commands
    @commands.command()
    async def abu(self, ctx):
        await ctx.send('Pong!')

def setup(client):
    client.add_cog(YouTube(client))