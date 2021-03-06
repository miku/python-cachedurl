General purpose filesystem URL caching. 
=======================================

Note: We are not backwards-compatible, 
    we need python 2.5+ (hashlib)

Sample usage
------------

    from cachedurl import URLCache

    cache = URLCache() # get a cache instance

    page = cache.get("http://www.heise.de")
    page, hit = cache.get("http://www.heise.de", hit=True)

Defaults
--------

    directory = $HOME/.cachedurlcache
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    compress = True
    invalidate = 604800
    debug = False
    enabled = True
    proxy = None
    rotating_user_agent = False
    user_agent_list = [
        'Opera/9.0 (Windows NT 5.1; U; en) ',
        'Avant Browser (http://www.avantbrowser.com)',
        'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        ]

Todo
----

    $ pylint cachedurl.py
    2 R: 58:URLCache: Too many instance attributes (9/7)
    3 R: 61:URLCache.__init__: Too many arguments (8/5)
    4 R:127:URLCache.get: Too many branches (16/12)
    5 W:204:URLCache.stats: Unused variable 'dirs'

    ...

    Your code has been rated at 9.62/10 (previous run: 9.62/10)

