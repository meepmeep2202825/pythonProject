from textblob import TextBlob
import sys
import matplotlib.pyplot as plt
import tweepy

def twitter_sentiment_analysis():
    consumerKey = "LF8GcD7zp4TzeHHpTvpNiZGDW"
    consumerSecret = "qGc8dNSVJFpfvgsnqcNYKJIqy4UA8XZbH96pQebXYFlDPaYksS"
    accessToken = "1579351083314356226-Qd2rk5BAc4xmshQQio4TbQJxidb9Eq"
    accessTokenSecret = "Jfz6e3JolGEUbBGLTkEZ9EmOBBrTJxaTcEfiPMEAUk2Bj"
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAJcIiAEAAAAA0rnD7UN%2BZrHFXNgQmnhQtShpvBA%3Dr3GVIPXbmxGazKXXj6WXvqMu0aSMJOuRNDTjsCeNmH3OfQyQEr"
    client = tweepy.Client(bearer_token)

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    #api = tweepy.API(auth)
    query = 'covid19 -is:retweet lang:en'
    print('Extracting Data...')
    tweetsData = tweepy.Paginator(client.search_recent_tweets, query=query,
                              tweet_fields=['context_annotations', 'created_at', 'author_id'], max_results=100).flatten(limit=100000)

    positive = 0
    negative = 0
    neutral = 0
    polarity = 0

    print('Analysing Tweets...')

    for tweet in tweetsData.tweets:
        analysis = TextBlob(tweet.text)

        if analysis.sentiment.polarity == 0:
            neutral += 1
        if analysis.sentiment.polarity < 0.00:
            negative += 1
        if analysis.sentiment.polarity > 0.00:
            positive += 1

    print ('Plotting Pie Chart...')

    def percentage(part, whole):
        return 100 * float(part) / float(whole)

    total_tweets = negative + positive + neutral
    positive = percentage(positive, total_tweets)
    negative = percentage(negative, total_tweets)
    neutral = percentage(neutral, total_tweets)

    positive = format(positive, '.2f')
    negative = format(negative, '.2f')
    neutral = format(neutral, '.2f')

    labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%]']
    sizes = [positive, neutral, negative]
    colors = ['darkgreen', 'gold', 'red']
    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title('How the world is feeling about the ongoing COVID-19 situation')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
