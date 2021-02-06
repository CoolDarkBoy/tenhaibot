import discord
import json
import random
import os
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='tenhai ')



@client.command(name='version')
async def version(context):
        
    myEmbed = discord.Embed(title="Bot Version", description="Current Version :", color=0x192d6b)
    myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date Released", value="16th Jan, 2021", inline=False)
    myEmbed.set_footer(text="Made by Tan")
    myEmbed.set_author(name="Tenhai Bot")
    
    await context.message.channel.send(embed=myEmbed)


@client.event
async def on_ready():
    print("Bot Running!")
    general_channel = client.get_channel(687297621332721675)
    #await general_channel.send("Hello World!")

#@client.event
#async def on_message(message):
#
#    if message.content == 'bot version':
#        general_channel = client.get_channel(687297621332721675)
#        
#        myEmbed = discord.Embed(title="Bot Version", description="Current Version :", color=0x192d6b)
#        myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
#        myEmbed.add_field(name="Date Released", value="16th Jan, 2021", inline=False)
#        myEmbed.set_footer(text="Made by Tan")
#        myEmbed.set_author(name="Tenhai Bot")
#        await general_channel.send(embed=myEmbed)
#    await client.process_commands(message)

list = ['1.gif','2.gif','3.gif']

#@client.command(name="gif")
#async def gif(context):
#    await context.message.channel.send(file=discord.File(random.choice(list)))

@client.command(name="gif")
async def gif(context):
    gif = os.listdir('./gifs/')
    imgString = random.choice(gif)  # Selects a random element from the list
    path = "./gifs/" + imgString
    await context.message.channel.send(file=discord.File(path))


@client.command(name="image")
async def image(ctx):
    img = os.listdir('./images/')
    imgString = random.choice(img)  # Selects a random element from the list
    path = "./images/" + imgString
    await ctx.send(file=discord.File(path))


@client.command(name='lewd',description='Plays lewd in the voice channel',pass_context=True,)
async def lewd(context):
    # grab the user who sent the command
    user=context.message.author
    voice_channel=user.voice.voice_channel
    channel=None
    # only play music if user is in a voice channel
    if voice_channel!= None:
        # grab user's voice channel
        channel=voice_channel.name
        await client.say('User is in channel: '+ channel)
        # create StreamPlayer
        vc= await client.join_voice_channel(voice_channel)
        player = vc.create_ffmpeg_player('lewd.mp3', after=lambda: print('done'))
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        player.stop()
        await vc.disconnect()
    else:
        await client.say('User is not in a channel.')


client.run('Nzk2MDA5NjExODE1MDI2Njk4.X_RruA._XpkNkTwmcMMS15HRSV_7EUaLqo')