# Generated by Django 2.2.1 on 2019-05-26 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('TO_DO', 'to do'), ('DOING', 'doing'), ('DONE', 'done')], default='TO_DO', max_length=6),
        ),
    ]
