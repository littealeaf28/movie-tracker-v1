import requests
from bs4 import BeautifulSoup

def update_movie_names(event, context):
    imdb_base_websites = [
        'https://www.imdb.com/search/title/?groups=top_1000&start=',
        # 'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&start=',
        # 'https://www.imdb.com/search/title/?groups=top_1000&sort=num_votes,desc&start=',
        # 'https://www.imdb.com/search/title/?groups=top_1000&sort=boxoffice_gross_us,desc&start=',
        # 'https://www.imdb.com/search/title/?groups=top_1000&sort=release_date,desc&start='
    ]

    for website in imdb_base_websites:
        for i in range(1, 1000, 50):
            imdb_website = website + str(i)
            r = requests.get(imdb_website)
            soup = BeautifulSoup(r.content, 'html.parser')
            title_elements = soup.find_all('h3', 'lister-item-header')
            for title_element in title_elements:
                title = title_element.a.string
                print(title)


# update_movie_names(None, None)

