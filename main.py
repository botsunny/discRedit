import os
import random
import discord
import asyncpraw
import asyncprawcore.exceptions
from replit import db
from keep_alive import keep_alive

token = os.environ['YOUR DISCORD TOKEN']
r_secret = os.environ['YOUR REDDIT SECRET']
id = os.environ['YOUR DISCORD CLIENT ID']

reddit = asyncpraw.Reddit(client_id=id,
                          client_secret=r_secret,
                          user_agent='YOUR REDDIT USERNAME')

client = discord.Client()

def update_settings(over18=None, sort=None):
    if 'over18' in db.keys():
        if over18 is not None:
            db['over18'] = over18
    else:
        db['over18'] = False if over18 is None else True

    if 'sort' in db.keys():
        if sort is not None:
            db['sort'] = sort
    else:
        db['sort'] = ['hot'] if sort is None else sort.split()

def get_submissions(sub, sort):
    if sort[0] == 'hot':
        return sub.hot()
    elif sort[0] == 'new':
        return sub.new()
    elif sort[0] == 'rising':
        return sub.rising()
    elif sort[0] == 'top':
        return sub.top(time_filter=sort[1])

@client.event
async def on_ready():
    print("Logged in as {0.user}.".format(client))
    if 'over18' not in db.keys() or 'sort' not in db.keys():
        update_settings()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '.dC settings':
        sort_str = "Sorting by {}{}.".format(db['sort'][0], ", time filter: " + db['sort'][1] if len(db['sort']) == 2 else "")
        await message.channel.send(
            "NSFW posts {}.\n{}".format('enabled' if db['over18'] else 'disabled', sort_str)
        )
    
    if message.content == '.dC nsfw':
        update_settings(over18=not db['over18'])
        await message.channel.send("NSFW posts will {} be shown.".format('now' if db['over18'] else 'not'))
        return
        
    if message.content.startswith('.dC sort'):
        split = message.content.split()
        if len(split) not in [3, 4]:
            return
        elif split[2] not in ['hot', 'new', 'rising', 'top']:
            return
        elif split[2] == 'top' and (len(split) != 4 or split[3] not in ['all', 'day', 'hour', 'month', 'week', 'year']):
            return
        else:
            update_settings(sort=split[2:])
            await message.channel.send("Sort type set to {}{}.".format(split[2], ", time filter: " + split[3] if len(split) == 4 else ""))
            return
    
    if message.content.startswith('.dC r/'):
        try:
            sub_name = message.content[6:]
        except IndexError:
            return
        
        try:
            sub = await reddit.subreddit(sub_name, fetch = True)
        except (asyncprawcore.exceptions.Redirect, asyncprawcore.exceptions.NotFound):
            await message.channel.send("Subreddit does not exist.")
            return
        else:
            if sub.over18 and not db['over18']:
                await message.channel.send("Bonk! Go to horny jail.")
                return
                
        posts = get_submissions(sub, db['sort'])
        
        submission = random.choice([post async for post in posts])
        
        if submission.is_self:
            if submission.selftext == '':
                await message.channel.send(submission.title)
            else:
                await message.channel.send(submission.selftext)
        else:
            await message.channel.send(submission.url)

keep_alive()
client.run(token)
  
