# Generated by Django 4.1.4 on 2022-12-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]
