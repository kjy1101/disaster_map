from django.contrib.gis.db import models
from django.db.models import Model


class BaseModel(Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

class Mark(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField()

    def __str__(self):
        return self.name


class Typhoon(BaseModel):
    freq = models.IntegerField(default=0)
    text = models.TextField()


class Downpour(BaseModel):
    freq = models.IntegerField(default=0)
    text = models.TextField()


class Snow(BaseModel):
    freq = models.IntegerField(default=0)
    text = models.TextField()


class Gale(BaseModel):
    freq = models.IntegerField(default=0)
    text = models.TextField()


class Drought(BaseModel):
    freq = models.IntegerField(default=0)
    text = models.TextField()


class Forestfire(BaseModel):
    freq = models.IntegerField(default=0)
    text = models.TextField()


class Earthquake(BaseModel):
    freq = models.IntegerField(default=0)
    text = models.TextField()


class Coldwave(BaseModel):
    freq = models.IntegerField(default=0)
    text = models.TextField()


class Heatwave(BaseModel):
    freq = models.IntegerField(default=0)
    text = models.TextField()


class Dust(BaseModel):
    freq = models.IntegerField(default=0)
    text = models.TextField()
