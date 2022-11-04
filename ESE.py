import discord
from discord.ext import commands, tasks
import asyncio
import os
from datetime import datetime, timedelta
import json

client = commands.Bot(command_prefix="!", intents=discord.Intents.all(), case_insensitive=True)

@client.command()
async def ktojestgej(ctx):
    await ctx.send("RUDY TO GEJ!")

async def readjson(filename):
  with open(filename, "r") as readjson:
    return json.load(readjson)



async def writejson(filename, variable, value):
  with open(filename, "r") as readjson:
    rjson = json.load(readjson)

  with open(filename, "w") as writejson:
    rjson[variable] = value
    json.dump(rjson, writejson)
  return True

save = 0


@client.command()
async def ustawtenkanal(ctx):
  save = int(ctx.message.channel.id)
  await writejson("save.json", "sendchannel", save)
  await ctx.send("tu bede wysylal wiadomosci")
  print(save)


@tasks.loop(hours=24)
async def job():
  save = await readjson("save.json")
  save = save["sendchannel"]
  general_channel = client.get_channel(save)
  await general_channel.send("21:37")
  print(f"[{datetime.now()}] Sent message into #{general_channel.name}")


@job.before_loop
async def before_job():
  hour = 21
  minute = 37
  await client.wait_until_ready()
  now = datetime.now()
  future = datetime(now.year, now.month, now.day, hour, minute)
  if now.hour >= hour and now.minute > minute:
    future += timedelta(days=1)
  await asyncio.sleep((future - now).seconds)


@client.event
async def on_ready():
  job.start()
  print(f"[{datetime.now()}] Bot is Online")

client.run('MTAzNjAwNTcxMjUxMTM2OTI3Ng.GKbzE-.w6QD61Yd1sym-43g_Awd0Zz9qlZUuGkVNx-J3o')

input()
