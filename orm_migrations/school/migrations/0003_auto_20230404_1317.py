# Generated by Django 3.1.2 on 2023-04-04 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20230404_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='teachers', to='school.Teacher'),
        ),
    ]
