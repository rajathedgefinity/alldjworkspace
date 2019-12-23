import falcon, json

class awesomeclass:

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200

        validate_params = True

        if 'name' not in req.params:
            validate_params = False

        if 'age' not in req.params:
            validate_params = False

        if validate_params:
            output = {
                'name': req.params['name'],
                'age': req.params['age'],
            }
        else:
            resp.status = falcon.HTTP_400
            output = {
            'msg': 'Missing Required Params',
            }

        resp.body = json.dumps(output)

api = falcon.API()
api.add_route('/params', awesomeclass())
