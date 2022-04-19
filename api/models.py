from django.contrib.gis.db import models as gismodels
from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

class Mark(models.Model):
    name = models.CharField(max_length=255)
    location = gismodels.PolygonField()

    def __str__(self):
        return self.name


class DisasterTag(models.Model):
    name=models.CharField(max_length=5)
    def __str__(self):
        return self.name

class Tweet(BaseModel):
    """twid = models.TextField()
    time = models.TextField()
    text = models.TextField()
    user = models.TextField()"""
    disaster_tag = models.ManyToManyField('DisasterTag', blank=True)
    location = models.ForeignKey(Mark, on_delete=models.CASCADE, null=True, blank=True)


class Typhoon(BaseModel):
    text = models.TextField()
    location = models.ForeignKey(Mark, on_delete=models.CASCADE, null=True, blank=True)


class Downpour(BaseModel):
    text = models.TextField()
    location = models.ForeignKey(Mark, on_delete=models.CASCADE, null=True, blank=True)


class Snow(BaseModel):
    text = models.TextField()
    location = models.ForeignKey(Mark, on_delete=models.CASCADE, null=True, blank=True)


class Gale(BaseModel):
    text = models.TextField()
    location = models.ForeignKey(Mark, on_delete=models.CASCADE, null=True, blank=True)


class Drought(BaseModel):
    text = models.TextField()
    location = models.ForeignKey(Mark, on_delete=models.CASCADE, null=True, blank=True)


class Forestfire(BaseModel):
    text = models.TextField()
    location = models.ForeignKey(Mark, on_delete=models.CASCADE, null=True, blank=True)


class Earthquake(BaseModel):
    text = models.TextField()
    location = models.ForeignKey(Mark, on_delete=models.CASCADE, null=True, blank=True)


class Coldwave(BaseModel):
    text = models.TextField()
    location = models.ForeignKey(Mark, on_delete=models.CASCADE, null=True, blank=True)


class Heatwave(BaseModel):
    text = models.TextField()
    location = models.ForeignKey(Mark, on_delete=models.CASCADE, null=True, blank=True)


class Dust(BaseModel):
    text = models.TextField()
    location = models.ForeignKey(Mark, on_delete=models.CASCADE, null=True, blank=True)
