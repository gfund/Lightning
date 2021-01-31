#Lightning Started 1/30/2021 
# Gunnar Funderburk
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
  i=1
  for item in arr:
    if delim not in ["nl","nb"]:
      if arr.index(item) != len(arr):
       buffer=buffer+str(item)+delim
      else:
        buffer=buffer+str(item)

    elif delim == "nb":
     
      if arr.index(item) != len(arr):
        buffer=buffer+str(i)+". "+str(item)+"\n"
      else:
        buffer=buffer+str(item)
    i+=1

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
bot = commands.Bot(command_prefix='.',intents=intents)  


global weapons 
weapons=False
global help
help=True
global debug
debug=False
#non weapon gif list May not use
global giflist
giflist=[""]
global weplist
weplist=[("repulsors","https://cdn.discordapp.com/attachments/724043385966559326/805207126749478942/ezgif.com-gif-maker.gif"),("missles","https://media.discordapp.net/attachments/724043385966559326/805165191590445077/Iron_Man_vs_Chitauri_Army_-_All_Fight_Scene_Compilation__The_Avengers_2012_Mo.gif"),("sidewinders","https://cdn.discordapp.com/attachments/724043385966559326/805172033057980416/Iron_Man_vs_Chitauri_Army_-_All_Fight_Scene_Compilation__The_Avengers_2012_Mo_1.gif")]
#keeps track of index
global wepnum
wepnum=0
#repeat user words
global echo
echo=False
global insuit
insuit=True

global sendm
sendm=False


 






def switch(var):
  global weapons
  global help
  global echo
  global insuit
  
  if var=="weapons":
    weapons= not (weapons)
    return "Safety Off" if (weapons) else "Safety On"
  if var=="help":
   
    help= not(help)
    return "Help On" if (help) else "Help Off"
  if var=="echo":
   
    echo= not(echo)
    return "Echo On" if (echo) else "Echo Off"
  if var=="suit":
   
    insuit= not(insuit)
    

    
















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
async def call(ctx,*,text):
  global sendm
  await ctx.send(text)
  #These are so duplicates dont pop up
  memberlist=[]
  channellist=[]
  for server in bot.guilds:
   for member in server.members:
     if member.name not in memberlist:
       memberlist.append(member.name)
       print(member.name)
       print("_---_")
       print(text)
      
       if (member.name==text) or( str(member.id)==text) or( member.nick==text):
                    user=member
                    await ctx.channel.send("FOUND")
                          
                       
                    
                    embed=discord.Embed(title="Found User in {0}".format(ctx.guild.name),color=discord.Color.blue())
                    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user))
                    embed.add_field(name="Name", value=str(user), inline=False)
                    embed.add_field(name="Bot", value=user.bot, inline=False)
                    embed.add_field(name="Created At ", value=user.created_at,  inline=False)
                    await ctx.channel.send(embed=embed)
                    await ctx.channel.send("CLEARED TO SEND")
                    sendm=True
                    person=member.id

                       
                    

@bot.command()
async def flood(ctx,*num):
  buffer=" "
  await ctx.send(num)
  if str(num)=="()":
    for i in range(0,5):
     buffer+="..........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................."
     i+=1
  await ctx.send(buffer)
@bot.command()
async def imgtext(ctx):
      import pytesseract
      pytesseract.pytesseract.tesseract_cmd = 'C:/Users/gfund/AppData/Local/Programs/Tesseract-OCR'
      from PIL import Image



     
      for attachment in ctx.message.attachments:
         import requests
         im = Image.open(requests.get(attachment.url, stream=True).raw)

     

         
         text=pytesseract.image_to_string(im)
         print(text)
         await ctx.send(text)
@bot.command()
async def fileinfo(ctx):
    #import urllib.request



    messages = await ctx.channel.history(limit=2).flatten()
    #message=messages[0]
    #await ctx.send("Corrupting")
    for attachment in messages[1].attachments:
     await ctx.send("Name "+str(attachment.filename))
     await ctx.send("Size "+str(attachment.size)+" bytes")
      
    

      
      
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
async def sampfire(ctx):
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
            await ctx.send("_Firing {0}_ ".format(weplist[wepnum][0]))
            await ctx.send(weplist[wepnum][1])
          else:
           await ctx.send("Safety is On")

@bot.command()
async def wepswitch(ctx):
  channel=ctx.channel
  uid=ctx.author.id
  def check(m):
            return m.channel == channel and m.author.id== uid
  
  
  global weplist
  global wepnum

  wepnames=[]
  
  for i in weplist:
   wepnames.append(i[0])
  
  await buffersender(ctx,wepnames,"nb")
 
  await ctx.send("Which weapon # do you want")
  wepn=await bot.wait_for("message",check=check)
  wepnum=int(wepn.content)-1
  
  await ctx.send(weplist[wepnum][0]+" selected")
@bot.command()
async def echotoggle(ctx):
  await ctx.send(switch("echo"))
@bot.command()
async def ban(ctx,member:discord.Member):
    global weapons
    if weapons:
     await ctx.guild.ban(member,reason="ban",delete_message_days=0)
     await ctx.send("banned " + member.mention)
    else: 
      await ctx.send("Safety On")
@bot.command()
async def suit(ctx):
  
  global insuit
  insuit=False
  await ctx.send("Ejecting")

    
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
   
        await member.kick(reason=None)
        await ctx.send(
            "kicked " + member.mention
        )  
    
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
    global insuit
    userid=message.author.id
    #this is if the bot is not responding
    # if message.author.id != 802306785087586344:
    # await message.channel.send(userid==int(os.environ.get("userx")))
    if message.content==os.environ.get("password"):
        os.environ["userx"] = str(message.author.id)
        
        await message.delete()
        
    if userid==int(os.environ.get("userx")):
      if echo:
        if not (isinstance(message.channel, discord.channel.DMChannel)):
          
              
          await bot.process_commands(message) 
          await message.delete()
          await message.channel.send(message.content)
          return
          

    
  
    
    if bot.command_prefix in message.content:
       if insuit:
        
          if( userid==int(os.environ.get("userx")) and ( echo==False)):
          
          
            await bot.process_commands(message)
       else:
        if(userid==int(os.environ.get("userx")) and message.content==".suit"):
          insuit=True
          await message.channel.send("Welcome back, sir")
          

      
    
        
keep_alive()

TOKEN=os.environ.get("DISCORD_BOT_SECRET")

bot.run(TOKEN)

