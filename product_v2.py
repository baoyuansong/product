import web
import http.client, urllib.parse
import json
import configparser
import os
import sys

urls = (
    '/product/list', 'ProductList',
)

app = web.application(urls, globals())
render = web.template.render('templates/')
class ProductList:
    def GET(self):
        config = configparser.ConfigParser()
        dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
        config.read(os.path.join(dirname, "conf", "product.conf"))
        servicename = config.get("stock", "service")
        serviceport = config.get("stock", "port")
        conn = http.client.HTTPConnection(servicename + ":" + serviceport, timeout=10)            
        conn.request("GET", "/stock/list")
        res = conn.getresponse()
        content = json.loads(res.read())

if __name__ == "__main__":
    app.run()
