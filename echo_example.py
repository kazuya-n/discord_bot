import discord
import asyncio
import user_token as ut


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!echo'):
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        await client.edit_message(tmp, 'Echoing : ' + message.content)

client.run(ut.TOKEN)
