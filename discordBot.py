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

@client.command()
async def sub(ctx, subreddit):
    submission_data = data(subreddit)
    await ctx.reply(submission_data, mention_author=True)

client.run(TOKEN)