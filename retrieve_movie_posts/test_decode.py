from retrieve_movie_posts.b64_encodings import str_base64_decode

movie_posts_file = open('movie_posts.txt', 'r')
encoded_movie_posts = movie_posts_file.readlines()

for encoded_post in encoded_movie_posts:
    post = str_base64_decode(encoded_post)
    print(post)