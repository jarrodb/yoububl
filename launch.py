#!/usr/bin/env python
import sys
import os.path
from optparse import OptionParser

import tornado.httpserver
import tornado.ioloop
import tornado.web

from lib import dependencies

from routes import routes

def start_instance(settings):
    app = tornado.web.Application(routes, **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(settings.instance_port, address='127.0.0.1')

    try: tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt: pass


def main():
    from settings import settings

    parser = OptionParser()
    parser.add_option("-p", "--port", type="int", help="instance bind port")
    (options, args) = parser.parse_args()

    if options.port:
        settings.instance_port = int(options.port)

    print "Starting Tornado on port", settings.instance_port
    start_instance(settings)


if __name__ == "__main__":
    main()
