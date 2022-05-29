from operator import sub
from turtle import color, title
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

    emoji_to_subreddit = {
        "\N{shower}" : "ShowerThoughts",
        "\N{Smiling Cat Face with Heart-Shaped Eyes}" : "Aww",
        "\N{Upwards Black Arrow}" : "GetMotivated",
        "\N{Test tube}" : "Homelab"
    }

    if user.bot:
        return

    else:
        if emoji in emoji_to_subreddit.keys():
            submission_data = await data(emoji_to_subreddit[emoji])
            await embed(user, submission_data)
        


async def embed(user, submission_data):
    body_lenght = len(submission_data['body'])
    if body_lenght >= 3500:
        description = f"{submission_data['body'][0:3500]}\n [Read full post...](https://www.reddit.com{submission_data['url']})"
        embed = discord.Embed(
            title = submission_data['title'],
            url = f"https://www.reddit.com{submission_data['url']}",
            description = description,
            color = 0xFF5733,
        )
    else:
        description = f"{submission_data['body']}\n [Read full post...](https://www.reddit.com{submission_data['url']})"
        embed = discord.Embed(
            title = submission_data['title'],
            url = f"https://www.reddit.com{submission_data['url']}",
            description = submission_data['body'],
            color = 0xFF5733,
        )   
    embed.set_author(
        name = f"/r/{submission_data['subreddit']}",
        url = f"https://www.reddit.com/r/{submission_data['subreddit']}",
        icon_url = submission_data['subreddit'].icon_img
    )
    if submission_data['is_self']:
        embed.set_thumbnail(
            url = submission_data['subreddit'].icon_img
        ) 
    else:
        embed.set_thumbnail(
            url = submission_data['media']
        )
    await user.send(embed = embed)


client.run(TOKEN)