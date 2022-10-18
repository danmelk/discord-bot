import os
import discord.ext.test as dpytest
import pytest
from discordBot import bot as bot_instance
from dotenv import load_dotenv
load_dotenv()


@pytest.fixture
def bot(event_loop):
    bot = bot_instance # However you create your bot, make sure to use loop=event_loop
    dpytest.configure(bot)
    return bot


@pytest.fixture(scope='session')
def bot_start():    
    discord_token = os.getenv("DISCORD_TOKEN")
    return discord_token 