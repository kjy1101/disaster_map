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

# twid, time, text, user, disaster, region

class DisasterTag(models.Model):
    name=models.CharField(max_length=5)
    def __str__(self):
        return self.name


class Tweet(BaseModel):
    twid = models.TextField()
    time = models.TextField()
    text = models.TextField()
    user = models.TextField()
    disaster_tag = models.ForeignKey(DisasterTag, on_delete=models.CASCADE)
    location = models.ForeignKey(Mark, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.disaster_tag) + " - " + str(self.text)
