import falcon
from falcon_auth import FalconAuthMiddleware, BasicAuthBackend, TokenAuthBackend

user_loader = lambda username, password : {'username': username}

basic_auth = BasicAuthBackend(user_loader)

auth_middleware = FalconAuthMiddleware(basic_auth)

api = falcon.API(middleware=[auth_middleware])

class ApiResource:

    auth = {
        'backend': TokenAuthBackend(user_loader = lambda token: { 'id':5 }),
        'exempt_methods': ['GET']
    }

    def on_post(self, req, resp):
        resp.body = "This Reource uses token authentication"

    def on_get(self, req, resp):
        resp.body = "This resource doesn't need authentication"

api.add_route("/api", ApiResource())
