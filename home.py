import webapp2
from controllers.hotmap import *
from controllers.tweetmap import *
from controllers.twitter_api import *


application = webapp2.WSGIApplication([
    ('/twitter_api', twitter_api),
    ('/hotmap', hotmap),
    ('/tweetmap', tweetmap),
], debug=True)
