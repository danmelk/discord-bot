import asyncio
import datetime
from cProfile import run
from turtle import title
from urllib.request import ProxyBasicAuthHandler
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
    submission = await subreddit.random()
    print(submission.permalink)
    data = [submission.permalink, submission.url, submission.title, submission.score, submission.author, submission.num_comments, submission.is_self]
    titles = ['url', 'media', 'title', 'score', 'author', 'num_comments', 'is_self']
    result = dict(zip(titles, data))
    return result 

        


# asyncio.run(data('aww'))