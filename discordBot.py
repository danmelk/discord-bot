import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from reddit import data
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

activity = discord.Activity(name="at Deathbringer's Will", type=discord.ActivityType.watching)

client = commands.Bot(command_prefix='$', activity = activity)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

@client.listen('on_message')
async def on_message(message):
    if message.content.startswith(client.user.mention):
        bot_response = await message.reply(f'Reddit request from {message.author.mention}!')
        emojis = [
        '\N{shower}',
        '\N{Smiling Cat Face with Heart-Shaped Eyes}',
        '\N{Upwards Black Arrow}',
        '\N{Test tube}'
        ]
        for emoji in emojis:
            await bot_response.add_reaction(emoji)

@client.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji
    if user.bot:
        return

    elif emoji == "\N{shower}":
        submission_data = await data('ShowerThoughts')
        await user.send(submission_data)

    elif emoji == "\N{Smiling Cat Face with Heart-Shaped Eyes}":
        submission_data = await data('Aww')
        await user.send(submission_data)
        
    elif emoji == "\N{Upwards Black Arrow}":
        submission_data = await data('GetMotivated')
        await user.send(submission_data)

    elif emoji == "\N{Test tube}":
        submission_data = await data('Homelab')
        await user.send(submission_data)
        
    else:
        return 



@client.command()
async def sub(ctx, subreddit):
    submission_data = data(subreddit)
    await ctx.reply(submission_data, mention_author=True)


client.run(TOKEN)