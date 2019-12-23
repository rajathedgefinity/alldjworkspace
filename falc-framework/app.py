import json, falcon

class ObjRqustClass:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        data = json.loads(req.stream.read())
        print(data)
        content = {
            'name':'rajath',
            'age':27,
            'country':'India',
        }
        output = {}
        if 'method' not in data:
            resp.status = falcon.HTTP_501
            output['value'] = "Error: None Method found Sorry"
        else:
            if(data['method'] == 'get-name'):
                resp.status = falcon.HTTP_200
                output['value'] = content['name']
            else:
                resp.status = falcon.HTTP_400
                output['value'] = None

        resp.body = json.dumps(output)

api = falcon.API()
api.add_route('/test',ObjRqustClass())
