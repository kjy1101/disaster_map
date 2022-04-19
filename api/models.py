from django.contrib.gis.db import models as gismodels
from django.contrib.postgres.fields import ArrayField
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
