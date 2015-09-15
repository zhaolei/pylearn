import web
import sys
sys.path.append('class')
from index import index


urls = (
    '/', 'index'
)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
