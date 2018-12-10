from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=100)
    state = models.BooleanField(default=False)

    class Meta():
        db_table = 'todos'