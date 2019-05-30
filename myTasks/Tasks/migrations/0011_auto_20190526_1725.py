# Generated by Django 2.2.1 on 2019-05-26 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0010_auto_20190526_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('TO_DO', 'To do'), ('DOING', 'Doing'), ('DONE', 'Done')], default='TO_DO', max_length=6),
        ),
    ]