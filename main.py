import discord
from discord.ext import commands, tasks
from itertools import cycle

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='z!', help_command=None)
status = cycle(['Zashin#0550'])
queue = []


@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_ready():
    change_status.start()
    print(f'Connected to {client.user}')


@client.command()
async def ping(cxt):
    await cxt.send(f'My fps is {round(client.latency * 1000)}ms ')

@client.listen('on_message')
async def on_message(message):
    if "!check 8990340321" in message.content:
        await message.channel.send('``mã giảm giá : 8990340321``')
        await message.channel.send('``sale 10% tổng đơn hàng``')
        await message.channel.send('``hạn sử dụng 30/7``')

client.run( "OTk4ODk0Mzk1NzQ5MzAyMzIz.G7SGhr.OShEnd81MS69jvTo7LZYQBnjQ2YNiKc7wNGkec")
