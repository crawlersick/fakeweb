#from apps.func1 import IndexHandler
from apps.func1 import proxy


def getlist():
    list_t = [ #(r"/", IndexHandler.IndexHandler),
              (r"/do", proxy.proxypost)]
    return list_t
