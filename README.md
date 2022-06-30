# discRedit

discRedit is a simple Discord bot coded in Python that fetches a random submission from a specified subreddit and sends it to the current channel. It is designed to run on [Replit](https://replit.com/) and be deployed on a [Replit HTTP server](https://docs.replit.com/hosting/deploying-http-servers), but you can modify it to host it on other platforms. APIs used include [discord.py](https://discordpy.readthedocs.io/en/stable/) and [Async PRAW](https://asyncpraw.readthedocs.io/en/stable/).

This bot was made with reference to the [beginner's tutorial](https://www.youtube.com/watch?v=SPTfmiYiuok) to create a Discord bot by freeCodeCamp.

### Usage

| Command                         | Description                                                                                                                                                                                                                            |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.dr r/<subreddit name>`        | Sends a random submission from the subreddit (sorted by Hot by default) to the current channel.                                                                                                                                        |
| `.dr nsfw`                      | Toggles whether to show posts from NSFW subreddits.                                                                                                                                                                                    |
| `.dr sort <type> <time filter>` | Changes how a subreddit is sorted before a random submission is chosen. Options for `type` are `hot`, `new`, `rising` and `top`. If `top`, the time filter can be specified with one of `all`, `day`, `hour`, `month`, `week`, `year`. |
| `.dr settings`                  | Shows the current settings.                                                                                                                                                                                                            |

### Quickstart

1. You need to have accounts for Replit, Discord, Reddit and [UptimeRobot](https://uptimerobot.com/).

2. Create applications for Discord (via the [Discord Developer Portal](https://www.reddit.com/prefs/apps)) and [Reddit](https://www.reddit.com/prefs/apps).

3. Install the `discord`, `asyncpraw` and `Flask` packages on Replit.

4. Create a new Repl and upload both `main.py` and `keep_alive.py` files.

5. Create secrets inside Replit for your Discord token, Reddit secret and Reddit client ID. The keys for each secret should then replace the strings inside the square brackets in lines 9, 10 and 11 of `main.py`. Also replace `REDDIT_USERNAME` in line 15 with your Reddit username (with which you create the Reddit app).

6. Run `main.py` inside Replit. A new window should appear in the top right. Copy the URL.

7. Go to UptimeRobot and add a new monitor. Monitor type is HTTP(s). Enter any friendly name you like. Paste the copied URL into the URL field. With a free account, the shortest monitoring interval we can use is 5 minutes. This is fine for Replit.

8. If using a free UptimeRobot account, uncheck any options only available for paid users. Leave other options as default and create the monitor.

9. Add the bot to your servers using the Discord Developer Portal.
