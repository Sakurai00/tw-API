import twapi.twapi
import tweepy


def v2_oauth2():
    client = twapi.twapi.generate_api_v2(2)

    tweets = client.search_recent_tweets(query="python")

    # print(tweets)

    for tweet in tweets:
        print(tweet)


def v2_oauth1():
    client = twapi.twapi.generate_api_v2(1)

    tweets = client.search_recent_tweets(query="python", user_auth=True)

    # print(tweets)

    for tweet in tweets:
        print(tweet)


def v1_oauth2():
    api = twapi.twapi.generate_api_v1(2)

    for tweet in tweepy.Cursor(api.search_tweets, q='tweepy').items(10):
        print(tweet.text)


v1_oauth2()
# oauth2()
