import wtforms

def comic_content_types(self, field):
    allowed_types = [
        'image/gif',
        'image/jpeg',
        'image/png',
        ]
    if not field.data.content_type in allowed_types:
        raise wtforms.ValidationError('gif, jpeg, png only.')


class ComicForm(wtforms.Form):
    title = wtforms.TextField(
        u'Title',
        [wtforms.validators.required(), wtforms.validators.length(max=50)]
        )
    comic = wtforms.FileField(
        u'Comic Image',
        [wtforms.validators.required(), comic_content_types],
        )



class CaptionForm(wtforms.Form):
    pass
