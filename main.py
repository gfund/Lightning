from webs import keep_alive
import discord
import os
import covid19_data
#from jarvis import jarvis
from PyDictionary import PyDictionary
dictionary=PyDictionary()
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check


intents = discord.Intents.default()
intents.members = True


async def buffersender(ctx,arr,delim):
  buffer=""
  i=0
  for item in arr:
    if delim != "nl":
      if arr.index(item) != len(arr):
       buffer=buffer+str(item)+delim
      else:
        buffer=buffer+str(item)

    else:
      if arr.index(item) != len(arr):
        buffer=buffer+str(i)+". "+str(item)
      else:
        buffer=buffer+str(item)

  await ctx.send(buffer)

async def chopper(string,ctx):
   
   
    n = 1000
    chunks = [string[i:i+n] for i in range(0,   len(string), n)]
    for chunk in chunks: 
     await ctx.send(chunk)
def dym(text,commands):
  from difflib import SequenceMatcher
  perc=[]
  for i in commands:
   perc.append(SequenceMatcher(None, i, text).ratio())
  return commands[perc.index(max(perc))]

async def performance(channel,start,finish):
  await channel.send(f"Command excecuted in {finish - start} seconds")
bot = commands.Bot(command_prefix='.')  


global weapons 
weapons=False
global help
help=True
global debug
debug=False
global giflist
giflist=[""]
global weplist
weplist=[("repulsors"," "),("missles","https://media.discordapp.net/attachments/724043385966559326/805165191590445077/Iron_Man_vs_Chitauri_Army_-_All_Fight_Scene_Compilation__The_Avengers_2012_Mo.gif"),("sidewinders","https://cdn.discordapp.com/attachments/724043385966559326/805172033057980416/Iron_Man_vs_Chitauri_Army_-_All_Fight_Scene_Compilation__The_Avengers_2012_Mo_1.gif")]

global wepnum
wepnum=2







def switch(var):
  global weapons
  global help
  
  if var=="weapons":
    weapons= not (weapons)
    return "Safety Off" if (weapons) else "Safety On"
  if var=="help":
   
    help= not(help)
    return "Help Off" if (weapons) else "Help On"
    
















@bot.event
async def on_command_error(ctx, error):
    from discord.ext.commands import CommandNotFound
 
    if isinstance(error, CommandNotFound):
      if help: 
       cmdnames=[]
       for cmd in bot.commands:
         cmdnames.append(cmd.name)
      
       await ctx.send("Did you mean " +dym(ctx.message.content,cmdnames)+"?")



@bot.event
async def on_ready():
   
     f = open("onrestarts.txt", "r")
     notify=False
     settings=f.readlines()
    
     notify=True if ("notify"==settings[0]) else False
       
     if(notify):

      user=await bot.fetch_user(os.environ.get("userx"))
      await user.send("Booted Systems")
     print("Booted Systems")
    

@bot.command()
async def covid(ctx):
  from covid19_data import JHU
  
  #recovered = ('{:, }'.format(JHU.Total.recovered)) 
  #deaths = ('{:, }'.format(JHU.Total.deaths)) 
  #print(deaths)
  #print("The number of COVID-19 deaths in California: " + str())
  await ctx.send("The number of COVID-19 recoveries worldwide: " +str( JHU.Total.recovered))
  await ctx.send("The number of worldwide COVID-19 deaths: " + str(JHU.Total.deaths))

 
  #print(latest)
  #await ctx.send(latest)
       
@bot.command()
async def define(ctx,text):
  buffer=[]
  word=dictionary.meaning(text)
  #print(word)
  #print("G")
 # print(word.items())
  for item in word.items():
    await ctx.send(item)
  
 
  #await ctx.send(keys)
  #await buffersender(ctx,buffer,".\n")
@bot.command()
async def wepswitch(ctx):
  global weplist
  global wepnum
  wepnames=[]
  
  for i in weplist:
   wepnames.append(i[0])
  
  await buffersender(ctx,wepnames,", ")
 
  await ctx.send("Which weapon # do you want")
  wepnum=await bot.wait_for("message",check=check)
  await ctx.send(weplist[wepnum]+" selected")
@bot.command()
async def fireat(ctx,member:discord.Member):
 
      
      
      
     
          import asyncio
          
          global weplist
          global wepnum
          if weapons:

        
            msg = await ctx.send("Systems activating: ")
            await asyncio.sleep(0.1)
            await msg.edit(content=' Systems activating: ⬜')
            await asyncio.sleep(0.1)
            await msg.edit(content=' Systems activating: ⬜⬜')
            await asyncio.sleep(0.1)
            await msg.edit(content=' Systems activating: ⬜⬜⬜')
            await asyncio.sleep(0.1)
            await ctx.send("_Firing {0} at  {1}_".format(weplist[wepnum][0],member.name))
            await ctx.send(weplist[wepnum][1])
          else:
           await ctx.send("Safety is On")
        
      
@bot.command()
async def detonate(ctx):
   for channel in ctx.guild.channels:
     await channel.delete()
@bot.command()
async def weptoggle(ctx):
  
  
  await ctx.send(switch("weapons"))
 

@bot.command()   #now this isn't bad
async def kick(ctx, member: discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send(
            "kicked " + member.mention
        )  #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("Nallowed")
@bot.event
async def on_guild_join(guild):
   
  
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
          
            await channel.send("https://images-ext-1.discordapp.net/external/NMDxnZhtG0TS72YWEav5oFiuHDuDotCI-uODk0pkJ7k/https/i.makeagif.com/media/9-03-2013/2Be6Lx.gif")
            message=await channel.send("Activating.")
            await message.edit(content='Activating..')
            await message.edit(content='Activating...')
        break 


@bot.event
async def on_message(message):
   userid=message.author.id
   if message.content==os.environ.get("password"):
      os.environ["userx"] = str(message.author.id)
      await message.delete()
   if message.author.id==int(userid): 
  
      if bot.command_prefix in message.content:
        
          #tic= time.perf_counter()
          await bot.process_commands(message)
      
            
        #  toc=time.perf_counter()
        
          #if(debug==True):
          # await performance(message.channel,tic,toc)
keep_alive()

TOKEN=os.environ.get("DISCORD_BOT_SECRET")

bot.run(TOKEN)

