from google.appengine.ext import db

class Tweet(db.Model):
  search_key = db.StringProperty(required=True)
  text = db.StringProperty(required=True)
  latitude = db.FloatProperty()
  longtitude = db.FloatProperty()
  addtime = db.DateProperty(auto_now=True)