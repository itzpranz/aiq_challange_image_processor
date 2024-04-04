from django.db import models

class ImageModel(models.Model):
    depth = models.FloatField()
    pixel_values = models.JSONField()