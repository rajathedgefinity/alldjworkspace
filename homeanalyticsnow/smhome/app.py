import falcon
from mongoengine import connect
from .api import AnalyticsResource

connect('analytics', host='127.0.0.1', port=27017, username='root', password='pass', authentication_source='admin')
app = application = falcon.API()
smarthomeresource = AnalyticsResource()
app.add_route('/getdata',smarthomeresource)
app.add_route('/adddata',smarthomeresource)
