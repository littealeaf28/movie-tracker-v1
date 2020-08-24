from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

imdb_websites = [
    'https://www.imdb.com/search/title/?groups=top_1000',
    'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc',
    'https://www.imdb.com/search/title/?groups=top_1000&sort=num_votes,desc',
    'https://www.imdb.com/search/title/?groups=top_1000&sort=boxoffice_gross_us,desc',
    'https://www.imdb.com/search/title/?groups=top_1000&sort=release_date,desc'
]

for website in imdb_websites:
    driver.get(website)
    for x in range(19):
        next_button = driver.find_element_by_css_selector('a.lister-page-next.next-page')
        next_button.click()
        driver.implicitly_wait(1000)

# driver.close()