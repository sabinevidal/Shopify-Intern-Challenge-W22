from flask_wtf import FlaskForm
from wtforms import Form, Field, BooleanField, StringField, IntegerField, validators
from wtforms.fields.core import FormField
from wtforms.widgets import TextInput
from .models import *
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

class TagListField(Field):
    widget = TextInput()

    def _value(self):
        if self.data:
            return u', '.join(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [x.strip() for x in valuelist[0].split(',')]
        else:
            self.data = []

class BetterTagListField(TagListField):
    def __init__(self, label='', validators=None, remove_duplicates=True, **kwargs):
        super(BetterTagListField, self).__init__(label, validators, **kwargs)
        self.remove_duplicates = remove_duplicates

    def process_formdata(self, valuelist):
        super(BetterTagListField, self).process_formdata(valuelist)
        if self.remove_duplicates:
            self.data = list(self._remove_duplicates(self.data))

    @classmethod
    def _remove_duplicates(cls, seq):
        """Remove duplicates in a case insensitive, but case preserving manner"""
        d = {}
        for item in seq:
            if item.lower() not in d:
                d[item.lower()] = True
                yield item

class UploadImageForm(FlaskForm):
    filename = FileField(validators=[FileRequired()])
    # description = StringField()
    # tags = BetterTagListField()
    # user_id = IntegerField()

class ImageDetailsForm(FlaskForm):
    # filename = FileField(validators=[FileRequired()])
    description = StringField()
    tags = BetterTagListField()
    user_id = IntegerField()
class GiantForm(FlaskForm):
    image_file = FormField(UploadImageForm)
    image_details = FormField(ImageDetailsForm)

