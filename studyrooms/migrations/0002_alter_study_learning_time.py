# Generated by Django 4.1.5 on 2023-02-16 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyrooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='learning_time',
            field=models.PositiveIntegerField(),
        ),
    ]
