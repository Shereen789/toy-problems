import collections
class LRU:
    def __init__(self,size):
        #cachesize is the size of the cache
        self.cachesize = size
        #cache is the ordered dictionary we are using to store data
        self.cache = collections.OrderedDict()
    def put(self,key,value):
        pass
    def get(self,key):
        pass
    def getcache(self):
        pass