

from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=32)


class Task(models.Model):
    TASKS_STATUS = (
        ('TO_DO', 'To do'),
        ('DOING', 'Doing'),
        ('DONE', 'Done')
    )
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    task_status = models.CharField(max_length=6, choices=TASKS_STATUS, default="TO_DO")
    date = models.DateField(default="2019-05-26")