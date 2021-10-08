import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("!cmd")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!cmd"):
        await message.channel.send("1.!제작자,2.!제작자서버")

    if message.content.startswith("!제작자"):
        await message.channel.send("Fantboss#4687")

    if message.content.startswith("!제작자서버"):
        await message.channel.send("**https://discord.gg/QUjVvmME3E**")

access_token = os.environ["BOT_TOKEN"]
client.run("access_token")
