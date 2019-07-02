from apps.func1 import IndexHandler
from apps.func1 import proxy
def getlist():
    l=[(r"/", IndexHandler.IndexHandler),
       (r"/proxy", proxy.proxypost)]
    return l
