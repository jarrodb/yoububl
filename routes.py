# URL Routes
from tornado.web import URLSpec, StaticFileHandler
from settings import settings
import views

routes = [
    URLSpec(r"/", views.index.IndexHandler, name="index"),

    # for development only
    (r"/static/(.*)", StaticFileHandler, dict(path=settings.static_path)),
    ]

