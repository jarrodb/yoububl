from os import path
from tornado.util import ObjectDict

settings_ = dict(
    debug = False,

    instance_port = 8888,

    cookie_secret = "101bunnies",
    xsrf_cookies = True,

    static_path = path.join(path.dirname(__file__), "static"),
    template_path = path.join(path.dirname(__file__), "tpl"),

    site_url = 'http://yoububl.com:81',
    login_url = '/login',
    )

# local overrides
try:
    from settings_local import settings as settings_local
    settings_.update(settings_local)
except ImportError:
    pass

settings = ObjectDict(settings_)
