import praw
import config
import time
import os
import requests

def bot_login():
    loginInstance = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "Respond test v0.1" )
    return loginInstance

def run_bot(loginInstance, comments_replied_to):
    print(comments_replied_to)
    print("Obtaining 20 comments")

    for comment in loginInstance.subreddit('test').comments(limit=20):
        if "sandtest" in comment.body and comment.id not in comments_replied_to and comment.author != loginInstance.user.me():
            print("'sand' has been found in comment " + comment.id)
            comment.reply(" > Sand \n\n  I don't like sand. It's coarse and rough and irritating and it gets everywhere")
            print("Replied to one comment")

            comments_replied_to.append(comment.id)
            print("ID of comment replied to " + comment.id)

            with open("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")
    print("Sleeping for 10 seconds")
    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))
            print(comments_replied_to)
    return comments_replied_to

loginInstance = bot_login()
comments_replied_to = get_saved_comments()

while True:
    run_bot(loginInstance, comments_replied_to)
