from lib.base import BaseHandler
from mongokit import ObjectId

COMIC_TPL = 'comic/comic.html'

class IndexHandler(BaseHandler):
    def get(self):
        self.render("index.html")

class ComicHandler(BaseHandler):
    def get(self, cid):
        oid = ObjectId(cid)
        comic = self.conn.Comic.one({'_id': oid})

        self.render(COMIC_TPL, **{
            'comic': comic,
            })

    def post(self, cid):
        pass
