# Generated by Django 2.2.10 on 2021-01-12 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='finished_at',
            field=models.DateField(null=True),
        ),
    ]
