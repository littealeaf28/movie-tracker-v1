import difflib
import string

# Assuming code has access to movie_posts and movie_titles file
reddit_post_list = open('movie_posts.txt', 'r')
movie_titles = open('movie_titles.txt', 'r')

text_data = reddit_post_list.read().split("\n")
reddit_post_list.close()

# Strips text of punctuation
for text in text_data:
    text.translate(string.maketrans("", ""), string.punctuation)

# Gets the movie titles, assuming formatting of title\ntitle\n etc.
movie_title_list = movie_titles.read().split("\n")
movie_titles.close()

# A dictionary counter for tracking each title
movie_title_counter = {}
title_counter = open('title_counts', 'a')

# We take one title, create a dictionary entry for it, then use it to search through each text
for title in movie_title_list:
    movie_title_counter[title] = 0
    word_length = len(title)
    for text in text_data:
        words = text.split(" ")
        # Individual words are combined into a phrase as long as the title, for comparison in SequenceMatcher
        for index in range(0, len(words) - word_length):
            phrase = string.join(words[index:(index + word_length + 1)])
            match = difflib.SequenceMatcher(None, title, phrase)
            if match.ratio() > 0.75:
                movie_title_counter[title] += 1
    title_counter.write(title + ": " + str(movie_title_counter[title]))

title_counter.close()