from app_store_scraper import AppStore
from google_play_scraper import reviews_all,Sort,app
import pandas as pd
import numpy as np

#google playstore reviews scraper
google_reviews=reviews_all(
    "ai.devrev.mobile", #enter app id from playstore url
    country='in', #manipulate to change the country to scrape from, defaults to us
    count=100, #manipulate to control the number of google_reviews scraped
    )

#apple appstore reviews scraper
apple_reviews = AppStore(country='in', app_name='devrev') #enter app name from app store url and change country from here
apple_reviews.review(how_many=100) #manipulate to control the number of apple_reviews scraped


# Convert Google Play reviews to a DataFrame and save as CSV
df_google = pd.DataFrame(google_reviews)
df_google.to_csv('google_play_reviews.csv', index=False)

# Convert Apple Store reviews to a DataFrame and save as CSV
df_apple = pd.DataFrame(apple_reviews.reviews)
df_apple.to_csv('apple_app_store_reviews.csv', index=False)