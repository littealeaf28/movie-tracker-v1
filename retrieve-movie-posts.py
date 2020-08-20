from dotenv import load_dotenv
import os
import praw
import base64


def str_base64_encode(string):
    encoded_bytes = base64.b64encode(string.encode('utf-8'))
    encoded_string = str(encoded_bytes, 'utf-8')
    return encoded_string


# Loads in credentials for PRAW from .env file
load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USER_AGENT = os.getenv('USER_AGENT')

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)
movie_subreddit = reddit.subreddit('movies')

# Iterates through all the submissions and comments in the r/movie subreddit
# Adds the discussion to a single string
movie_posts = ''
for submission in movie_subreddit.top(time_filter='day'):
    movie_posts += submission.title + '\n'
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        movie_posts += comment.body + '\n'

encoded_movie_posts = str_base64_encode(movie_posts)

# Writes the string of all the comments for the day to a file
movie_posts_file = open('movie-posts.txt', 'w')
movie_posts_file.write(encoded_movie_posts)
movie_posts_file.close()