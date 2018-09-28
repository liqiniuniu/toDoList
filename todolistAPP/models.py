from django.db import models
# from django.conf import settings


class User(models.Model):
    name = models.CharField(max_length=10, blank=False)
    Email = models.EmailField(blank=False)
    password = models.CharField(max_length=20, blank=False)

    class Meta:
        unique_together = (("Email"), )


class ToDo(models.Model):
    priority_level = (
        (1, 'ordinary'),
        (2, 'urgent'),
        (3, 'important'),
    )
    finish_status = {
        (0, 'not finished'),
        (1, 'finished'),
    }
    user = models.ForeignKey(User, related_name="user_todo")
    affair = models.CharField(max_length=100, blank=False)
    priority = models.IntegerField(choices=priority_level)
    finished = models.IntegerField(choices=finish_status, default=0)
    time = models.DateField()

