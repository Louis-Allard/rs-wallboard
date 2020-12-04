import twitter
from .apis.api import t_key, t_secret, t_bearer, t_token, t_tokensecret

#twitter

api = twitter.Api(consumer_key=t_key, consumer_secret=t_secret, access_token_key=t_token,access_token_secret=t_tokensecret)

user=api.GetUser(screen_name='lallard_59')
fo_user=user.followers_count
fr_user=user.friends_count