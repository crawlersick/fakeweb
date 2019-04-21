import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import urllib
import json
import datetime
import time
config = {
    'proxy_host': 'localhost',
    'proxy_port': 8998
}
tornado.httpclient.AsyncHTTPClient.configure(
    "tornado.curl_httpclient.CurlAsyncHTTPClient")
class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        query = self.get_argument('q')
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield tornado.gen.Task(
                client.fetch,"http://search.twitter.com/search.json?" + \
                urllib.parse.urlencode({"q": query, "result_type": "recent", "rpp": 100}),
                **config
                )
        self.write(response.body)
        self.finish()


