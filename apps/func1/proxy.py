import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import urllib
import json
import datetime
import time
from stringendcode import *
import base64
#
config = {
#    'proxy_host': 'localhost',
#    'proxy_port': 8998
}
tornado.httpclient.AsyncHTTPClient.configure(
    "tornado.curl_httpclient.CurlAsyncHTTPClient")
class proxypost(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        param=self.request.body.decode('utf-8')
        param=json.loads(param)
        #myurl=param.get('keyl','NA')
        cnt=param.get('cnt','NA')
        looplist=param.get('looplist',[])
        if cnt == 'NA' or not looplist:
            self.write('need cnt and looplist')
            self.finish()
            return
        try:
            i
            print('fetch... '+myurl)
            client = tornado.httpclient.AsyncHTTPClient()
        except Exception as e:
            print("Error %s" % e)
            self.write({"msg":"invalid keyl,error found"})
            self.finish()
            return

        try:
            response = yield tornado.gen.Task(client.fetch,myurl,validate_cert=False,**config)
        except Exception as e:
            print("Error %s" % e)
            self.write({"msg":"error found"})
            self.finish()
        else:
            for x in response.headers.get_all():
                print(x)
                #self.set_header(x[0],x[1])
            #self.write(response.body)
            try:
                self.write(response.body)
            except Exception as e:
                print("Error %s" % e)
                self.write({"msg":"invalid response,error found"})
            self.finish()

