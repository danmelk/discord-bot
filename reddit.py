import asyncpraw
from dotenv import load_dotenv
import os
load_dotenv()

reddit = asyncpraw.Reddit(
    client_id = os.getenv("REDDIT_ID"),
    client_secret = os.getenv("REDDIT_SECRET"),
    user_agent = os.getenv("REDDIT_AGENT"),)

async def data(subreddit_name):
    subreddit = await reddit.subreddit(subreddit_name, fetch=True)
    submission = await subreddit.random()
    data = [subreddit, submission.permalink, submission.url, submission.title, submission.selftext, submission.score, submission.author, submission.num_comments, submission.is_self]
    titles = ['subreddit', 'url', 'media', 'title', 'body', 'score', 'author', 'num_comments', 'is_self']
    print(submission.url)
    result = dict(zip(titles, data))
    return result 

        
