from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields import DateTimeField

import datetime


class Post(models.Model):
    title = CharField(max_length=200)
    description = TextField()
    image = ImageField(upload_to="blog/images")
    date_posted = DateTimeField(datetime.date.today())
