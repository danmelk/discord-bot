import asyncio
from cProfile import run
import praw
from dotenv import load_dotenv
import os
load_dotenv()

def auth():
    reddit = praw.Reddit(
        client_id = os.getenv("REDDIT_ID"),
        client_secret = os.getenv("REDDIT_SECRET"),
        user_agent = os.getenv("REDDIT_AGENT"),
    )
    print(f'instance is {reddit}')
    return reddit

def data(subreddit_name):

    reddit = auth()
    subreddit = reddit.subreddit(subreddit_name)
    message = ""

    for submission in subreddit.hot(limit=5):
        entry = f'{submission.url}\n'
        message += entry

    return message

