import falcon, base64, json

user_accounts = {
    'admin':'adminpassword'
}

class Authorize(object):
    def __init__(self):
        pass

    def __auth_basic(self, username, password):
        if username in user_accounts and user_accounts[username] == password:
            print('You have access')
        else:
            raise falcon.HTTPUnauthorized("Unauthorized", "Your access is not allowed")

    def __call__(self, req, resp, resource, params):
        print('Before Trigger - Class: Authorize')

        if req.auth is not None:
            auth_exp = req.auth.split(' ')
            print(auth_exp)
        else:
            None

        if auth_exp[0].lower() == 'basic':
            auth = base64.b64decode(auth_exp[1]).decode('utf-8').split(':')
            username = auth[0]
            password = auth[1]
            self.__auth_basic(username, password)
        else:
            raise falcon.HTTPNotImplemented('Not Implement', 'You donont use the right authentication method')


class ObjResource:

    @falcon.before(Authorize())
    def on_get(self, req, resp):
        print('on_get trigger')

        output = {
            'method':'get'
        }
        resp.media = output

api = falcon.API()
api.add_route('/account', ObjResource())
