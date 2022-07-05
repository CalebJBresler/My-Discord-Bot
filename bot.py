import discord
from dotenv import load_dotenv
import os

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  channel = client.get_channel(993599667097047201)
  await channel.send('Online') 
  await channel.purge(limit=1)

@client.event
async def on_message(message):

    uni_code = ">"
    position = []

    if message.author == client.user:
        return


    Message = message.content
    MessageList = Message.split(' ')


    if MessageList[0] == "cls":
      await message.channel.purge(limit=1)
      number = MessageList[1]
      await message.channel.purge(limit=int(number))
  
    for each in Message:
      if each == uni_code:
        await message.channel.purge(limit=1)
        Message = message.content
        spliter = uni_code
        MessageList = Message.split(spliter)
        MessageLen = len(MessageList)
        times = Message.count(spliter)
        embed = discord.Embed(url=str(MessageList[2]))
        c = 0
        for i in range(times//3):
            c += 3
            number = c-1
            position.append(number)
        print(position)
        for each in position:
            embed.description = f"{MessageList[each-2]} [{MessageList[each-1]}]({MessageList[each]})"
            await message.channel.send(embed=embed)
        await message.channel.send()
        break

client.run(os.getenv("TOKEN"))
