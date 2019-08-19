import praw
import tweepy
import time

CONSUMER_KEY = 'yceCLAwesrXkWtF3PYy2LYoi2'
CONSUMER_SECRET = 'iQG8Uaf225BHhbORlm7yVkA6i8slO4ntF3QRm9sMHrmmC9AQ18'
ACCESS_KEY = '1162117668519972865-PlDv6p7ixEUQxHPQpkayr8Qx39rjvI'
ACCESS_SECRET = '4now7yrabExbhBaXr1C9SKApEtJ8vDqOfjgZBYqohbesN'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

reddit = praw.Reddit(client_id = 'LvTyUgoJJf9V7g',
                     client_secret = '4SARkrVeBTbGQ1JMgUat-KIfnlI',
                     username = 'TwitterDealBot',
                     password = 'redditBot1212#',
                     user_agent = 'TwitterDealBot v1.0 by /u/TwitterDealBot')

subreddit = reddit.subreddit('deals')


def fetchReadPosts():

    readPostsFile = open('readPosts.txt', 'r')

    readPosts = []

    for line in readPostsFile:
        readPosts.append(line.strip())

    readPostsFile.close()

    return readPosts

def tweet(postTitle, postURL):
    message = postTitle + "\n" + postURL
    api.update_status(message)


def tryTweeting():
    
    readPosts = fetchReadPosts()

    readPostsFile = open('readPosts.txt', 'a')

    submissions = subreddit.new(limit = 30)

    print(readPosts)

    for post in submissions:

        if not str(post.id) in readPosts:
            if "amazon" in post.title.lower() or "amazon" in post.selftext.lower() or "amazon" in post.url.lower():
                
                tweet(post.title, post.url)

                readPostsFile.write("\n" + str(post.id))

    readPostsFile.close()

while True:
    tryTweeting()
    time.sleep(21600)