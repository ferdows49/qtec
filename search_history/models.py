from datetime import datetime
from django.db import models


class S_history(models.Model):
    RESULT = [
        ('A', 'All'),
        ('V', 'Verbatim')
    ]
    keyword = models.CharField(max_length=200)
    user = models.CharField(max_length=100)
    time = models.DateTimeField()
    result = models.CharField(max_length=1, choices=RESULT)

    def __str__(self):
        return self.keyword
