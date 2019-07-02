import sys
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.autoreload
from tornado.options import define, options
from apps import func1
define("port", default=8000, help="run on the given port", type=int)
settings = {
            'debug': True,
           # other stuff
           }
resgister_list = []
resgister_list.extend(func1.getlist())
print(resgister_list)
if __name__ == '__main__':
    plist=sys.argv[1:]
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=resgister_list, **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    listenport=options.port if len(plist)<1 else plist[0]
    http_server.listen(listenport)
    tornado.ioloop.IOLoop.instance().start()
