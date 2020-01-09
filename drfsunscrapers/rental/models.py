from django.db import models
from django.conf import settings

# Create your models here.

class OwnedModel(models.Model):
    """Owned model

       This Module is all about what you own.

       Args:
            No (str): Nothing gonna Accept

        Returns:
            Creates simple table known as OwnedModel in the DB
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Friend(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Belonging(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Borrowed(models.Model):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{} {} {} {}'.format(self.what,self.to_who,self.when,self.returned)
