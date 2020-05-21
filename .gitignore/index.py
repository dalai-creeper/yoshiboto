import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='§')

# a copi colle en changent le texte et nom de la fonction
@bot.command()
async def i_i_i (ctx):
    await ctx.send("LOVE LITTLE GIRL THEY MAKE ME FEEL SO GOOD https://www.youtube.com/watch?v=GAHfZNPoLW0")


jeton = "NzEyNzg5NTIxOTgwMzI1OTgx.XsWzmw.UvftApGFgU0ciKhSM-y7ZmADaVE"

bot.run(jeton)

