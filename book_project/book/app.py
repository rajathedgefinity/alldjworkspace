import falcon
from mongoengine import connect
from .api import BookResource

connect('bookdb',host='127.0.0.1',port=27017, username='root', password='pass', authentication_source='admin')
app = application = falcon.API()
books = BookResource()
app.add_route('/getbook/{book_id}',books)
app.add_route('/addbook/', books)
