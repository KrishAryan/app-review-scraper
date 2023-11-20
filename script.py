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


# print(google_reviews)
# df = pd.DataFrame(np.array(apple_reviews.reviews),columns=['review'])
# df2 = df.join(pd.DataFrame(df.pop('review').tolist()))
# df2.head()
# df2.to_csv('/home/krish/Desktop/review.csv')