from mongoengine import connect
from mongoengine import StringField, BooleanField, DateTimeField, Document

# connect('analytics', host='127.0.0.1', port=27017, username='root', password='pass', authentication_source='admin')

class smarthome(Document):
    name = StringField()
    presentstate = StringField()
    onoffstate = StringField()
    timestampnow = StringField()

# smh = smarthome(name="63_fueb1_Switch_L2",presentstate="OFF",onoffstate="OFF",timestampnow="Dec 27,2019  12:22:25")
# smh.tags = ["mongodb", "mongoengine"]
# smh.save()
# print("data created")

# 0
# name	"63_fueb1_Switch_L1"
# state	"OFF"
# OnOffState	"OFF"
# label	"L1_bulbIcon"
# timestampNew	"Dec 27,2019  12:22:25"
# timestamp	"1970-01-01T05:30:00.000+0530"
