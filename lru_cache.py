import collections
class LRU:
    def __init__(self,size):
        #cachesize is the size of the cache
        self.cachesize = size
        #cache is the ordered dictionary we are using to store data
        self.cache = collections.OrderedDict()
    def put(self,key,value):
        if key not in self.cache.keys():
            if len(self.cache)>=self.cachesize:
                #Remove and return a (key, value) pair from the dictionary.
                #Pairs are returned in LIFO order if last is true or FIFO order if false
                 self.cache.popitem(last = False)
        self.cache[key] = value
    def get(self,key):
        pass
    def getcache(self):
        pass