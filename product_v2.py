import web
import httplib
import json
import configparser
import os
import sys

urls = (
    '/product/list', 'ProductList',
)

app = web.application(urls, globals())
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
render = web.template.render(os.path.join(dirname, "templates"))
class ProductList:
    def GET(self):
        try:
            config = configparser.ConfigParser()
            config.read(os.path.join(dirname, "conf", "product.conf"))
            servicename = config.get("stock", "service")
            serviceport = config.get("stock", "port")
            conn = httplib.HTTPConnection(servicename + ":" + serviceport, timeout=10)            
            conn.request("GET", "/stock/list")
            res = conn.getresponse()
            content = json.loads(res.read())
        except Exception as e:
            content = ["fail to get product"]
        return render.product_list_v2(content)

if __name__ == "__main__":
    app.run()
