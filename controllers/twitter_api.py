import tweepy
import datetime
import webapp2
from models.Tweet import * 

class twitter_api(webapp2.RequestHandler):

	def get(self):
		self.response.write(self.request.get("keyword"))

		# Prompt for login credentials and setup stream object
		consumer_key = ""
		consumer_secret = ""
		access_token = ""
		access_token_secret = ""

		auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		api = tweepy.API(auth)
		keyword = self.request.get("keyword")
		count =0
		search_results = api.search(q=keyword, result_type = "recent", count=100)
		for tweet in search_results: 
			if tweet.place != None:
				count+=1
				tweet.text.replace("\n", " ");				
				text = tweet.text.encode('utf8')
				print text
	            #logging.info(tweet.text)
				latitude = tweet.place.bounding_box.coordinates[0][0][0]
				longtitude = tweet.place.bounding_box.coordinates[0][0][1]
				
				e = Tweet(search_key=keyword, text=tweet.text, latitude= latitude, longtitude= longtitude)
				e.put()
