import discord
from discord.ext import commands
import pytest
import discord.ext.test as dpytest


@pytest.mark.asyncio
async def test_ping(bot):
    await dpytest.message("!ping")
    assert dpytest.verify().message().contains().content("Ping:")

@pytest.mark.asyncio
async def test_foo(bot):
    await dpytest.message("!hello")
    assert dpytest.verify().message().content("Hello World!")