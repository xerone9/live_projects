from django.db import models


class UploadFile(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    file = models.FileField(upload_to='uploads/')


