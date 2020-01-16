import os
import falcon_jsonify

dbcfg = {
    'host':'localhost',
    'port':27017,
    'username':'root',
    'password':'pass',
    'authentication_source'='admin'
}

middleware = [
    falcon_jsonify.Middleware(help_messages=True),
]
