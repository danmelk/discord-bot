# discord-bot

Async Discord bot with Reddit API to get random posts from four
different subreddits like: `r/Aww`, `/rShowerThoughts`, `r/Homelab`, `r/Getmotivated`. `@mention` a bot at any place at your server and click an emoji for
requesting a content.

To start-up a bot, you need to generate your environment variables:
1 - `DISCORD_TOKEN` for getting an access to API, 2 - `REDDIT_ID`, `REDDIT_SECRET`, `REDDIT_AGENT` for fetching a data from Reddit. Put them into your 
`.env` file.
Next, run `$ pip install -r requirements.txt` and `python3 discordBot.py`. 

Enjoy :)
