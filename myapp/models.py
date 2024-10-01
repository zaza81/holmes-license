from django.db import models

class Documento(models.Model):
    titolo = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.titolo