import falcon, json
from .models import Book

class BookResource(object):
    def on_get(self, req, resp, book_id):
        book_obj = Book.objects.get(id=book_id)
        content = {
            'author':book_obj.author,
            'name':book_obj.name,
            'isbn':book_obj.isbn,
        }
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(content)

    def on_post(self, req, resp):
        book_data = req.media
        book_obj = Book.objects.create(**book_data)
        content = {
            'book_id':str(book_obj.id),
            'msg':'Book Succesfully Added',
        }
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(content)
