from dotenv import load_dotenv
import os
import praw
from b64_encodings import str_base64_encode

# Loads in credentials for PRAW from .env file
load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USER_AGENT = os.getenv('USER_AGENT')

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)
movie_subreddit = reddit.subreddit('movies')

# Clears movie posts file
open('movie_posts.txt', 'w').close()

movie_posts_file = open('movie_posts.txt', 'a+')

# Iterates through all the submissions and comments in the r/movie subreddit
# Appends their encodings to movie posts file each on a new line
for submission in movie_subreddit.top(time_filter='day'):
    movie_posts_file.write(str_base64_encode(submission.title) + '\n')
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        movie_posts_file.write(str_base64_encode(comment.body) + '\n')

movie_posts_file.close()
