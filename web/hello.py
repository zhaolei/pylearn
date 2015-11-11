#!/usr/bin/env python

import web
import sys
import os

classpath = "%s/class"%os.getcwd()

print classpath
sys.path.append(classpath)

from index import index


urls = (
    '/', 'index'
)


if __name__ == "__main__":
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app = web.application(urls, globals())
    app.run()
