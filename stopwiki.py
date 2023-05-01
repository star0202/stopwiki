import discord
import re
import time
from asyncio import sleep

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game("검열"),
    )


p = re.compile(
    "(https?:\/\/(ko[.])?wikipedia[.]org\/wiki(\/[^\s]+)?)|(https?:\/\/w[.]wiki(\/[^\s]+)?)"
)


@client.event
async def on_message(msg):
    if p.search(msg.content):
        a = await msg.channel.send("위키백과 관련 대화는 제한됩니다.")
        await msg.delete()
        sleep(5)
        await a.delete()
        return


client.run(TOKEN)
