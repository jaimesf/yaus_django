from mongoengine import Document, StringField, SequenceField


class Url(Document):
    id_url = SequenceField(required=False)
    url = StringField(max_length=2000, required=True)
