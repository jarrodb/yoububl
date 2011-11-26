# URL Routes
from tornado.web import URLSpec, StaticFileHandler
from settings import settings
import views

routes = [
    URLSpec(r"/", views.index.IndexHandler, name="index"),
    URLSpec(
        r"/comic/([a-zA-Z0-9]+)/",
        views.index.ComicHandler,
        name="comic-comic"),

    URLSpec(r"/admin/", views.admin.AdminHandler, name="admin"),
    URLSpec(
        r"/admin/comic/([a-zA-Z0-9]+)/",
        views.admin.ComicHandler,
        name="admin-comic"),

    # for development only
    (r"/static/(.*)", StaticFileHandler, dict(path=settings.static_path)),
    ]

