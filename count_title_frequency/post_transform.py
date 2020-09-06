import string
import os

# Assumes movie_posts file is accessible, and transformed_movie_posts is no longer needed if it already exists
reddit_post_list = open('movie_posts.txt', 'r')
transformed_posts = open('transformed_movie_posts', 'a')

# Checks if file is empty
if os.stat('transformed_movie_posts').st_size == 0:
    transformed_posts.write("0")
text_data = transformed_posts.readlines()
line_tracker = int(text_data.pop())

# Individual entries are stripped so program doesn't have to run continuously in a single operation
reddit_post_list.close()

# Removes text from punctuation except colon, which is often used in movie titles
current_line = 0
for text in text_data:
    # Allows transformation of posts to be performed in multiple sessions, not all at once
    if current_line < line_tracker:
        continue
    transformed = text.translate(string.maketrans("", ""), string.punctuation.replace(":", ""))
    transformed_posts.write(transformed + "\n")
    current_line += 1

transformed_posts.write(str(current_line))
transformed_posts.close()
