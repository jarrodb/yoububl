from lib.base import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        a = self.conn.Comic.find_one()
        self.render("index.html", comic=a)

