from django.db import models

class Comparison(models.Model):
    doc_a = models.TextField()
    doc_b = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
