import asyncio
from cProfile import run
import asyncpraw
from dotenv import load_dotenv
import os
load_dotenv()

async def auth():
    reddit = asyncpraw.Reddit(
        client_id = os.getenv("REDDIT_ID"),
        client_secret = os.getenv("REDDIT_SECRET"),
        user_agent = os.getenv("REDDIT_AGENT"),
    )
    print(f'instance is {reddit}')
    return reddit

async def data(subreddit_name):

    reddit = await auth()
    subreddit = await reddit.subreddit(subreddit_name)
    message = ""

    async for submission in subreddit.new(limit=10):
        entry = f'{submission.title}\n'
        message += entry
    
    await reddit.close()
    return message


asyncio.run(data('learnpython'))
