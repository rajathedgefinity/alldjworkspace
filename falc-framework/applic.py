import json, falcon

class Authorize(object):
    def __init__(self, roles):
        self._roles = roles
        print(self._roles)

    def __call__(self, req, resp, resource, param):
        # DB User Get a Role.
        if 'Admin' in self._roles:
            req.user_id = 5
        else:
            raise falcon.HTTPBadRequest('Bad Request','You are not a admin right now')

class objResource:

    @falcon.before(Authorize(['Normal','Guest']))
    def on_get(self, req, resp):
        print("Trigger - Get")

        output = {
            'method' : 'get',
            'get-id' : req.user_id,
        }

        resp.media = output

    @falcon.before(Authorize(['Admin','Normal','Guest']))
    def on_post(self, req, resp):
        print("Trigger = Post")

        output = {
            'method' : 'post',
            'get-id' : req.user_id,
        }

        resp.media = output

api = falcon.API()
api.add_route('/account', objResource())
