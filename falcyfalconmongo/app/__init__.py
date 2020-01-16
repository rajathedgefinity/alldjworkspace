import falcon
import mongoengine as mongoengine

from app.settings import middleware

app = falcon.API(middleware=middleware)

db = mongo.connect(
    'development',
    host = dbcfg['host'],
    port = dbcfg['port'],
    username = dbcfg['username'],
    password = dbcfg['password'],
    authentication_source = dbcfg['authentication_source']
)
