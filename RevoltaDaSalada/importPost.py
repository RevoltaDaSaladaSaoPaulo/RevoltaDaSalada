
from django.http import HttpResponse
import requests
import simplejson as json
import models, calendar, datetime

def import_instagram():
    if models.InstagramPost.objects.count():
        last_post = models.InstagramPost.objects.latest('min_tag_id')
        min_tag_id = str(last_post.min_tag_id)
        print min_tag_id
    else:
        min_tag_id = "0"
    url = "https://api.instagram.com/v1/tags/revoltadasalada/media/recent?client_id=759b7cbffd6e4ec4866dbfbb5c6ecce6&min_tag_id=" + min_tag_id
    answer = requests.get(url).json()
    photos = answer["data"]
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

def import_facebook(url = "https://graph.facebook.com/search?q=%23revoltadasalada&type=post"):
    answer = requests.get(url).json()
    posts = answer["data"]
    go_to_next_page = True
    if posts:
        for post in posts:
            id = post["id"]
            try:
                models.FacebookPost.objects.get(original_id=id)
                # go_to_next_page = False
                print "exist"
            except:
                author = post["from"]["name"]
                author_id = post["from"]["id"]
                profile_picture = "http://graph.facebook.com/" + author_id + "/picture"
                message = post.get("message", "")
                print "autor: " + author
                type = post["type"]
                print "type: " + type
                if type == "photo" or type == "link" or type == "video":
                    image_url = post.get("picture", "")
                    url = post.get("link", "")
                    facebookPost = models.FacebookPost(description=message, author=author,
                    author_thumbnail_url=profile_picture, url=url, original_id=id, image_url=image_url,
                    created_at=datetime.datetime.now(), content=message)
                    facebookPost.save()
    if go_to_next_page and answer.get("paging", None) and answer["paging"].get("next", None):
        import_facebook(answer["paging"]["next"])
