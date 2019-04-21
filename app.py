import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
from tornado.options import define, options
from apps import func1
define("port", default=8000, help="run on the given port", type=int)
resgister_list=[]
resgister_list.extend(func1.getlist())
print(resgister_list)
if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=resgister_list)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

