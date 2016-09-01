'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'T4sEgP3kYxybwEXZCWR18mLIQ'
MY_CONSUMER_SECRET = 'krU07qXnj4uc70gOpn0o3CsDaPjdm3T7owshZgt36wNgAfhOaZ'
MY_ACCESS_TOKEN_KEY = '524534295-paB2f56UV68r81V3P7DG8gVxE7vcAbiwZ6gJCRXU'
MY_ACCESS_TOKEN_SECRET = 'Jt6BlmTDoKdKl0t7VJ8MbHUX7EhuImNx2LV4AodOobM87'

SOURCE_ACCOUNTS = ["scifri", "iraflatow", "nprscience"] #["SiliconHBO", "HouseOfCards", "Frank_Underwood", "BarackObama", "SeinfeldToday"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 2  #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "aniketg07" #The name of the account you're tweeting to.
