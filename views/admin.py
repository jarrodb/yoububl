import os
from mongokit import ObjectId
from forms.admin import ComicForm
from lib.base import BaseHandler
from lib.forms import TornadoMultiDict
from settings import settings

ADMIN_TPL = 'admin/admin.html'
COMIC_TPL = 'admin/comic.html'

class AdminHandler(BaseHandler):
    def get(self):
        self.render(ADMIN_TPL, **{
            'comic_form': ComicForm(),
            'error': None,
            })

    def post(self, error=None):
        allowed_types = [
            'image/gif',
            'image/jpeg',
            'image/png',
            ]
        postdata = self.request.arguments
        postdata.update(self.request.files)
        form = ComicForm(TornadoMultiDict(postdata))
        try:
            if not form.validate():
                raise ValueError('Form Error')
            c = self.conn.Comic()
            c.title = unicode(form.title.data)

            clean_fn = self.strip_file_chars(form.comic.data.filename)
            file_path = '/images/comics/%s' % (clean_fn)
            open_path = '%s/%s' % (settings.static_path, file_path)
            # check this
            open(open_path, 'w').write(form.comic.data.body)

            c.file = unicode('/static%s' % (file_path))
            c.save()
        except Exception, e:
            #c.delete()
            error = e
        else:
            self.redirect(self.reverse_url('admin-comic',unicode(c._id)))

        self.render(ADMIN_TPL, **{
            'comic_form': form,
            'error': error,
            })

    def strip_file_chars(self, filename):
        import re
        return re.sub(r'[^\w\d\-\.]','_',filename)

    def random_dir(self):
        import random
        import string
        return ''.join(
            [random.choice(string.letters+string.digits) for i in xrange(4)]
            )


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

        captions = []
        changed = False

        # process deletes FIRST
        for k in self.request.arguments:
            if k.startswith('delcaption_'):
                index = 0
                for cc in comic.captions:
                    if cc.get('title') == self.get_argument(k):
                        del comic.captions[index]
                        changed = True
                    index += 1

        # process additions
        for k in self.request.arguments:
            if k.startswith('caption_'):
                ckey = k.replace('caption_','')
                newc = self.conn.Caption()
                newc.title = unicode(ckey)
                newc.coords = self.get_argument(k)
                newc.save()
                captions.append(newc)

        if captions:
            comic.captions.extend(captions)
            comic.enabled = True
            comic.save()
        elif changed:
            comic.save()

        self.redirect(self.reverse_url('admin-comic',unicode(comic._id)))


