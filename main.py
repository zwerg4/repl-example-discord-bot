import discord, flask_server, threading
from discord.ext import commands
bot = commands.Bot(command_prefix='$')
@bot.command()
async def test(ctx):
    await ctx.send("something")
threading.Thread(target=flask_server.run).start()
bot.run("NTQxNzgzOTM5MTc4NTYxNTM2.D0DNnA.bZPaQyRLp9Zl-A9-7Kl89SQSbTM")
