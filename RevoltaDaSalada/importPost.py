#coding: utf-8
from django.conf import settings
from django.utils import timezone
import requests, models, datetime, twitter

from twitter.oauth_dance import oauth_dance

HASHTAGS = ['revoltadasalada']

def import_instagram():
    if models.InstagramPost.objects.count():
        last_post = models.InstagramPost.objects.latest('min_tag_id')
        min_tag_id = str(last_post.min_tag_id)
    else:
        min_tag_id = "0"
    photos = None
    for hashtag in HASHTAGS:
        url = "https://api.instagram.com/v1/tags/%s/media/recent?client_id=759b7cbffd6e4ec4866dbfbb5c6ecce6&min_tag_id=%s" % (hashtag, min_tag_id)
        answer = requests.get(url).json()
        photos += answer["data"]
    if photos:
        next_min_tag_id = int(answer["pagination"]["next_min_id"])
        for photo in photos:
            try:
                id = photo["id"]
                url = photo["link"]
                photoUrl = photo["images"]["low_resolution"]["url"]
                profile_picture = photo["user"]["profile_picture"]
                caption = photo["caption"]["text"]
                username = photo["user"]["username"]
                created_at = datetime.datetime.utcfromtimestamp(float(photo["created_time"]))
                instagramPost = models.InstagramPost(description=caption, author=username,
                	author_thumbnail_url=profile_picture, url=url, original_id=id, image_url=photoUrl,
                    created_at=created_at, min_tag_id=next_min_tag_id)
                instagramPost.save()
            except:
                pass

def import_twitter():
    def login():

        try:
            (oauth_token, oauth_token_secret) = "14255439-yjVwbkd6rFtWFgTdxE8tj6mEmmr7R255YfeRA8RdB", "6uY8k4TftKZLfs7emGKETDv8LiEt2urINENVUmtC4" 
        except IOError, e:
            (oauth_token, oauth_token_secret) = oauth_dance("Revolta da Salada", settings.CONSUMER_KEY,
                    settings.CONSUMER_SECRET)
            print e.errno
            print e

        auth = twitter.oauth.OAuth(oauth_token, oauth_token_secret, settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
        return twitter.Twitter(auth=auth)
    t = login()

    tweets = []

    if models.TwitterPost.objects.count():
        last_post = models.TwitterPost.objects.latest('min_tag_id')
        min_tag_id = str(last_post.min_tag_id)
    else:
        min_tag_id = "0"

    print min_tag_id
    for hashtag in HASHTAGS:
        data = t.search.tweets(q=hashtag, since_id=min_tag_id, count=100)
        tweets += data.get('statuses', [])

    if tweets:
        next_min_tag_id = int(data["search_metadata"]["max_id_str"])
        for tweet in tweets:
            try:
                id = tweet["id_str"]
                url = "https://twitter.com/%s/status/%s" % (tweet["user"]["screen_name"], tweet["id_str"])
                profile_picture = tweet["user"]["profile_image_url"]
                caption = tweet["text"]
                username = tweet["user"]["name"]
                created_at = datetime.datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
                created_at_aware = timezone.make_aware(created_at, timezone=timezone.get_default_timezone())
                twitterPost = models.TwitterPost(description=caption, author=username,
                    author_thumbnail_url=profile_picture, url=url, original_id=id, 
                    created_at=created_at_aware, min_tag_id=next_min_tag_id)
                twitterPost.save()
            except Exception as e:
                print e
