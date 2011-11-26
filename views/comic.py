from lib.base import BaseHandler
from mongokit import ObjectId

USER_TPL = 'comic/user.html'

class UserComicHandler(BaseHandler):
    def get(self, cid):
        oid = ObjectId(cid)
        comic = self.conn.UserComic.one({'_id': oid})

        self.render(USER_TPL, **{
            'comic': comic,
            })

