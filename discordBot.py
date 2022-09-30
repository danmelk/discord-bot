from discord.utils import get
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from reddit import data
load_dotenv()

activity = discord.Activity(name="hentai", type=discord.ActivityType.watching)

bot = commands.Bot(command_prefix='$', activity = activity)

emoji_to_subreddit = {
        "\N{shower}" : "ShowerThoughts",
        "\N{Smiling Cat Face with Heart-Shaped Eyes}" : "Aww",
        "\N{Upwards Black Arrow}" : "GetMotivated",
        "\N{Test tube}" : "Homelab"
    }

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.listen('on_message')
async def on_message(message):

    if message.author == bot.user:
        return
       
    if message.content.startswith(bot.user.mention):
        
        if isinstance(message.channel, discord.channel.DMChannel):
            await message.channel.send("Dont DM me prick")
            return 

        else:
            emojis = [
            '\N{shower}',
            '\N{Smiling Cat Face with Heart-Shaped Eyes}',
            '\N{Upwards Black Arrow}',
            '\N{Test tube}'
            ]

            for emoji in emojis:
                await message.add_reaction(emoji)

@bot.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji

    if user.bot:
        return

    if emoji in emoji_to_subreddit.keys():
        
        channel_name = f'{emoji}-{emoji_to_subreddit.get(emoji).lower()}'
        
        category = discord.utils.get(reaction.message.guild.categories, name = "Reddit")
        channel = discord.utils.get(reaction.message.guild.text_channels, name = channel_name)        

        if category is None:

            new_category = await reaction.message.guild.create_category("Reddit")
        
            if channel is None:

                new_channel = await reaction.message.guild.create_text_channel(channel_name, category = new_category)
                
                submission_data = await data(emoji_to_subreddit[emoji])
                await embed(submission_data, new_channel)
            
            else:
                
                submission_data = await data(emoji_to_subreddit[emoji])
                await embed(submission_data, channel)

        else:

            if channel is None:

                submission_data = await data(emoji_to_subreddit[emoji])
                new_channel = await reaction.message.guild.create_text_channel(channel_name, category = category)
                await embed(submission_data, new_channel)

            else:
                
                submission_data = await data(emoji_to_subreddit[emoji])
                await embed(submission_data, channel)


async def embed(submission_data, channel):
    if len(submission_data['body']) >= 1500:
        description = f"{submission_data['body'][0:1500]}\n [Read full post...](https://www.reddit.com{submission_data['url']})"
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

    await channel.send(embed = embed)


bot.run(os.getenv("DISCORD_TOKEN"))