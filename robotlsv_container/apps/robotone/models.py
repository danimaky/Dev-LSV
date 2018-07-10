from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# class MonitorizatorRobot(models.Model):
#     started = models.DateTimeField()
#     finished = models.DateTimeField()
#     response = models.CharField(max_length=250)
#     TYPE = (
#         ('RobotA''', 'robotA'),
#         ('RobotB', 'robotB')
#     )
#     type = models.CharField(choices=TYPE, default=1, max_length=50)
#     STATE = (
#         ('Waiting', 'waiting'),
#         ('Working', 'working'),
#         ('Finished', 'finished')
#     )
#     status = models.CharField(choices=STATE, default=1,  max_length=50)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user.username

class Robotmintor(models.Model):
    started = models.DateTimeField(blank=True, null=True)
    finished = models.DateTimeField(blank=True, null=True)
    response = models.CharField(max_length=250, blank=True)
    TYPE = (
        ('1', 'robotA'),
        ('2', 'robotB')
    )
    type = models.CharField(choices=TYPE, default=1, max_length=50)
    STATUS = (
        ('1', 'Waiting'),
        ('2', 'Working'),
        ('3', 'Finished'),
    )
    status = models.CharField(choices=STATUS, default=1, max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


