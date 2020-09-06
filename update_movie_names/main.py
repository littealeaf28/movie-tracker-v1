from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def add_movie_titles_on_page(driver, titles):
    title_elements = driver.find_elements_by_css_selector('h3.lister-item-header')
    for title_element in title_elements:
        title = title_element.find_element_by_css_selector('a').text
        titles.append(title)


def update_movie_names(event, context):
    options = Options()
    # Get rid of headless options to see what script is doing in a browser
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                              options=options)

    imdb_websites = [
        'https://www.imdb.com/search/title/?groups=top_1000',
        'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc',
        'https://www.imdb.com/search/title/?groups=top_1000&sort=num_votes,desc',
        'https://www.imdb.com/search/title/?groups=top_1000&sort=boxoffice_gross_us,desc',
        'https://www.imdb.com/search/title/?groups=top_1000&sort=release_date,desc'
    ]

    movie_titles = []
    for website in imdb_websites:
        driver.get(website)
        add_movie_titles_on_page(driver, movie_titles)

        NUM_NEXTS = 19
        for x in range(NUM_NEXTS):
            next_button = driver.find_element_by_css_selector('a.lister-page-next.next-page')
            next_button.click()
            add_movie_titles_on_page(driver, movie_titles)
            driver.implicitly_wait(500)

    for movie_title in movie_titles:
        print(movie_title + '\n')

    driver.close()