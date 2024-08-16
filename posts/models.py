from django.db import models

# Create your models here.


class Post(models.Model):

    text = models.TextField()

    def __str__(self):
        """ String represenation of the model"""

        # to improve readability of your models, add str() methods
        return self.text[:50]