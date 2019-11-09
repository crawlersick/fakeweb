import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen
from apps.comm.ApiPre import ApiCommon
import logging
import urllib
import json
import datetime
import time
from stringendcode import *
import base64

# curl -X POST -d '{"keyl":"http://baidu.com/"}' http://127.0.0.1:8000/do
#curl -H 'Content-Type: application/json' -X POST localhost:8000/do -d '{"keyl":"https://www.baidu.com"}'
config = {
    #    'proxy_host': 'localhost',
    #    'proxy_port': 8998
}
tornado.httpclient.AsyncHTTPClient.configure(
    "tornado.curl_httpclient.CurlAsyncHTTPClient")

myHeader = {'user-agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20191022 Firefox/70.0.1'}

class proxypost(ApiCommon):
    @tornado.gen.coroutine
    def post(self):
        param = self.my_get_post_data()
        myurl = param.get('keyl', 'NA')
        if myurl == 'NA' or not myurl:
            self.write('need keyl')
            self.finish()
            return
        try:
            logging.info('fetch... ' + myurl)
            client = tornado.httpclient.AsyncHTTPClient()
        except Exception as e:
            logging.info("Error %s" % e)
            self.write({"msg": "invalid keyl,error found"})
            self.finish()
            return

        try:
            response = yield client.fetch(myurl,headers=myHeader) #, validate_cert=False)# , **config)
        except Exception as e:
            logging.info("Error %s" % e)
            self.write({"msg": "error found"})
            self.finish()
        else:
            logging.info('>>>>>>>>>get target page header:')
            for x in response.headers.get_all():
                logging.info(x)
                # self.set_header(x[0],x[1])
            # self.write(response.body)
            try:
                self.write(response.body)
            except Exception as e:
                logging.info("Error %s" % e)
                self.write({"msg": "invalid response,error found"})
            logging.info('<<<<<<<<<<<<<<<<<<<<<<<<<<<request end')
            self.finish()
