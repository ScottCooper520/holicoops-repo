from django.db import models

class Slide (models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title