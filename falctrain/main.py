import falcon
from falcon_auth import FalconAuthMiddleware, BasicAuthBackend

user_loader = lambda username, password: {'username': username }
auth_backend = BasicAuthBackend(user_loader)
auth_middleware = FalconAuthMiddleware(auth_backend, exempt_routes=['/exempt'], exempt_methods=['HEAD'])
api = falcon.API(middleware=[auth_middleware])

class ApiResource:

    def on_post(self, req, resp):
        user = req.context['user']
        resp.body = "User Found: {}".format(user['username'])

api.add_route("/api", ApiResource())
