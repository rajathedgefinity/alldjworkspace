import sys
import logging

from passlib.hash import sha256_crypt

import falcon
import falcon_jwt


LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
LOGGER.addHandler(ch)

USERS = {
    "admin@company.com":
    {
        "email":"admin@company.com",
        "password": sha256_crypt.encrypt("adminpassword")
    }
}

class ThingsResource(object):

    def on_get(self, req, resp):
        logging.debug("Reached on_get()")
        resp.status = falcon.HTTP_200
        resp.body = {'one':1,'two':2}

COOKIE_OPTS = {"name":"my_auth_token",
                "max_age":86400,
                "path": "/things",
                "http_only": True}

login, auth_middleware = falcon_jwt.get_auth_objects(
    USERS.get, "randomsecret", 3600, token_opts=COOKIE_OPTS
)

app = falcon.API(middleware=[auth_middleware])
things = ThingsResource()

app.add_route('/things', things)
app.add_route('/login', login)
