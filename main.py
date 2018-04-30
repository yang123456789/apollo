import tornado.ioloop
import tornado.web
import os
from tornado.options import options
import tornado.httpserver
from sqlalchemy.orm import scoped_session, sessionmaker
from conf.config import *
from views.url import *
from models import initdb, engine


class Application(tornado.web.Application):
    def __init__(self):
        initdb()
        settings = dict(
            debug=DEBUG,
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            template_path=os.path.join(os.path.dirname(__file__), 'template')
        )
        tornado.web.Application.__init__(self, urls, **settings)
        scoped_session(sessionmaker(bind=engine,
                       autocommit=False, autoflush=True,
                       expire_on_commit=False))


if __name__ == '__main__':
    options.parse_config_file("conf/apollo.conf")
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
