# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Spider(models.Model):
    title = models.CharField(max_length= 200)
    time = models.CharField(max_length = 200)
    text = models.TextField()
    def __unicode__(self):
        return self.title
    def __unicode__(self):
        return self.time
    def __unicode__(self):
        return self.text

