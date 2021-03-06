import falcon, json
from .models import smarthome

class AnalyticsResource:
    __json_content = {}

    def __validate_json_input(self, req):

        try:
            self.__json_content = json.loads(req.stream.read())
            print("json from client is validated!")
            print(self.__json_content)
            return True

        except:
            self.__json_content = {}
            print("json from client is not validated")
            return False

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        validated = self.__validate_json_input(req)

        content = {
            'status': 200,
            'msg': None,
            'name':None,
            'presentstate': None,
            'dimmervalue': None,
            'dimmer': None,
            'onoffstate': None,
            'timeanddate': None,
        }

        if validated:
            if 'smarthome_name' in self.__json_content:
                smarthome_obj = smarthome.objects.get(name=self.__json_content["smarthome_name"])
                content['msg'] = "Success"
                content['name'] = smarthome_obj.name
                content['presentstate'] = smarthome_obj.presentstate
                content['dimmervalue'] = smarthome_obj.dimmervalue
                content['dimmer'] = smarthome_obj.dimmer
                content['onoffstate'] = smarthome_obj.onoffstate
                content['timeanddate'] = str(smarthome_obj.timestampnow)
            else:
                content['status'] = 404
                content['msg'] = "Do not find id in the request"
        else:
            content['status'] = 404
            content['msg'] = "Json Input is not validated"
        resp.body = json.dumps(content)

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        validated = self.__validate_json_input(req)

        content = {
            'id':None,
            'msg':'Data not Added',
        }

        if validated:
            if 'name' in self.__json_content and 'presentstate' in self.__json_content and 'dimmervalue' in self.__json_content and 'dimmer' in self.__json_content and 'onoffstate' in self.__json_content and 'timestampnow' in self.__json_content:
                smarthome_obj = smarthome.objects(name=self.__json_content['name']).update(**self.__json_content, upsert=True)
                # print(smarthome_obj.presentstate)
                # content['name'] = str(smarthome_obj.name)
                content['msg'] = 'Switch State Successfully added to Analytics Database'
            else:
                content['id'] = None
                content['msg'] = 'Json input params needed'
        else:
            content['id'] = None
            content['msg'] = "Json Input is Not Validated"
        resp.body = json.dumps(content)
