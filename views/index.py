from lib.base import BaseHandler
from mongokit import ObjectId

COMIC_TPL = 'comic/comic.html'

class IndexHandler(BaseHandler):
    def get(self):
        # display recent 10
        recent = self.conn.UserComic.fetch().sort('create_date', -1).limit(10)
        available = self.conn.Comic.fetch().sort('create_date', -1).limit(10)
        self.render("index.html", **{
            'recent': recent,
            'available': available,
            })

class ComicHandler(BaseHandler):
    def get(self, cid):
        oid = ObjectId(cid)
        comic = self.conn.Comic.one({'_id': oid})

        self.render(COMIC_TPL, **{
            'comic': comic,
            })

    def post(self, cid):
        oid = ObjectId(cid)
        comic = self.conn.Comic.one({'_id': oid})

        usercomic = self.conn.UserComic()
        captions = []
        # process captions
        for k in self.request.arguments:
            if k.startswith('caption_'):
                title = k.replace('caption_','')
                newc = self.conn.UserCaption()
                newc.title = unicode(title)
                newc.text = self.get_argument(k)
                newc.save()
                captions.append(newc)

        usercomic.comic = comic
        usercomic.captions.extend(captions)
        usercomic.save()

        self.redirect(self.reverse_url('comic-user',unicode(usercomic._id)))


