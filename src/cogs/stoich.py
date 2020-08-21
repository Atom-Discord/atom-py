import discord
from discord.ext import commands
from equation import Equation

class stoich(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Stoich is ready.')

    # Commands
    @commands.command()
    async def stoichiometry(self, ctx, element, unknown_element, known_mass: float, mmA: float, mmB: float, *, eq):
        equation = Equation(eq)
        balanced_equation = equation.balance()
        split = balanced_equation.split(' = ')
        left = split[0]
        right = split[1]
        left_components = left.split(' + ')
        right_components = right.split(' + ')
        left_coefs = {}
        right_coefs = {}
        lis = []
        lis2 = []
        u = 0
        u2 = 0
        p = lambda x: enumerate(x)
        o  = list(p(left_components))
        o2  = list(p(right_components))
        for i in range(len(o)):
            lis.append(o[u][0])
            u += 1
        for i in range(len(o2)):
            lis2.append(o[u2][0])
            u2 += 1
        for x in lis:
            if x >= 0:
                left_coefs[left_components[x][1:len(left_components[x]) + 1]] = left_components[x][0]
        for x2 in lis2:
            if x2 >= 0:
                right_coefs[right_components[x2][1:len(right_components[x2]) + 1]] = right_components[x2][0]


        if element in left_coefs.keys(): coefA = int(left_coefs[element])
        elif element in right_coefs.keys(): coefA = int(right_coefs[element])
        else: await ctx.send(left_coefs)

        if unknown_element in left_coefs.keys(): coefB = int(left_coefs[unknown_element])
        elif unknown_element + " " in right_coefs.keys(): coefB = int(right_coefs[unknown_element + ' '])
        else: await ctx.send(right_coefs)

        # Calculation

        mass_to_mass = (known_mass * coefB) * (mmB) / (mmA * coefA)
        await ctx.send(f'{round(mass_to_mass, 2)} grams of {unknown_element}')



def setup(client):
    client.add_cog(stoich(client))
