#from apps.func1 import IndexHandler
from apps.func1 import proxy


def getlist():
    list_t = [(r"/do", proxy.proxypost)] #(r"/", IndexHandler.IndexHandler)]
    return list_t
