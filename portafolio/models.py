from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields import URLField


class Project (models.Model):
    title = CharField(max_length=100)
    description = TextField()
    image = ImageField(upload_to="portafolio/images/")
    url = URLField(blank=True)
