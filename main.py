import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True  
TOKEN = "MTMzNTY0MDA0MTU1MjA4OTIzOQ.GmueXG.LM8IjoJcxGDAyb3TLM5oIrqwoFYt3BcleEqxV8"

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} está listo para usar en {len(bot.guilds)} servidores.")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="general")  
    if channel:
        await channel.send(f"🎉 ¡Bienvenido/a {member.mention} al servidor!")

@bot.command()
async def hola(ctx):
    await ctx.send(f"¡Hola, {ctx.author.mention}! 😊")

@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! Latencia: {round(bot.latency * 1000)}ms")

@bot.command()
async def canales(ctx):
    canales = [channel.name for channel in ctx.guild.text_channels]
    await ctx.send(f"📜 Canales donde puedo hablar: {', '.join(canales)}")

bot.run(TOKEN)
