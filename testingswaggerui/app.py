import falcon
from falcon_swagger_ui import register_swaggerui_app

app = falcon.API()

SWAGGERUI_URL = '/swagger'
SCHEMA_URL = 'http://petstore.swagger.io/v2/swagger.json'

page_title = 'Falcon Swagger Doc'
favicon_url = 'https://falconframework.org/favicon-32x32.png'

register_swaggerui_app(
    app, SWAGGERUI_URL, SCHEMA_URL,
    page_title=page_title,
    favicon_url=favicon_url,
    config={'supportedSubmitMethods': ['get'], }
)
