# discRedit

disCredit is a simple Discord bot coded in Python that fetches a random submission from a specified subreddit and sends it to the current channel. It is designed to run on [Replit](https://replit.com/) and be deployed on a [Replit HTTP server](https://docs.replit.com/hosting/deploying-http-servers). APIs used include [discord.py](https://discordpy.readthedocs.io/en/stable/) and [Async PRAW](https://asyncpraw.readthedocs.io/en/stable/).

This bot was made with reference to the [beginner's tutorial](https://www.youtube.com/watch?v=SPTfmiYiuok) to create a Discord bot by freeCodeCamp.

### Usage

| Command  | Description |
| ------------- | ------------- |
| `.dC r/[subreddit name]`  | Sends a random submission from the subreddit (sorted by Hot by default) to the current channel.  |
| `.dC nsfw`  | Toggles whether to show NSFW posts on or off.  |
| `.dC sort [type] [time filter]` | Changes how a subreddit is sorted before a random submission is chosen. Options for `type` are `hot`, `new`, `rising` and `top`. If `top`, the time filter can be specified with one of `all`, `day`, `hour`, `month`, `week`, `year`. |
| `.dC settings` | Shows the current settings.
