import difflib
import string

# Meant to be run after the post_transform has finished running
transformed_post_list = open('transformed_movie_posts.txt', 'r')
movie_titles = open('movie_titles.txt', 'r')

text_data = transformed_post_list.readlines()
# Have to remove the last entry, which is an integer for tracking transformation progress
text_data.pop()
transformed_post_list.close()

movie_title_list = movie_titles.readlines()
movie_titles.close()

movie_title_counter = {}
title_counter = open('title_counts', 'a')

# Each title is run through reddit post text (getting movies from reddit post text isn't tenable)
for title in movie_title_list:
    # Movie titles with a colon are often referred to by the title after the colon e.g. Avengers: Infinity War
    if ":" in title:
        fractured = title.split(":")
        movie_title_list.append(fractured[len(fractured) - 1].strip())
    movie_title_counter[title] = 0
    word_length = len(title)
    # The text is split into words so that phrases the length of the title can be compared with the title
    for text in text_data:
        words = text.split(" ")
        for index in range(0, len(words) - word_length):
            phrase = string.join(words[index:(index + word_length + 1)])
            match = difflib.SequenceMatcher(None, title, phrase)
            if match.ratio() > 0.75:
                movie_title_counter[title] += 1
    title_counter.write(title + ": " + str(movie_title_counter[title]))

title_counter.close()
