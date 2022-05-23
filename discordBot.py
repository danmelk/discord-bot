import os
import discord
import asyncio
from dataclasses import dataclass
from dotenv import load_dotenv
from reddit import data
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hi'):
            await message.reply(f'Hello, {message.author.name}!', mention_author=True)

        # if message.content.startswith('!meme'):
        #     loop = asyncio.new_event_loop()
        #     asyncio.set_event_loop(loop)
        #     print('1')
        #     loop.run_until_complete(data("learnpython"))
        #     print('2')
            
        #     submission_data = loop
        #     print('3')

        #     loop.close()
        #     await message.reply(submission_data, mention_author=True)



activity = discord.Activity(name="at Deathbringer's Will", type=discord.ActivityType.watching)
print('1')

client = MyClient(activity=activity)
print('2')

client.run(TOKEN)