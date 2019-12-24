from mongoengine import connect
from mongoengine import StringField, IntField, Document

#connect('bookdb',host='127.0.0.1',port=27017, username='root', password='pass', authentication_source='admin')

class Book(Document):
    name = StringField()
    isbn = IntField()
    author = StringField()

#simplebook = Book(name="Pythonista",isbn=12345,author="Rajath Kumar K S")
#simplebook.tags = ['mongodb','mongoengine']
#simplebook.save()
#print("Data Created")
