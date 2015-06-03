"""imple webapp2 server."""
import webapp2
import jinja2
import os
import urllib
from google.appengine.ext import db

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('views'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class hotmap(webapp2.RequestHandler):

	def get(self):
		category = self.request.get("category")
		sql = "";
		if category != "":
			sql = "SELECT * FROM Tweet where search_key in ('{0}') LIMIT 1000".format(category)
		else: 
			sql = "SELECT * FROM Tweet ORDER BY addtime DESC LIMIT 1000"
		print sql
		tweets = db.GqlQuery(sql)
		
		# for tweet in tweets:
		# 	self.response.out.write(tweet.text+"<br>")
		# 	self.response.out.write(tweet.search_key+"<br>")
		# 	self.response.out.write(str(tweet.addtime)+"<br>")
		template_values = {
			'tweets': tweets,
			'category':category
			}

		template = JINJA_ENVIRONMENT.get_template('hotmap.html')
		self.response.write(template.render(template_values))
